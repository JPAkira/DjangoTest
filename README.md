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

```html
<ol>
 <li>/LOJA/LISTAR/</li>
 <li>/LOJA/ADICIONAR/</li>
 <li>/LOJA/EDITAR/<PK>/</li>
 <li>/LOJA/EXCLUIR/<PK>/</li>
 <li>/LOJA/<PK>/</li>
</ol>
```
