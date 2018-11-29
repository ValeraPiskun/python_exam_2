

"""
Користувач має пошту у домені @kpi.ua. Він купляє товари вказуючи назву та ціну.

Формати даних:

    пошта: перша літера англійської абетки у нижньому регістрі, далі стоїть крапка потім прізвище студента.

    назва товару : не більше 10 літер англійської абетки у нижньому регістрі

    ціна товару: додатне дійсне число з двома знаками після десяткової коми

"""


#    Сформувати структуру датасету для дного користувача.


dataset = {
    "hum01":{
                "qwerty123":{

                                "sell": 999.99
                },
                "qwer123":{

                                "sell": 999.99
                          }

            },
    "hum02":{
                "qwerty123":{

                                "sell": 999.99
                },
                "qwer123":{

                                "sell": 999.99
                          }

            }

}

names=list(dataset.keys())
for name in  names:
        print(name)
        phoneNames = list(dataset[name].keys())
        for phoneName in phoneNames:
            print(phoneName)
            phoneSell=dataset[name][phoneName]["sell"]
            print(phoneSell)
