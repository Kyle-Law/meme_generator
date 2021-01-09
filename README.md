# Meme generator

> A meme generator powered by Python and Flask. There're 2 interfaces for generating meme, web and CLI.

### Concepts practiced
- Object Oriented Programming
- `__init__.py` in building python modules
- Using external libraries
- Python Virtual Environment
- Strategy Object Design Pattern - Abstract Base Class
- Python in Systems - using Argparser and Subprocess

### Deployment
1. Install dependencies by running ``pip install -r requirements.txt``
2. Run `export FLASK_APP=app.py`
3. Run `flask run --host localhost --port 3000 --reload`
4. Open up [localhost:3000](http://localhost:3000/)
5. Enjoy :)

### Features (Web App)
- Some default memes and images are feeded.
- User can create new meme given image link, text, and author.
- New meme will be stored under the `output` folder.
- User can visit web version by following the deployment below.

### Features (CLI)
- User can create meme by running `python3 meme.py`
- Meme is created and stored under `output_cli` folder
- User can customize body and author of the meme by giving `--body` and `--author` options. (Note: body and author are either both presented, or not at all. )
- User can customize image by pointing to the image location (locally) with `--path` option. For example, `python3 meme.py --path ./_data/photos/coding/coding1.jpeg --body "Python is fun" --author "Kyle Law"`

## Built With

- Python
- Flask
- Libraries: python-docx, pandas, Pillow, flask, requests, argparser

### Inheritance Flow
- IngestorInterface > CSV, Docx, PDF, Text Ingestors
- Ultimately all file ingestors are aggregated into an `Ingestor` class

## Authors

👤 **Kyle Law**

- Github: [@Kyle-Law](https://github.com/Kyle-Law)
- Linkedin: [Kyle law](https://www.linkedin.com/in/kyle-lawzhunkhing/)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

Feel free to check the [issues page](https://github.com/Kyle-Law/meme-generator/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc).

## Show your support

Give a ⭐️ if you like this project!

## Acknowledgments

- Udacity Intermediate Python Nanodegree

## 📝 License

This project is [MIT](LICENSE) licensed.


### References

#### Install Dependencies in virtual environment
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

#### Install pdftotext
1. Download and install the pdftotext CLI tool [HERE](https://www.xpdfreader.com/download.html)
2. For macOS, run `brew install pkg-config poppler python`, then `pip install pdftotext`

#### Update pip setuptools
1. Run `pip install -U setuptools`

#### Using subprocess
1. Install emoj by `npm install --global emoj` and add the code required to implement `subprocess.Popen` to call this tool from within our Python script. [References](https://docs.python.org/3/library/subprocess.html#subprocess.Popen)

##### To set requirements.txt
1. `pip freeze > requirements.txt`

##### To create virtual environment
1. `python3 -m venv venv`

##### To activate virtual environment
1. `source venv/bin/activate`
