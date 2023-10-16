# TP 2 Algo prog 3

# Exercice 1
import math 

def convert(t_milliseconds):
    t_seconds = t_milliseconds // 1000
    
    (t_min, s) = divmod(t_seconds, 60)
    (t_h, m) = divmod(t_min, 60)
    (t_days, h) = divmod(t_h, 24)
    (t_months, days) = divmod(t_days, 30)
    (years, months) = divmod(t_months, 12)
    return [years, months, days, h, m, s]


def printTime(t_milliseconds):
    t = convert(t_milliseconds)
    print(str(t[0])+ " années," + str(t[1]) + " mois," + str(t[2]) + 
          " jours," + str(t[3]) + " heures," + str(t[4]) + " minutes," + str(t[5]) + " secondes")
    

"""
Une instruction simple prend 1 milliseconde. 
Donc on peut estimer le temps d'exécution d'un programme en comptant le nombre d'instructions simples.
Voici quelques exemples avec un programme qui a pour paramètre n = 1 million.
Alors qu'un programme en log(n) s'effectue en moins d'une seconde, un programme linéaire en O(n) met 16 minutes
et un programme quadratique en O(n^2) met 32 années.
"""
n = 1000000

printTime(math.log(n))
printTime(n)
printTime(n*math.log(n))
printTime(n**2)
printTime(n**3)
# printTime(2**n)


### PARTIE 2 
import random 
def generate_tab(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(0, 1000))
    return tab


"""
Version en 1 ligne:
def generate_tab(n):
    return [random.randint(0, n) for i in range(1000)]
"""

# Tri par insertion

def insertion_sort(tab):
    for i in range(1, len(tab)):
        j = i
        while j > 0 and tab[j-1] > tab[j]: # Si il est plus grand, on swap avec le précédent.
            tab[j-1], tab[j] = tab[j], tab[j-1]
            j -= 1
    return tab


# Tri bulle

def bubble_sort(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-1):
            if tab[j] > tab[j+1]: # Si il est plus grand, on swap avec le suivant.
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab


# Tri fusion

def merge(tab1, tab2):
    tab = []
    i = 0
    j = 0
    while i < len(tab1) and j < len(tab2):
        if tab1[i] < tab2[j]:
            tab.append(tab1[i])
            i += 1
        else:
            tab.append(tab2[j])
            j += 1
    if i < len(tab1):
        tab += tab1[i:]
    if j < len(tab2):
        tab += tab2[j:]
    return tab

def merge_sort(tab):
    if len(tab) <= 1:
        return tab
    else:
        mid = len(tab) // 2
        left = merge_sort(tab[:mid])
        right = merge_sort(tab[mid:])
        return merge(left, right)
    

# Tri rapide
"""
Version longue:

def partition(tab, pivot):
    left = []
    right = []
    equal = []
    for x in tab:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)

    return left, equal, right

def quick_sort(tab):
    if len(tab) <= 1:
        return tab
    else:
        pivot = tab[0]
        left, equal, right = partition(tab, pivot)
        return quick_sort(left) + equal + quick_sort(right)
"""

def quick_sort(tab):
    if len(tab) <= 1:
        return tab
    else:
        pivot = tab[0]
        left = [x for x in tab[1:] if x < pivot]
        right = [x for x in tab[1:] if x >= pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)



# Comparaison du temps d'exécution

import time 

def compare_time():
    tab = generate_tab(1000)
    list_tris = [insertion_sort, bubble_sort, merge_sort]#, quick_sort]
    list_names = ["insertion_sort", "bubble_sort", "merge_sort"]#, "quick_sort"]
    for i in range(len(list_tris)):
        start = time.time()
        list_tris[i](tab)
        end = time.time()
        print(list_names[i])
        printTime((end-start))


compare_time()


# J'ai mis en parenthese le quick sort car il y a trop de réccurence imbriquées.
# Complexité du tri par insertion : O(n^2) (double boucle for)
# Complexité du tri bulle : O(n^2) (double boucle for)
# Complexité du tri fusion : O(n log(n)) (on divise par 2 à chaque fois la taille de la liste)
# Complexité du tri rapide : en moyenne O(n log(n)) (on divise par 2 à chaque fois la taille de la liste) 
# mais dans le pire des cas O(n^2) (si le pivot est toujours le plus petit ou le plus grand)