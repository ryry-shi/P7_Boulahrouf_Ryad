import csv
from action import Action

def load_from_csv(csv_path: str):
    with open(csv_path) as file:
        reader = csv.DictReader(file)
        return [Action(name=i["name"],price=float(i["price"]),profit=float(i["profit"])) for i in reader]

def result_one(best_combi):
    print(f"le financement est de {best_combi.price}")
    print(f"le profit est de {best_combi.profit}")
    print(f"les actions qui financée sont {[value.name for value in best_combi.actions]}")

def chooce_file():
    chooce = 0
    while True:
        # On entre une valeur tant que ca ne correspond pas a une valeur attendu
        chooce = int(input())
        if chooce == 0:
            action = load_from_csv("action.csv")
            return action
        if chooce == 1:
            action = load_from_csv("dataset1_Python+P7.csv")
            return action
        if chooce == 2:
            action = load_from_csv("dataset2_Python+P7.csv")
            return action

