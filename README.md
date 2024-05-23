# Library API
## Docker bilan ModelsViewSetda

1. Django RestFrameWorkni o'rnatamiz
```shell
pip install -U pip
pip install djangorestframework
```
2. Djangoda project va app yaratib olamiz, packagelarni faylga saqlaymiz.
```shell
django-admin startproject config .
django-admin startapp library
pip freeze > requirements.txt
```
3. Dockerfile va docker-compose.yml fayl yaratib olamiz
4. Projectni dockerda ishga tushurish ketma-ketligi.
```shell
docker-compose build
docker-compose run app pyhton manage.py makemigrations
docker-compose run app pyhton manage.py migrate
docker-compose run app pyhton manage.py createsuperuser
docker-compose up
```
