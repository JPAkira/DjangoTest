# DjangoTest
 Python/Django/Postgresql Teste
 
1. Configure database in settings
```sh
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```
3. Run migrate to create db
```sh
python manage.py migrate
```
3. Create superuser to access api's
```sh
python manage.py createsuperuser
```
4. Add file to date folder
5. Use the command to import data from the file
```sh
python manage.py import_data <File_Name.csv>
```
6. API'S URLS:

 * /LOJA/LISTAR/
 * /LOJA/ADICIONAR/
 * /LOJA/EDITAR/(PK)/
 * /LOJA/EXCLUIR/(PK)/
 * /LOJA/(PK)/
