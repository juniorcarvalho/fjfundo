import csv
import os.path
from datetime import datetime
from django.conf import settings
from fjfundo.core.models import MyUser
from fjfundo.mensalidades.models import Financeiro


def importar(self):
    filename = settings.CSV_ROOT = '/financeiro.csv'
    filename = '/home/junior/projetos/gloria/csv/financeiro.csv'
    if os.path.isfile(filename):
        with open(filename, newline='') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                if row[1] == 'USUARIO_ID':
                    continue

                id = int(row[0])
                usuario_id = int(row[1])

                associadoSearch = MyUser.objects.filter(pk=usuario_id)
                if not associadoSearch.exists():
                    continue

                valor = row[3]
                valor_extra = row[4]
                valor_acresdesc = row[5]
                valor_liquido = row[6]
                valor_jurdescbco = row[7]
                valor_despbco = row[8]

                valor = float(valor.replace(',', '.'))
                valor_extra = float(valor_extra.replace(',', '.'))
                valor_acresdesc = float(valor_acresdesc.replace(',', '.'))
                valor_liquido = float(valor_liquido.replace(',', '.'))
                valor_jurdescbco = float(valor_jurdescbco.replace(',', '.'))
                valor_despbco = float(valor_despbco.replace(',', '.'))

                valor = float("{0:.2f}".format(valor))
                valor_extra = float("{0:.2f}".format(valor_extra))
                valor_acresdesc = float("{0:.2f}".format(valor_acresdesc))
                valor_liquido = float("{0:.2f}".format(valor_liquido))
                valor_jurdescbco = float("{0:.2f}".format(valor_jurdescbco))
                valor_despbco = float("{0:.2f}".format(valor_despbco))

                data_vencimento = row[9]
                if len(data_vencimento) > 0:
                    data_vencimento = datetime.strptime(data_vencimento, '%d.%m.%Y').date()
                else:
                    data_vencimento = None

                data_pagamento = row[10]
                if len(data_pagamento) > 0:
                    data_pagamento = datetime.strptime(data_pagamento, '%d.%m.%Y').date()
                else:
                    data_pagamento = None

                data_proc = row[11]
                if len(data_proc) > 0:
                    data_proc = datetime.strptime(data_proc, '%d.%m.%Y').date()
                else:
                    data_proc = None

                financeiroSearch = Financeiro.objects.filter(pk=id)

                financeiro = Financeiro(id=id, usuario=associadoSearch[0], nrodoc=str(id), parcela=row[2],
                                        valor=valor, valor_extra=valor_extra, valor_acresdesc=valor_acresdesc,
                                        valor_liquido=valor_liquido, valor_jurdescbco=valor_jurdescbco,
                                        valor_despbco=valor_despbco,
                                        data_vencimento=data_vencimento,
                                        data_pagamento=data_pagamento,
                                        data_proc=data_proc,
                                        historico=row[12])

                if financeiroSearch.exists():
                    financeiroSearch.update(id=id, usuario=associadoSearch[0], nrodoc=str(id), parcela=row[2],
                                            valor=valor, valor_extra=valor_extra, valor_acresdesc=valor_acresdesc,
                                            valor_liquido=valor_liquido, valor_jurdescbco=valor_jurdescbco,
                                            valor_despbco=valor_despbco,
                                            data_vencimento=data_vencimento,
                                            data_pagamento=data_pagamento,
                                            data_proc=data_proc,
                                            historico=row[12])
                else:
                    financeiro.save()
    else:
        print(filename, 'nao localizado')