import csv
import os.path
from django.conf import settings
from fjfundo.mensalidades.models import Turma
from fjfundo.core.models import MyUser


def importar(self):
    filename = settings.CSV_ROOT + '/associado.csv'
    if os.path.isfile(filename):
        with open(filename, newline='') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if row[1] == 'ID_TURMA':
                    continue
                id = int(row[0])
                id_turma = int(row[1])
                turma = Turma.objects.filter(pk=id_turma)
                email=row[2]
                # if len(email) == 0:
                #     email = 'Email não informado.'

                if turma.exists():
                    associadoSearch = MyUser.objects.filter(pk=id)
                    if associadoSearch.exists():
                        associadoSearch.update(id=id, turma=turma[0], email=email, cpf=row[3], identidade=row[4],
                                               nome=row[5], logradouro=row[6], numero=row[7], complemento=row[8],
                                               bairro=row[9], cidade=row[10], uf=row[11], cep=row[12],
                                               fone1=row[13], fone2=row[14], nivel=int(row[15]))
                    else:
                        MyUser.objects.create(id=id, turma=turma[0], email=row[2], cpf=row[3], identidade=row[4],
                                               nome=row[5], logradouro=row[6], numero=row[7], complemento=row[8],
                                               bairro=row[9], cidade=row[10], uf=row[11], cep=row[12],
                                               fone1=row[13], fone2=row[14], nivel=int(row[15]))
