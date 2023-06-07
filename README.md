# E-Library

The online library that stored books which has been downloaded by [tululu parser](https://github.com/Gennadynemchin/library_parser)

The static version is deployed on Github Pages:

[GitHub Pages link](https://gennadynemchin.github.io/E-Library/pages/index1.html)

### How to use

```commandline
git clone https://github.com/Gennadynemchin/E-Library.git
```
- Create virtual environment:
```commandline
python -m venv env
```
- Then activate it:
MacOS/Linux
```commandline
source env/bin/activate
```
Windows
```commandline
env\Scripts\activate.bat
```
- Install requirements:
```commandline
pip install -r requierements.txt
```

Put json file with books info to `json` directory. Book's text and covers should be placed in `media/books`
and `media/images`

Run:
```commandline
python render_website.py
```
Pages will be generated and placed into `pages` directory

- Either follow to the first page:

http://127.0.0.1:5500/pages/index1.html

or go to the:
```commandline
<PROJECT_FOLDER>/pages/index1.html
```
then open ```index1.html``` by your browser