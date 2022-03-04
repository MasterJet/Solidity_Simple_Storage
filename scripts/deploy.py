"""
To deploy on rinkeby we need to tell infura project id
and a real account having etherium on rinkeby network
"""


from brownie import accounts, SimpleStorage, config, network


def deply_simple_storage():
    # use ganache accounts
    # account = accounts[0]
    # Medthod 1.
    # added in brwonie networks add
    # account = accounts.load("majid1")
    # print(account)
    # Method 2. (import os)
    #
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # print(os.getenv("WEB3_IFURA_PROJECT_ID"))
    # Method 3.
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)

    account = getAccount()

    print("Deployoing Simple Storage on Local")
    simple_storage = SimpleStorage.deploy({"from": account})

    stroedvalue = simple_storage.retrieve()
    print(stroedvalue)
    print("Updating Value")
    tx = simple_storage.store(101, {"from": account})
    tx.wait(1)
    UpdatedValue = simple_storage.retrieve()
    print(UpdatedValue)


def getAccount():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deply_simple_storage()
