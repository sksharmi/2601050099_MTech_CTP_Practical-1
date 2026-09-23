from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def withdraw(self, amount: float) -> None: pass

class Savings(Bank):
    def withdraw(self, amount: float) -> None:
        print("Withdrawn:", amount)

a: Bank = Savings()
a.withdraw(500)