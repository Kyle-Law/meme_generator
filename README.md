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
