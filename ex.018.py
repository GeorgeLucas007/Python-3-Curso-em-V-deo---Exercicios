import math

an = float(input("Digite o angulo:"))

seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))

print("Seno é:{:.2f} \nCosseno é:{:.2f} \nTangente é:{:.2f}".format(seno, cos, tg))