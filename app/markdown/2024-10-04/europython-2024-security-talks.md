# EuroPython 2024 talks about security

[EuroPython 2024](https://ep2024.europython.eu/) which occurred back in July 2024
has published the talk recordings [to YouTube earlier this week](https://www.youtube.com/@EuroPythonConference/videos).
I've been under the weather for most of this week, but have had a chance to
listen to a few of the security-related talks in-between resting.

## Counting down for Cyber Resilience Act: Updates and expectations

This talk was delivered by Python Software Foundation Executive Director **Deb Nicholson** and and Board Member **Cheuk Ting Ho**.
The Cyber Resilience Act (CRA) is coming, and it'll affect more software than just the software written in the EU.
Deb and Cheuk describe the recent developments in the CRA like the creation of a new entity called the "Open Source Steward"
and how open source foundations and maintainers are preparing for the CRA.

<div><center><iframe width="560" height="315" src="https://www.youtube.com/embed/ZyC7c5fxr3A?si=AMN_8QZXSEAiOK8M" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center></div>

For the rest of this year and next year I am focusing on getting the Python ecosystem ready for
software security regulations like the CRA and SSDF from the United States.

Starting with improving the
Software Bill-of-Materials (SBOM) story for Python, because this is required by both (and likely, future)
regulations. Knowing *what* software you are running is an important first step towards being able to secure that same software.

To collaborate with other open source foundations and projects on this work, I've joined the
[Open Regulatory Compliance Working Group](https://orcwg.org/) hosted by the Eclipse Foundation.

## Towards licensing standardization in Python packaging

This talk was given by **Karolina Surma** and it detailed all the work that goes into researching, writing,
and having a Python packaging standard accepted (spoiler: it's a lot!). Karolina is working on [PEP 639](https://peps.python.org/pep-0639/) which
is for adopting the [SPDX licensing expression and identifier standards](https://spdx.org/licenses/) in Python as they are the current
state of the art for modeling complex licensing situations accurately for machine (and human) consumption.

<div><center><iframe width="560" height="315" src="https://www.youtube.com/embed/8PuhFlojJ2s?si=WG59zWOeIm0jvUJc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center></div>

This work is very important for Software Bill-of-Materials, as they require accurate license information
in this exact format. Thanks to Karolina, C.A.M. Gerlach, and many others for working for years on this PEP, it will be useful to so many uers once adopted!

## The Update Framework (TUF) joins PyPI

This talk was given by **Kairo de Araujo** and **Lukas Pühringer**
and it detailed the history and current status of The Update Framework (TUF)
integration into the Python Package Index.

TUF provides better integrity guarantees for software repositories like PyPI
like making it more difficult to "compel" the index to serve the incorrect artifacts
and to make a compromise of PyPI easier to roll-back and be certain that files hadn't been modified.
For a full history and latest status, you can view [PEP 458](https://peps.python.org/pep-0458/) and the [top-level GitHub issue](https://github.com/pypi/warehouse/issues/10672) for Warehouse.

<div><center><iframe width="560" height="315" src="https://www.youtube.com/embed/ZKcxa6Ch6mY?si=6NLnGSXpQ9YkBzWr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center></div>

I was around for the original key-signing ceremony for the PyPI TUF root keys which was [live-streamed](https://www.youtube.com/watch?v=jjAq7S49eow)
back in October 2020. Time flies, huh.

## Writing Python like it's Rust: more robust code with type hints

This talk was given by **Jakub Beránek** about using type hints for
more robust Python code. Having written
a [case-study on urllib3's adoption of type hints](https://sethmlarson.dev/tests-arent-enough-case-study-after-adding-types-to-urllib3)
to find defects that testing and other tooling missed I highly recommend type hints for Python code as well:

<div><center><iframe width="560" height="315" src="https://www.youtube.com/embed/OFRLKWacOoA?si=oFccevckHliBoR8j" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center></div>

## Accelerating Python with Rust: The PyO3 Revolution

This talk was given by **Roshan R Chandar** about using PyO3
and Rust in Python modules.

<div><center><iframe width="560" height="315" src="https://www.youtube.com/embed/_33zs20Sy0k?si=ceXbhPI88PTEi8HK" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center></div>

## Automatic Trusted Publishing with PyPI

This talk was given by **Facundo Tuesca** on using Trusted Publishing for authenticating with PyPI to publish packages.

<div><center><iframe width="560" height="315" src="https://www.youtube.com/embed/ozu48KewEl4?si=5nkQ8bgcsKnbbcbW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center></div>

## Zero Trust APIs with Python

This talk was given by **Jose Haro Peralta** on how to design and implement secure web APIs using Python,
data validation with Pydantic, and testing your APIs using tooling for detecting common security defects.

<div><center><iframe width="560" height="315" src="https://www.youtube.com/embed/CRaTRDknUkM?si=Tyx8FhEcijnrKvaT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center></div>

## Best practices for securely consuming open source in Python

This talk was given by **Cira Carey** which highlights many of today's threats targetting open source consumers.
Users should be aware of these when selecting projects to download and install.

<div><center><iframe width="560" height="315" src="https://www.youtube.com/embed/TUH_nI9XrxM?si=DG0nQJEMBj4V93GP" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></center></div>
