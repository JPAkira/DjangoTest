# DjangoTest
 Python/Django/Postgresql Teste
 
1. Configure database in settings
2. Run migrate to create db
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
 * /LOJA/EDITAR/<PK>/
 * /LOJA/EXCLUIR/<PK>/
 * /LOJA/<PK>/
