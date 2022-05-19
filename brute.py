
from itertools import combinations
from time import time
from portfolio import Portfolio
from utils import load_from_csv

def force_brute(path):
    start = time()
    data = load_from_csv(path)
    best_portfolio = None
    for rep in range(1,len(data) + 1):
        for cmb in combinations(data, rep):
            portfolio = Portfolio(cmb)
            # if le prix est supérieur à 500 l'ignore passe a la boucle suivante
            if portfolio.price > 500:
                continue
            if best_portfolio is None or (best_portfolio is not None and best_portfolio.profit < portfolio.profit) :
                best_portfolio = portfolio
    stop = time()
    elapsed  = stop - start
    print(f"{elapsed:2f}s"), print(best_portfolio)

def main():
    data = "action.csv"
    force_brute(data)

if __name__ == "__main__" :
    main()