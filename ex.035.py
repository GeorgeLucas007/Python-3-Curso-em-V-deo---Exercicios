print("Analisador de Triângulos")

reta1 = float(input("Primeiro segmento de reta:"))
reta2 = float(input("Segundo segmento de reta:"))
reta3 = float(input("Terceiro segmento de reta:"))

#Principio matematico onde diz que um segmento de reta tem que ser menor que a soma dos outros dois. Assim para os três segmentos.
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("Os segmentos acima PODEM FORMAR um triângulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMAR um triângulo")


