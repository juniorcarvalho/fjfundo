import csv
import os.path
from django.conf import settings
from datetime import datetime
from fjfundo.mensalidades.models import Fundo
from fjfundo.mensalidades.models import Turma


def importar(self):
    filename = settings.CSV_ROOT + '/turma.csv'
    if os.path.isfile(filename):
        with open(filename, newline='') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if row[1] == 'ID_FUNDO':
                    continue
                id = int(row[0])
                id_fundo = int(row[1])
                fundo = Fundo.objects.filter(pk=id_fundo)

                if fundo.exists():
                    turmaSearch = Turma.objects.filter(pk=id)
                    if turmaSearch.exists():
                        turmaSearch.update(id=id, fundo=fundo[0], nome_turma=row[2],
                                           dia_venc=row[3],
                                           data_formatura=datetime.strptime(row[4], '%d.%m.%Y').date(),
                                           valor_multa=2.00,
                                           valor_juros=1.00)
                    else:
                        Turma.objects.create(id=id, fundo=fundo[0], nome_turma=row[2],
                                           dia_venc=row[3],
                                           data_formatura=datetime.strptime(row[4], '%d.%m.%Y').date(),
                                           valor_multa=2.00,
                                           valor_juros=1.00)
