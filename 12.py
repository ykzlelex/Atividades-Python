semana = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]
somatemp = 0
temperatura = []
print("diga a temperatura de cada dia")
for temperatura in range(7):
    temperatura = float(input(f"{semana[temperatura]}: "))
    somatemp += temperatura
    media = temperatura /7
    maiortemp = max(temperatura)
    menortemp = min(temperatura)
    print(f"a temperatura max e {maiortemp}")
    print(f"a temperatura min e {menortemp}")
    print(f"a media das temperaturas da semana e {media:.2f}")