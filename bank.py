# bank_system.py

from dataclasses import dataclass, field
from typing import Dict
import itertools

@dataclass
class Account:
    accno: int
    name: str
    phone: str
    balance: float = field(default=0.0)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= amount
        return self.balance

    def __str__(self):
        return (f"Account No: {self.accno}\n"
                f"Name      : {self.name}\n"
                f"Phone     : {self.phone}\n"
                f"Balance   : {self.balance:.2f}")

class Bank:
    def __init__(self):
        self._accounts: Dict[int, Account] = {}
        self._id_iter = itertools.count(1001)  # generate account numbers starting from 1001

    def create_account(self, name: str, phone: str, initial_deposit: float = 0.0) -> Account:
        accno = next(self._id_iter)
        acct = Account(accno=accno, name=name, phone=phone, balance=0.0)
        if initial_deposit > 0:
            acct.deposit(initial_deposit)
        self._accounts[accno] = acct
        return acct

    def get_account(self, accno: int) -> Account:
        acct = self._accounts.get(accno)
        if not acct:
            raise KeyError(f"No account with number {accno}.")
        return acct

    def deposit(self, accno: int, amount: float):
        acct = self.get_account(accno)
        return acct.deposit(amount)

    def withdraw(self, accno: int, amount: float):
        acct = self.get_account(accno)
        return acct.withdraw(amount)

    def transfer(self, from_acc: int, to_acc: int, amount: float):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive.")
        src = self.get_account(from_acc)
        dst = self.get_account(to_acc)
        # perform atomic-like transfer: check first then update
        if src.balance < amount:
            raise ValueError("Insufficient funds in source account.")
        src.withdraw(amount)
        dst.deposit(amount)
        return (src.balance, dst.balance)

    def print_account(self, accno: int):
        acct = self.get_account(accno)
        print(acct)

    def list_accounts(self):
        for acct in self._accounts.values():
            print("-" * 30)
            print(acct)

# Simple demonstration
if __name__ == "__main__":
    bank = Bank()

    # Create two accounts
    a1 = bank.create_account(name="Alice", phone="9876543210", initial_deposit=1000.0)
    a2 = bank.create_account(name="Bob", phone="9123456780", initial_deposit=500.0)

    print("Created accounts:")
    bank.list_accounts()

    print("\nDeposit 200 to Alice's account")
    bank.deposit(a1.accno, 200.0)
    bank.print_account(a1.accno)

    print("\nWithdraw 100 from Bob's account")
    bank.withdraw(a2.accno, 100.0)
    bank.print_account(a2.accno)

    print("\nTransfer 300 from Alice to Bob")
    bank.transfer(a1.accno, a2.accno, 300.0)
    bank.print_account(a1.accno)
    bank.print_account(a2.accno)
