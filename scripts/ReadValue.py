"""
Brownie keep data of test nets
so we can access last deployed contracts 
SimpleStorage[-1] mean latest
"""
from brownie import SimpleStorage


def readCurrentValue():
    simple_storage = SimpleStorage[-1]
    CurrentValue = simple_storage.retrieve()
    print("Current Stored Value is")
    print(CurrentValue)


def main():
    readCurrentValue()
