import math
import random

# Question 1.
def rac(n, epsilon):
    n_iter = 0
    x = random.randint(1,100000)
    while abs(x**2 - n) > epsilon:
        x = (x + n/x)/2
        n_iter += 1
    return x, n_iter

epsilon = 0.000001

# Regardons sur les 100 premiers entiers.
for n in range(1, 100):
    x,_ = rac(n, epsilon)
    print("Racine de {} = {}".format(n, x))
    vrai = math.sqrt(n)
    print("Valeur réelle: {}".format(vrai))


# Regardons pour n = 100000000
_, n_iter_milliard = rac(1000000000, epsilon)
print("Nombre d'itérations pour 1 milliard: {}".format(n_iter_milliard))

# Maintenant on veut calculer le nombre d'itérations moyennes et maximum pour 1 à 1 million.
total_iter = 0
max_iter = 0
for n in range(1,1000001):
    _, n_iter = rac(n, epsilon)
    total_iter += n_iter
    max_iter = max(max_iter, n_iter)

print("Nombre d'itérations pour 1 à 1 million: {}".format(total_iter))
print("Nombre d'itérations maximum: {}".format(max_iter))
print("Nombre d'itérations moyen: {}".format(total_iter/1000000))

# On trouve environ 10 itérations en moyenne (même avec des epsilon plus grand), et 20 pour le maximum.

# Pour la question 3 , voir le TD.