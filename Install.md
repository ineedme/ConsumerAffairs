# Setup
#### Clone Github Repository
```bash
git clone https://github.com/ineedme/ConsumerAffairs.git
```

#### Create and activate a new Virtual Environment
```bash
cd ConsumerAffairs
python -m venv virt_env
```
**Activate Environment**

- on windows
```bash 
virt_env\Scripts\activate.bat
```
- on linux
```bash
source virt_env\bin\activate
```

#### Install requirements
```bash
pip install -r requirements.txt
```

#### Migrate Database and load data
```bash
python manage.py makemigrations reviews
python manage.py migrate
python manage.py fixture.json
```

### Run Server
```bash
python manage.py runserver
```

#### Coverage Check
```bash
coverage erase
corevage run manage.py test
coverage html
```
- open on browser ./htmlcov/index.html