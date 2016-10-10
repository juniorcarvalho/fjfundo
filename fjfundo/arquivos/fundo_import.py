import csv
import os.path
import re
from django.conf import settings
from datetime import datetime
from fjfundo.mensalidades.models import Fundo


def importar(self):
    filename = settings.CSV_ROOT + '/fundo.csv'
    if os.path.isfile(filename):
        with open(filename, newline='') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if row[1] == 'NOME_FUNDO':
                    continue

                id = int(row[0])
                cnpj = re.sub(r'[^0-9]', '', row[4])

                fundoSearch = Fundo.objects.filter(pk=id)
                if fundoSearch.exists():
                    fundoSearch.update(id=id, nome_fundo=row[1],
                                       data_inicial=datetime.strptime(row[2], '%d.%m.%Y').date(),
                                       data_final=datetime.strptime(row[3], '%d.%m.%Y').date(),
                                       cnpj=cnpj)
                else:
                    Fundo.objects.create(id=id, nome_fundo=row[1],
                                         data_inicial=datetime.strptime(row[2], '%d.%m.%Y').date(),
                                         data_final=datetime.strptime(row[3], '%d.%m.%Y').date(),
                                         cnpj=cnpj)

if __name__ == "__main__":
    importar(__name__)
