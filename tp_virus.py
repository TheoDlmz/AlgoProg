def updateEtat(grille, i, j):
    
    if grille[i][j] > 0:
        return grille[i][j]
    
    voisins_infectes = 0
    if i>0 and grille[i-1][j] == 1:
        voisins_infectes += 1
    if i<len(grille)-1 and grille[i+1][j] == 1:
        voisins_infectes +=  1
    if j>0 and grille[i][j-1] == 1:
        voisins_infectes += 1
    if j<len(grille[0])-1 and grille[i][j+1] == 1:
        voisins_infectes += 1

    if voisins_infectes >= 2:
        return 1
    else:
        return 0

grille = [[1,0,0,1],[0,0,1,0],[0,0,0,0],[1,0,0,0]]


def updateGrille(grille):
    # On crée une nouvelle grille
    nouvelle_grille = []
    
    # On met à jour chaque cellule
    for i in range(len(grille)):
        grille_ligne = []
        for j in range(len(grille[0])):
            grille_ligne.append(updateEtat(grille, i, j))
        nouvelle_grille.append(grille_ligne)
    
    # On retourne la nouvelle grille
    return nouvelle_grille


def propagation(grille):
    n_jour = 0
    while True:
        nouvelle_grille = updateGrille(grille)
        if nouvelle_grille == grille:
            break
        grille = nouvelle_grille
        n_jour += 1
    return n_jour, grille

def nombreInfectes(grille):
    total = 0
    for ligne in range(len(grille)):
        for colonne in range(len(grille[0])):
            if grille[ligne][colonne] == 1:
                total += 1
    return total 



import random 

def createRandomGrille(n, p_virus, p_vaccin):
    grille = []
    for i in range(n):
        ligne = []
        for j in range(n):
            etat = 0
            x = random.random()
            if x < p_virus:
                etat = 1
            elif x < p_virus+p_vaccin:
                etat = 2
            ligne.append(etat)
        grille.append(ligne)
    return grille

import matplotlib.pyplot as plt
import matplotlib.animation as animation


grille_animated = grille
def animatePropagation(grille):

    fig = plt.figure() # initialise la figure
    im = plt.imshow(grille, animated=True) # initialise la grille

    def animate(i): 
        global grille_animated
        if i == 0:
            grille_animated = grille
        im.set_array(grille_animated)
        grille_animated = updateGrille(grille_animated)
        return im,
    
    ani = animation.FuncAnimation(fig, animate, frames=50,
                                interval=200, blit=True, repeat=True)


    plt.show()


animatePropagation(createRandomGrille(30,0.1,0.05))