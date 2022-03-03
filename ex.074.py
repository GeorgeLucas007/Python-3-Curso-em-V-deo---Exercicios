from random import sample
nums = tuple(sample(range(10), 5))#Outra forma de escrever uma tupla
print(nums)
print(f'O maior valor é {max(nums)} e o menor é {min(nums)}.')#Metodo max e min para não fazer tanto if.

