import argparse
import json
import os

from dotenv import load_dotenv
from jinja2 import Environment
from jinja2 import FileSystemLoader
from jinja2 import select_autoescape
from livereload import Server
from more_itertools import chunked


def get_books_info(json_file):
    books_features = []
    with open(json_file, "r") as file:
        for book in json.load(file)["books_features"]:
            content = {
                "title": book["title"],
                "author": book["author"],
                "img_src": os.path.join("..", book["img_src"]),
                "book_path": os.path.join("..", book["book_path"]),
                "comments": book["comments"],
                "genres": book["genres"]
            }
            books_features.append(content)
    return books_features


def main():
    json_path = os.path.join("json", "books_info.json")
    parser = argparse.ArgumentParser(description="Tululu books library")
    parser.add_argument("--json_path", type=str, default=json_path, help="Destination folder for json file")
    args = parser.parse_args()
    load_dotenv()
    env = Environment(
        loader=FileSystemLoader("."),
        autoescape=select_autoescape(["html", "xml"])
    )
    books_on_page = 80
    books_in_row = 2
    os.makedirs("pages", exist_ok=True)
    template = env.get_template("template.html")
    books_for_pages = list(chunked(get_books_info(args.json_path), books_on_page))

    for count, value in enumerate(books_for_pages):
        rendered_page = template.render(
            books_info=list(chunked(value, books_in_row)),
            current_page=count,
            total_pages=len(books_for_pages)
        )
        with open(os.path.join("pages", f"index{count + 1}.html"), "w", encoding="utf8") as file:
            file.write(rendered_page)

    server = Server()
    server.watch("template.html", main)
    server.serve(root=".", default_filename="./pages/index1.html")


if __name__ == "__main__":
    main()
