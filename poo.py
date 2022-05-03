from cgi import test
from dataclasses import dataclass
import csv
from itertools import combinations
from typing import List, Sequence
@dataclass
class Action:
    
    name : str
    price : float
    profit : float


@dataclass
class Portfolio:
    
    actions : Sequence[Action]
    price : float = 0.0
    profit : float = 0.0

    def compute_price(self):
        self.price = sum(action.price for action in self.actions)
        
    
    def compute_profit(self):
        self.profit = sum(action.profit for action in self.actions)


def load_from_csv(csv_path: str):
    with open(csv_path) as file:
        reader = csv.DictReader(file)
        return [Action(name=i["name"],price=float(i["price"]),profit=float(i["profit"])) for i in reader]

def result_one(best_combi):
    print(f"le financement est de {best_combi.price}")
    print(f"le profit est de {best_combi.profit}")
    print(f"{[value.name for value in best_combi.actions]}")


file = load_from_csv("action.csv")
Best_combinations = Portfolio(["actions"])
for repetitions in range(5,len(file) + 1):
    for cmb in combinations(file, repetitions):
        portefeuille = Portfolio(cmb)
        portefeuille.compute_price()
        if portefeuille.price > 500:
            continue
        portefeuille.compute_profit()
        Best_combinations = portefeuille
result_one(Best_combinations)

        