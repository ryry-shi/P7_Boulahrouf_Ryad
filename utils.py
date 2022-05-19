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