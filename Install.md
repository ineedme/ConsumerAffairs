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
---
- User: admin
- Password: password_123
- Token: 1d57dc76826cc7dd049221113170d122e59fa5ee
---
- User: player_one
- Password: password_123
- Token: d1b97ef8ecd16341342b931964267ad19ef7ac97
---
### Run Server
```bash
python manage.py runserver
```

## Testing
While the server is running
```bash
curl -X GET http://127.0.0.1:8000/api/reviews/ -H 'Authorization: Token 1d57dc76826cc7dd049221113170d122e59fa5ee'
```

Or directly through the browser, by going to the URL [http://127.0.0.1:8000/api/reviews/](http://127.0.0.1:8000/api/reviews/)

#### Coverage Check
```bash
coverage erase
corevage run manage.py test
coverage html
```
- open on browser ./htmlcov/index.html
