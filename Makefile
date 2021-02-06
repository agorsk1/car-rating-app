superuser:
	python manage.py createsuperuser
migrate:
	python manage.py makemigrations && python manage.py migrate
runserver:
	python manage.py migrate && python manage.py runserver 0.0.0.0:8000
dev_backend_bash:
	docker-compose -f docker-compose-dev.yml run backend bash
dev_up:
	docker-compose -f docker-compose-dev.yml up -d
dev_superuser:
	docker-compose -f docker-compose-dev.yml run backend make superuser
dev_build:
	docker-compose -f docker-compose-dev.yml build
dev_down:
	docker-compose -f docker-compose-dev.yml down
dev_migrate:
	docker-compose -f docker-compose-dev.yml run backend make migrate
dev_test:
	docker-compose -f docker-compose-dev.yml run backend python manage.py test --noinput
