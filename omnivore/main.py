from pathlib import Path

from dateutil.parser import parse as parse_datetime
from omnivoreql import OmnivoreQL


def main():
    api_token = (Path(__file__).parent / "secret.txt").read_text()
    omnivore = OmnivoreQL(api_token=api_token)
    omnivore.client.transport.timeout = 3
    omnivore.client.transport.retries = 5
    labels = [node["name"][1:] for node in omnivore.get_labels()["labels"]["labels"] if node["name"].startswith("+") and node["name"] != "+RT"]

    print("<p>")
    for label in sorted(labels):
        print(f"<h2>{label}</h2><ul>")

        cursor = None
        while True:
            articles = omnivore.get_articles(
                cursor=cursor,
                query=f"in:all label:\"+{label}\" label:\"+RT\""
            )
            edges = articles["search"]["edges"]
            article_date_name_url_author = []
            for edge in edges:
                article_date = parse_datetime(edge['node']['createdAt'])
                article_date_name_url_author.append((
                    article_date,
                    edge['node']['title'],
                    edge['node']['url'],
                    edge['node']['author'] or None
                ))
            for date, title, url, author in sorted(article_date_name_url_author, reverse=True):
                print(f"<li>“<a href=\"{url}\">{title}</a>”{' by <strong>' + author + '</strong>' if author else ''}</li>")
            if not edges:
                break
            cursor = articles["search"]["edges"][-1]["cursor"]

        print("</ul>")
    print("</p>")


if __name__ == "__main__":
    main()
