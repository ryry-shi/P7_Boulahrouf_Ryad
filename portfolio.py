
from dataclasses import dataclass
from random import shuffle
from typing import Sequence
from action import Action

@dataclass(init=False)
class Portfolio:
    
    actions : Sequence[Action]
    __price : float = 0.0
    __profit : float = None

    def __init__(self, actions):
        self.actions = actions
        self.__compute_price()

    
    @property
    def price(self):
        return self.__price
        
    def __compute_price(self):
        self.__price = sum(action.price for action in self.actions)
        
    @property
    def profit(self):
        if self.__profit is None:
             self.__compute_profit()
        return self.__profit


    def __compute_profit(self):
        self.__profit = sum(action.profit for action in self.actions)
