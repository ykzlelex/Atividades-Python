from time import sleep
meses = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
temperaturas = []
somatemp = 0
print("media anual das temperaturas")
for mes in range(12):
    temperatura = float(input(f"{meses[mes]}: "))
    temperatura.append(temperatura)
    somatemp += temperatura
    media = somatemp / 12
    print(f"a media anual de temperatura foi: {media:.1f}")
    sleep(1)
    print("meses em que ultrapassou a media")
    for mes in range(12):
        if temperatura[mes] > media:
            print(f"{meses[mes]}: {temperaturas[mes]}")