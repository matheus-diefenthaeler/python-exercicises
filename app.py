import random
from datetime import datetime, timedelta, date


def populate(number):
    date = datetime.now()
    apps = ["Mobile PF", "Mobile Personnalite", "Mobile Cartoes", "Mobile Varejo/Uniclass", "Mobile Empresa"]
    data = []
    for num in range(0, number):
        date = date - timedelta(minutes=5)
        idx = random.randrange(len(apps))
        randApp = apps[idx]
        clientes = random.randint(1000, 100000)
        impactados = random.randrange(0, clientes)
        alta = random.randrange(0, impactados)
        baixa = random.randrange(0, impactados)
        body = {
            "data": date.strftime("%Y/%m/%d"),
            "horaCodAplicacao": "{0}#{1}".format(date.strftime("%H:%M"), "Mobile PF"),
            "clientes": clientes,
            "impactados": impactados,
            "app": "Mobile PF",
            "altaPrioridade": alta,
            "baixaPrioridade": baixa,
            "dataHora": date.strftime("%Y/%m/%d" "%H:%M")
        }
        data.append(body)

    return data


results = populate(30)

app = ""
alta = 0
alta_pct = 0.0
baixa = 0
baixa_pct = 0.0
clientes = 0
impactados = 0
impactados_pct = 0.0
hora = ""
data = []

for impactado in range(0, len(results), 3):
    # if(results.__getitem__(impactado).get("horaCodAplicacao"))
    var = results.__getitem__(impactado).get("horaCodAplicacao").split("#")
    horaAtual = var[0]
    format = '%H:%M'
    hora = datetime.strptime(horaAtual, format)
    if (hora < (hora + timedelta(minutes=15))):
        print(hora)

# for result in results:
#     print(result.get("horaCodAplicacao").split("#"))

# def convert(time):
#     format = '"%H:%M"'
#     datetime_str = datetime.datetime.strptime(time, format)
#
#     return datetime_str
