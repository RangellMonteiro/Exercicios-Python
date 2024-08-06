# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética. 
#d) Em que posição está o time da Chapecoense.
times = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense", "Atlético", "Botafogo", "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória", "Coritiba", "Avaí", "Ponte preta", "Atlético-GO")
print("-=" * 15)
print("Lista de times do brasileirão {}".format(times))
print("-=" * 15)
print("Os cinco primeiros times são {}". format(times[0:5]))
print("-=" * 15)
print("Os quatro últimos times são {}".format(times[-4:]))
print("-=" * 15)
print("Times em ordém alfabética: {}".format(sorted(times)))
print("-=" * 15)
print("O Chapecoense está na {}ª posição".format(times.index("Chapecoense")+1))
