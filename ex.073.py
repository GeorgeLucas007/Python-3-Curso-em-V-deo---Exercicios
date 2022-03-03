times = ("Liverpool", "M. City", "M. United", "Chelsea", "Leicester City", "Tottenham", "Wolves",
         "Arsenal", "Sheffield", "Burnley", "Southampton", "Everton", "Newcastle", "Crystal Palace",
         "Brighton", "West Ham", "Aston Villa", "Bournemouth", "Watford", "Norwich")
print("-=" * 30)
print(f"Lista de times da Premier League: {times}")
print("-=" * 30)
print(f"O 5 primeiros colocados são: {times[0:5]}")
print("-=" * 30)
print(f"Os 4 últimos colocados são: {times[16:]}")
print("-=" * 30)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=" * 30)
print(f"O Arsenal está na {times.index('Arsenal')+1}ª posição")