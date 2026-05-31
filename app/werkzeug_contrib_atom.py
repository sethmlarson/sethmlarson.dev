# -*- coding: utf-8 -*-

# Vendored copy of werkzeug.contrib.atom prior to v1.0.
# License: BSD-3-Clause

"""
    werkzeug.contrib.atom
    ~~~~~~~~~~~~~~~~~~~~~

    This module provides a class called :class:`AtomFeed` which can be
    used to generate feeds in the Atom syndication format (see :rfc:`4287`).

    Example::

        def atom_feed(request):
            feed = AtomFeed("My Blog", feed_url=request.url,
                            url=request.host_url,
                            subtitle="My example blog for a feed test.")
            for post in Post.query.limit(10).all():
                feed.add(post.title, post.body, content_type='html',
                         author=post.author, url=post.url, id=post.uid,
                         updated=post.last_update, published=post.pub_date)
            return feed.get_response()

    :copyright: 2007 Pallets
    :license: BSD-3-Clause
"""
from datetime import datetime

from werkzeug.wrappers.response import Response

# flake8: noqa
# This whole file is full of lint errors
import functools
import operator
import sys

try:
    import builtins
except ImportError:
    import __builtin__ as builtins


PY2 = sys.version_info[0] == 2
WIN = sys.platform.startswith("win")

_identity = lambda x: x

if PY2:
    unichr = unichr
    text_type = unicode
    string_types = (str, unicode)
    integer_types = (int, long)

    iterkeys = lambda d, *args, **kwargs: d.iterkeys(*args, **kwargs)
    itervalues = lambda d, *args, **kwargs: d.itervalues(*args, **kwargs)
    iteritems = lambda d, *args, **kwargs: d.iteritems(*args, **kwargs)

    iterlists = lambda d, *args, **kwargs: d.iterlists(*args, **kwargs)
    iterlistvalues = lambda d, *args, **kwargs: d.iterlistvalues(*args, **kwargs)

    int_to_byte = chr
    iter_bytes = iter

    import collections as collections_abc

    exec("def reraise(tp, value, tb=None):\n raise tp, value, tb")

    def fix_tuple_repr(obj):
        def __repr__(self):
            cls = self.__class__
            return "%s(%s)" % (
                cls.__name__,
                ", ".join(
                    "%s=%r" % (field, self[index])
                    for index, field in enumerate(cls._fields)
                ),
            )

        obj.__repr__ = __repr__
        return obj

    def implements_iterator(cls):
        cls.next = cls.__next__
        del cls.__next__
        return cls

    def implements_to_string(cls):
        cls.__unicode__ = cls.__str__
        cls.__str__ = lambda x: x.__unicode__().encode("utf-8")
        return cls

    def native_string_result(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs).encode("utf-8")

        return functools.update_wrapper(wrapper, func)

    def implements_bool(cls):
        cls.__nonzero__ = cls.__bool__
        del cls.__bool__
        return cls

    from itertools import imap, izip, ifilter

    range_type = xrange

    from StringIO import StringIO
    from cStringIO import StringIO as BytesIO

    NativeStringIO = BytesIO

    def make_literal_wrapper(reference):
        return _identity

    def normalize_string_tuple(tup):
        """Normalizes a string tuple to a common type. Following Python 2
        rules, upgrades to unicode are implicit.
        """
        if any(isinstance(x, text_type) for x in tup):
            return tuple(to_unicode(x) for x in tup)
        return tup

    def try_coerce_native(s):
        """Try to coerce a unicode string to native if possible. Otherwise,
        leave it as unicode.
        """
        try:
            return to_native(s)
        except UnicodeError:
            return s

    wsgi_get_bytes = _identity

    def wsgi_decoding_dance(s, charset="utf-8", errors="replace"):
        return s.decode(charset, errors)

    def wsgi_encoding_dance(s, charset="utf-8", errors="replace"):
        if isinstance(s, bytes):
            return s
        return s.encode(charset, errors)

    def to_bytes(x, charset=sys.getdefaultencoding(), errors="strict"):
        if x is None:
            return None
        if isinstance(x, (bytes, bytearray, buffer)):
            return bytes(x)
        if isinstance(x, unicode):
            return x.encode(charset, errors)
        raise TypeError("Expected bytes")

    def to_native(x, charset=sys.getdefaultencoding(), errors="strict"):
        if x is None or isinstance(x, str):
            return x
        return x.encode(charset, errors)


