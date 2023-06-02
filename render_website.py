import os
import json
from livereload import Server, shell
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


with open('json/books_info.json', 'r') as file:
    books_info = json.load(file)['books_features']

def main():
    load_dotenv()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')
    rendered_page = template.render(
            books_info=list(chunked(books_info, 2))

    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = Server()
    server.watch('*.html', main)
    server.serve(root='.')


if __name__ == '__main__':
    main()
