# On récupère nos action 
# On pioche au hasard
# On vérifie que le prix de l'action aditionné au prix des autres actions piocher ne dépassent pas les 500 euro
# Et répeter tant qu'il y a des action a piocher
from utils import chooce_file
from random import randint
from time import time

def glouton(actions):
    #On déclare une liste vide
    portfolio = []
    prix = 0
    # Tant que actions a un paramètre la boucle tourne
    while actions:
        # prend au hasard les valeur action
        id_action = randint(0, len(actions) - 1)
        # retire la dernière valeur
        action = actions.pop(id_action)
        # if le prix est inférieur a 500 en ajoute action a la liste portfolio
        if prix + action.price <= 500 :
            prix += action.price
            portfolio.append(action)
    # On calcule la somme des profit dans une liste d'intention dans une variable
    profit = sum(i.profit for i in portfolio)
    # la meme chose pour le name
    name = [i.name for i in portfolio]
    return  prix , profit, name

def main():
    start = time()
    best_profit = 0
    best_prix = 0
    best_name = []
    # Fonction qui choisis un fichier
    actions = chooce_file()
    max_iteraction = 100000
    # on choisis une valeur max et on fais une boucle en itérant dessus
    for _ in range(max_iteraction): 
        prix , profit , name = glouton(actions)
        if best_profit < profit:
            best_profit = profit
            best_prix = prix
            best_name = name
    stop = time()
    elapsed  = stop - start
    print(f"{elapsed:2f} s"), print(best_prix, best_profit, best_name)

if __name__ == "__main__" :
    main()