else:
    unichr = chr
    text_type = str
    string_types = (str,)
    integer_types = (int,)

    iterkeys = lambda d, *args, **kwargs: iter(d.keys(*args, **kwargs))
    itervalues = lambda d, *args, **kwargs: iter(d.values(*args, **kwargs))
    iteritems = lambda d, *args, **kwargs: iter(d.items(*args, **kwargs))

    iterlists = lambda d, *args, **kwargs: iter(d.lists(*args, **kwargs))
    iterlistvalues = lambda d, *args, **kwargs: iter(d.listvalues(*args, **kwargs))

    int_to_byte = operator.methodcaller("to_bytes", 1, "big")
    iter_bytes = functools.partial(map, int_to_byte)

    import collections.abc as collections_abc

    def reraise(tp, value, tb=None):
        if value.__traceback__ is not tb:
            raise value.with_traceback(tb)
        raise value

    fix_tuple_repr = _identity
    implements_iterator = _identity
    implements_to_string = _identity
    implements_bool = _identity
    native_string_result = _identity
    imap = map
    izip = zip
    ifilter = filter
    range_type = range

    from io import StringIO, BytesIO

    NativeStringIO = StringIO

    _latin1_encode = operator.methodcaller("encode", "latin1")

    def make_literal_wrapper(reference):
        if isinstance(reference, text_type):
            return _identity
        return _latin1_encode

    def normalize_string_tuple(tup):
        """Ensures that all types in the tuple are either strings
        or bytes.
        """
        tupiter = iter(tup)
        is_text = isinstance(next(tupiter, None), text_type)
        for arg in tupiter:
            if isinstance(arg, text_type) != is_text:
                raise TypeError(
                    "Cannot mix str and bytes arguments (got %s)" % repr(tup)
                )
        return tup

    try_coerce_native = _identity
    wsgi_get_bytes = _latin1_encode

    def wsgi_decoding_dance(s, charset="utf-8", errors="replace"):
        return s.encode("latin1").decode(charset, errors)

    def wsgi_encoding_dance(s, charset="utf-8", errors="replace"):
        if isinstance(s, text_type):
            s = s.encode(charset)
        return s.decode("latin1", errors)

    def to_bytes(x, charset=sys.getdefaultencoding(), errors="strict"):
        if x is None:
            return None
        if isinstance(x, (bytes, bytearray, memoryview)):  # noqa
            return bytes(x)
        if isinstance(x, str):
            return x.encode(charset, errors)
        raise TypeError("Expected bytes")

    def to_native(x, charset=sys.getdefaultencoding(), errors="strict"):
        if x is None or isinstance(x, str):
            return x
        return x.decode(charset, errors)


def to_unicode(
    x, charset=sys.getdefaultencoding(), errors="strict", allow_none_charset=False
):
    if x is None:
        return None
    if not isinstance(x, bytes):
        return text_type(x)
    if charset is None and allow_none_charset:
        return x
    return x.decode(charset, errors)


def escape(s, quote=None):
    """Replace special characters "&", "<", ">" and (") to HTML-safe sequences.

    There is a special handling for `None` which escapes to an empty string.

    .. versionchanged:: 0.9
       `quote` is now implicitly on.

    :param s: the string to escape.
    :param quote: ignored.
    """
    if s is None:
        return ""
    elif hasattr(s, "__html__"):
        return text_type(s.__html__())
    elif not isinstance(s, string_types):
        s = text_type(s)
    if quote is not None:
        from warnings import warn

        warn(
            "The 'quote' parameter is no longer used as of version 0.9"
            " and will be removed in version 1.0.",
            DeprecationWarning,
            stacklevel=2,
        )
    s = (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )
    return s


XHTML_NAMESPACE = "http://www.w3.org/1999/xhtml"


