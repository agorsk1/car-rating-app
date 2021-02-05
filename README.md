# car-rating-app
The backend for a car rating app. <br>
Created by Artur Górski

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
  Gather all apis, views logic
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

