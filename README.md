# car-rating-app
The backend for a car rating app. <br>
Created by Artur Górski <br>
https://artur-gorski-car-app.herokuapp.com/admin/ <br>
Api docs (require to be logged in): <br>
https://artur-gorski-car-app.herokuapp.com/docs/swagger/


## Project styleguide
### Project structure
- #### Config
    Django Framework Configuration folder
- #### Apps
    Directory of django apps (domains)
### Apps structure:
- #### Factory
  Inside we can find extensions of factory_boy's DjangoModelFactory which are used to
  simplify model creation for test purposes.
- #### Selectors
  Gather business logic for any read operations (db and external sources)
- #### Service
  Gather business logic for write operations (db and external sources)
- #### Api
  Gather all apis, views logic, serializers etc.
- #### Models
  Django Models
- #### Admin
  Django admin panel settings

## Setup
### Docker env files
#### example .env files:
In directory ./.env/dev/ create:

* .env.backend
```
SECRET_KEY=<Your secret>
DEBUG=True
DJANGO_SETTINGS_MODULE=config.settings.dev
```
* .env.postgres
```
POSTGRES_DB=postgres
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
POSTGRES_PORT=5432
POSTGRES_HOST=db
```

## Makefile commands:
* #### python manage.py createsuperuser
```
make superuser
```
* #### python manage.py makemigrations && python manage.py migrate
```
make migrate
```

* #### python manage.py migrate && python manage.py runserver 0.0.0.0:8000
```
make runserver
```
  
* #### docker-compose -f docker-compose-dev.yml run backend bash
```
make dev_backend_bash
```
	
* #### docker-compose -f docker-compose-dev.yml up -d
```
make dev_up
```
	
* #### docker-compose -f docker-compose-dev.yml run backend make superuser
```
make dev_superuser
```
	
* #### docker-compose -f docker-compose-dev.yml build
```
make dev_build
```
	
* #### docker-compose -f docker-compose-dev.yml down
```
make dev_down
```
	
* #### docker-compose -f docker-compose-dev.yml run backend make migrate
```
make dev_migrate
```
	
* #### docker-compose -f docker-compose-dev.yml run backend python manage.py test --noinput
```
make dev_test
```
