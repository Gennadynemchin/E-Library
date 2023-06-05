import os
import json
from livereload import Server, shell
from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, select_autoescape
from more_itertools import chunked


def get_books_info(json_file):
    books_features = []
    with open(json_file, 'r') as file:
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

'''
def create_pages(template, books_info):
    os.makedirs('pages', exist_ok=True)
    print(len(books_info))
    for count, books in enumerate(books_info):
        rendered_page = template.render(
                books_info=list(chunked(books, 2)),
                page_numbers=count)
        with open(os.path.join('pages', f'index{count+1}.html'), 'w', encoding="utf8") as file:
            file.write(rendered_page)
        return count
'''

def main():
    load_dotenv()
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    os.makedirs('pages', exist_ok=True)
    template = env.get_template('template.html')
    books_for_pages = list(chunked(get_books_info('json/books_info.json'), 10))

    for count, value in enumerate(books_for_pages):
        rendered_page = template.render(
                books_info=list(chunked(value, 2)),
                current_page=count,
                total_pages=len(books_for_pages)
        )
        with open(os.path.join('pages', f'index{count+1}.html'), 'w', encoding="utf8") as file:
            file.write(rendered_page)

    server = Server()
    server.watch('template.html', main)
    server.serve(root='.', default_filename='./pages/index1.html')


if __name__ == '__main__':
    main()
