
from itertools import combinations
from time import time
from unittest import result
from portfolio import Portfolio
from utils import chooce_file, load_from_csv, result_one

def force_brute(path):


    start = time()
    data = load_from_csv(path)
    data_slice = data[:20]
    best_portfolio = None
    i=0
    for rep in range(1,len(data_slice) + 1):
        for cmb in combinations(data_slice, rep):
            portfolio = Portfolio(cmb)
            i+=1
            # if le prix est supérieur à 500 l'ignore passe a la boucle suivante
            if portfolio.price > 500:
                continue            
            if best_portfolio is None or (best_portfolio is not None and best_portfolio.profit < portfolio.profit) :
                best_portfolio = portfolio       
    stop = time()
    elapsed  = stop - start
    print(i)
    print(f"L'analyse a durée {elapsed:2f} seconde"), result_one(best_portfolio)

def main():
    force_brute("action.Csv")
    
if __name__ == "__main__" :
    main()