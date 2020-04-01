# Silent_Guardian
 
 This project is about rendering banners based on statistical data.

## Running Locally
You can run it as below on your local:

Install Docker & Docker Compose

```
docker-compose up
```

###Connecting to DB

```
docker exec -it {postgre container id} bash

psql -U postgres

\c postgres
```

Now you are connected to DB.

Web app is available at: **0.0.0.0:8000/campaigns/{campaign_id}**


## Tests
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py test
```