def _make_text_block(name, content, content_type=None):
    """Helper function for the builder that creates an XML text block."""
    if content_type == "xhtml":
        return u'<%s type="xhtml"><div xmlns="%s">%s</div></%s>\n' % (
            name,
            XHTML_NAMESPACE,
            content,
            name,
        )
    if not content_type:
        return u"<%s>%s</%s>\n" % (name, escape(content), name)
    return u'<%s type="%s">%s</%s>\n' % (name, content_type, escape(content), name)


def format_iso8601(obj):
    """Format a datetime object for iso8601"""
    iso8601 = obj.isoformat()
    if obj.tzinfo:
        return iso8601
    return iso8601 + "Z"


@implements_to_string
class AtomFeed(object):

    """A helper class that creates Atom feeds.

    :param title: the title of the feed. Required.
    :param title_type: the type attribute for the title element.  One of
                       ``'html'``, ``'text'`` or ``'xhtml'``.
    :param url: the url for the feed (not the url *of* the feed)
    :param id: a globally unique id for the feed.  Must be an URI.  If
               not present the `feed_url` is used, but one of both is
               required.
    :param updated: the time the feed was modified the last time.  Must
                    be a :class:`datetime.datetime` object.  If not
                    present the latest entry's `updated` is used.
                    Treated as UTC if naive datetime.
    :param feed_url: the URL to the feed.  Should be the URL that was
                     requested.
    :param author: the author of the feed.  Must be either a string (the
                   name) or a dict with name (required) and uri or
                   email (both optional).  Can be a list of (may be
                   mixed, too) strings and dicts, too, if there are
                   multiple authors. Required if not every entry has an
                   author element.
    :param icon: an icon for the feed.
    :param logo: a logo for the feed.
    :param rights: copyright information for the feed.
    :param rights_type: the type attribute for the rights element.  One of
                        ``'html'``, ``'text'`` or ``'xhtml'``.  Default is
                        ``'text'``.
    :param subtitle: a short description of the feed.
    :param subtitle_type: the type attribute for the subtitle element.
                          One of ``'text'``, ``'html'``, ``'text'``
                          or ``'xhtml'``.  Default is ``'text'``.
    :param links: additional links.  Must be a list of dictionaries with
                  href (required) and rel, type, hreflang, title, length
                  (all optional)
    :param generator: the software that generated this feed.  This must be
                      a tuple in the form ``(name, url, version)``.  If
                      you don't want to specify one of them, set the item
                      to `None`.
    :param entries: a list with the entries for the feed. Entries can also
                    be added later with :meth:`add`.

    For more information on the elements see
    http://www.atomenabled.org/developers/syndication/

    Everywhere where a list is demanded, any iterable can be used.
    """

    default_generator = ("Werkzeug", None, None)

    def __init__(self, title=None, entries=None, **kwargs):
        self.title = title
        self.title_type = kwargs.get("title_type", "text")
        self.url = kwargs.get("url")
        self.feed_url = kwargs.get("feed_url", self.url)
        self.id = kwargs.get("id", self.feed_url)
        self.updated = kwargs.get("updated")
        self.author = kwargs.get("author", ())
        self.icon = kwargs.get("icon")
        self.logo = kwargs.get("logo")
        self.rights = kwargs.get("rights")
        self.rights_type = kwargs.get("rights_type")
        self.subtitle = kwargs.get("subtitle")
        self.subtitle_type = kwargs.get("subtitle_type", "text")
        self.generator = kwargs.get("generator")
        if self.generator is None:
            self.generator = self.default_generator
        self.links = kwargs.get("links", [])
        self.entries = list(entries) if entries else []

        if not hasattr(self.author, "__iter__") or isinstance(
            self.author, string_types + (dict,)
        ):
            self.author = [self.author]
        for i, author in enumerate(self.author):
            if not isinstance(author, dict):
                self.author[i] = {"name": author}

        if not self.title:
            raise ValueError("title is required")
        if not self.id:
            raise ValueError("id is required")
        for author in self.author:
            if "name" not in author:
                raise TypeError("author must contain at least a name")

    def add(self, *args, **kwargs):
        """Add a new entry to the feed.  This function can either be called
        with a :class:`FeedEntry` or some keyword and positional arguments
        that are forwarded to the :class:`FeedEntry` constructor.
        """
        if len(args) == 1 and not kwargs and isinstance(args[0], FeedEntry):
            self.entries.append(args[0])
        else:
            kwargs["feed_url"] = self.feed_url
            self.entries.append(FeedEntry(*args, **kwargs))

    def __repr__(self):
        return "<%s %r (%d entries)>" % (
            self.__class__.__name__,
            self.title,
            len(self.entries),
        )

    def generate(self):
        """Return a generator that yields pieces of XML."""
        # atom demands either an author element in every entry or a global one
        if not self.author:
            if any(not e.author for e in self.entries):
                self.author = ({"name": "Unknown author"},)

        if not self.updated:
            dates = sorted([entry.updated for entry in self.entries])
            self.updated = dates[-1] if dates else datetime.utcnow()

        yield u'<?xml version="1.0" encoding="utf-8"?>\n'
        yield u'<feed xmlns="http://www.w3.org/2005/Atom">\n'
        yield "  " + _make_text_block("title", self.title, self.title_type)
        yield u"  <id>%s</id>\n" % escape(self.id)
        yield u"  <updated>%s</updated>\n" % format_iso8601(self.updated)
        if self.url:
            yield u'  <link href="%s" />\n' % escape(self.url)
        if self.feed_url:
            yield u'  <link href="%s" rel="self" />\n' % escape(self.feed_url)
        for link in self.links:
            yield u"  <link %s/>\n" % "".join(
                '%s="%s" ' % (k, escape(link[k])) for k in link
            )
        for author in self.author:
            yield u"  <author>\n"
            yield u"    <name>%s</name>\n" % escape(author["name"])
            if "uri" in author:
                yield u"    <uri>%s</uri>\n" % escape(author["uri"])
            if "email" in author:
                yield "    <email>%s</email>\n" % escape(author["email"])
            yield "  </author>\n"
        if self.subtitle:
            yield "  " + _make_text_block("subtitle", self.subtitle, self.subtitle_type)
        if self.icon:
            yield u"  <icon>%s</icon>\n" % escape(self.icon)
        if self.logo:
            yield u"  <logo>%s</logo>\n" % escape(self.logo)
        if self.rights:
            yield "  " + _make_text_block("rights", self.rights, self.rights_type)
        generator_name, generator_url, generator_version = self.generator
        if generator_name or generator_url or generator_version:
            tmp = [u"  <generator"]
            if generator_url:
                tmp.append(u' uri="%s"' % escape(generator_url))
            if generator_version:
                tmp.append(u' version="%s"' % escape(generator_version))
            tmp.append(u">%s</generator>\n" % escape(generator_name))
            yield u"".join(tmp)
        for entry in self.entries:
            for line in entry.generate():
                yield u"  " + line
        yield u"</feed>\n"

    def to_string(self):
        """Convert the feed into a string."""
        return u"".join(self.generate())

    def get_response(self):
        """Return a response object for the feed."""
        return Response(self.to_string(), mimetype="application/atom+xml")

    def __call__(self, environ, start_response):
        """Use the class as WSGI response object."""
        return self.get_response()(environ, start_response)

    def __str__(self):
        return self.to_string()


