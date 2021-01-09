# meme generator

### Deployment
1. Install flask by running `pip install flask -U`
2. Run `export FLASK_APP=app.py`
3. Run `flask run --host localhost --port 3000 --reload`
4. Open up `localhost:3000`
5. Enjoy :)

#### Install Dependencies
1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`

#### Install pdftotext
1. Download and install the pdftotext CLI tool [HERE](https://www.xpdfreader.com/download.html)
2. For macOS, run `brew install pkg-config poppler python`, then `pip install pdftotext`


##### To set requirements.txt
1. `pip freeze > requirements.txt`

##### To create virtual environment
1. `python3 -m venv venv`

##### To activate virtual environment
1. `source venv/bin/activate`
