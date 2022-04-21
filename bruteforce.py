from argparse import Action
import csv
from itertools import combinations
from math import comb
from typing import Dict
from unicodedata import name
import pandas



def load_from_csv(csv_path: str):
    with open(csv_path) as file:
        reader = csv.DictReader(file)
        return [i for i in reader]

def sum_cmb_prices(cmb):
    return sum(int(action["price"]) for action in cmb)

def sum_cmb_profit(cmb):
    return sum(int(action["profit"]) for action in cmb)

def return_best_one(cmb, best_cmb, profit, best_profit, price, best_price):
    if profit < best_profit :
        return best_cmb, best_profit, best_price
    return cmb, profit, price

def print_result(best_cmb, best_profit, best_price):
    print(f"Profit realisee : {best_profit} euro")
    print(f"Investissement : {best_price} euro")
    print([action["name"] for action in best_cmb ])


def brute_force(csv_path: str, max_investment: int = 500):
    actions = load_from_csv(csv_path)
    best_profit = 0
    best_cmb = None
    best_price = 0
    for repetition in range(1,len(actions)+1):
        for cmb in combinations(actions,repetition):
            price = sum_cmb_prices(cmb)
            if price > max_investment:
                continue
            profit = sum_cmb_profit(cmb)
            best_cmb, best_profit, best_price = return_best_one(cmb, best_cmb, profit, best_profit, price, best_price) 
    print_result(best_cmb, best_profit, best_price)

            
if __name__ == "__main__":
    
    brute_force("action.csv")