@implements_to_string
class FeedEntry(object):

    """Represents a single entry in a feed.

    :param title: the title of the entry. Required.
    :param title_type: the type attribute for the title element.  One of
                       ``'html'``, ``'text'`` or ``'xhtml'``.
    :param content: the content of the entry.
    :param content_type: the type attribute for the content element.  One
                         of ``'html'``, ``'text'`` or ``'xhtml'``.
    :param summary: a summary of the entry's content.
    :param summary_type: the type attribute for the summary element.  One
                         of ``'html'``, ``'text'`` or ``'xhtml'``.
    :param url: the url for the entry.
    :param id: a globally unique id for the entry.  Must be an URI.  If
               not present the URL is used, but one of both is required.
    :param updated: the time the entry was modified the last time.  Must
                    be a :class:`datetime.datetime` object.  Treated as
                    UTC if naive datetime. Required.
    :param author: the author of the entry.  Must be either a string (the
                   name) or a dict with name (required) and uri or
                   email (both optional).  Can be a list of (may be
                   mixed, too) strings and dicts, too, if there are
                   multiple authors. Required if the feed does not have an
                   author element.
    :param published: the time the entry was initially published.  Must
                      be a :class:`datetime.datetime` object.  Treated as
                      UTC if naive datetime.
    :param rights: copyright information for the entry.
    :param rights_type: the type attribute for the rights element.  One of
                        ``'html'``, ``'text'`` or ``'xhtml'``.  Default is
                        ``'text'``.
    :param links: additional links.  Must be a list of dictionaries with
                  href (required) and rel, type, hreflang, title, length
                  (all optional)
    :param categories: categories for the entry. Must be a list of dictionaries
                       with term (required), scheme and label (all optional)
    :param xml_base: The xml base (url) for this feed item.  If not provided
                     it will default to the item url.

    For more information on the elements see
    http://www.atomenabled.org/developers/syndication/

    Everywhere where a list is demanded, any iterable can be used.
    """

    def __init__(self, title=None, content=None, feed_url=None, **kwargs):
        self.title = title
        self.title_type = kwargs.get("title_type", "text")
        self.content = content
        self.content_type = kwargs.get("content_type", "html")
        self.url = kwargs.get("url")
        self.id = kwargs.get("id", self.url)
        self.updated = kwargs.get("updated")
        self.summary = kwargs.get("summary")
        self.summary_type = kwargs.get("summary_type", "html")
        self.author = kwargs.get("author", ())
        self.published = kwargs.get("published")
        self.rights = kwargs.get("rights")
        self.links = kwargs.get("links", [])
        self.categories = kwargs.get("categories", [])
        self.xml_base = kwargs.get("xml_base", feed_url)

        if not hasattr(self.author, "__iter__") or isinstance(
            self.author, string_types + (dict,)
        ):
            self.author = [self.author]
        for i, author in enumerate(self.author):
            if not isinstance(author, dict):
                self.author[i] = {"name": author}

        if not self.title:
            raise ValueError("title is required")
        if not self.id:
            raise ValueError("id is required")
        if not self.updated:
            raise ValueError("updated is required")

    def __repr__(self):
        return "<%s %r>" % (self.__class__.__name__, self.title)

    def generate(self):
        """Yields pieces of ATOM XML."""
        base = ""
        if self.xml_base:
            base = ' xml:base="%s"' % escape(self.xml_base)
        yield u"<entry%s>\n" % base
        yield u"  " + _make_text_block("title", self.title, self.title_type)
        yield u"  <id>%s</id>\n" % escape(self.id)
        yield u"  <updated>%s</updated>\n" % format_iso8601(self.updated)
        if self.published:
            yield u"  <published>%s</published>\n" % format_iso8601(self.published)
        if self.url:
            yield u'  <link href="%s" />\n' % escape(self.url)
        for author in self.author:
            yield u"  <author>\n"
            yield u"    <name>%s</name>\n" % escape(author["name"])
            if "uri" in author:
                yield u"    <uri>%s</uri>\n" % escape(author["uri"])
            if "email" in author:
                yield u"    <email>%s</email>\n" % escape(author["email"])
            yield u"  </author>\n"
        for link in self.links:
            yield u"  <link %s/>\n" % "".join(
                '%s="%s" ' % (k, escape(link[k])) for k in link
            )
        for category in self.categories:
            yield u"  <category %s/>\n" % "".join(
                '%s="%s" ' % (k, escape(category[k])) for k in category
            )
        if self.summary:
            yield u"  " + _make_text_block("summary", self.summary, self.summary_type)
        if self.content:
            yield u"  " + _make_text_block("content", self.content, self.content_type)
        yield u"</entry>\n"

    def to_string(self):
        """Convert the feed item into a unicode object."""
        return u"".join(self.generate())

    def __str__(self):
        return self.to_string()