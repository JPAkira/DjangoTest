import os

import pandas as pd
from django.core.management.base import BaseCommand
from loja.models import Loja
from sqlalchemy import create_engine
from django.conf import settings

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('nome_do_arquivo')

    def handle(self, *args, **options):
        nome_do_arquivo = options['nome_do_arquivo']
        data = os.path.join(settings.BASE_DIR, "data", nome_do_arquivo)
        df = pd.read_csv(data, index_col=0)

        df['postalCode'] = df.postalCode.str.strip()

        usuario = settings.DATABASES['default']['USER']
        senha = settings.DATABASES['default']['PASSWORD']
        nome_do_banco = settings.DATABASES['default']['NAME']

        database_url = f'postgresql://{usuario}:{senha}@localhost:5432/{nome_do_banco}'

        engine = create_engine(database_url, echo=False)

        df.to_sql(Loja._meta.db_table, if_exists='append', con=engine, index=False)