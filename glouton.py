
# On récupère nos action 
# On pioche au hasard
# On vérifie que le prix de l'action aditionné au prix des autres actions piocher ne dépassent pas les 500 euro
# Et répeter tant qu'il y a des action a piocher
from tracemalloc import start
from action import Action
from utils import load_from_csv
from random import randint
from time import time



def glouton(actions):
    portfolio = []
    prix = 0
    while actions:
        id_action = randint(0, len(actions) - 1)
        action = actions.pop(id_action)
        if prix + action.price <= 500 :
            prix += action.price
            portfolio.append(action)
    profit = sum(i.profit for i in portfolio)
    name = [i.name for i in portfolio]
    return  prix , profit, name

def main():
    start = time()
    best_profit = 0
    best_prix = 0
    best_name = []
    actions = load_from_csv("action.csv")
    max_iteraction = 1000000
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
