from Motoboy import Motoboy
from Stores import Stores
import random


def main(motoboy):
    motoboy1 = Motoboy("1")
    motoboy2 = Motoboy("2")
    motoboy3 = Motoboy("3")
    motoboy4 = Motoboy("4")
    motoboy5 = Motoboy("5")

    orders(motoboy1, motoboy2, motoboy3, motoboy4, motoboy5)

    if motoboy is "":
        # return None
        motoboy1.getInformation()
        motoboy2.getInformation()
        motoboy3.getInformation()
        motoboy4.getInformation()
        motoboy5.getInformation()

    else:
        if motoboy1.getId() == motoboy:
            motoboy1.getInformation()
        elif motoboy2.getId() == motoboy:
            motoboy2.getInformation()
        elif motoboy3.getId() == motoboy:
            motoboy3.getInformation()
        elif motoboy4.getId() == motoboy:
            motoboy4.getInformation()
        elif motoboy5.getId() == motoboy:
            motoboy5.getInformation()
        else:
            print("Motoboy not found")


def orders(motoboy1, motoboy2=None, motoboy3=None, motoboy4=None, motoboy5=None):

    store1 = Stores("1")
    store2 = Stores("2")
    store3 = Stores("3")

    motoboys = [motoboy1, motoboy2, motoboy3, motoboy4, motoboy5]
    stores = [store1, store2, store3]

    while True:
        randomOrders = random.randrange(1, 5)
        store = random.choice(stores)
        motoboy = random.choice(motoboys)
        orders = store.getOrders()

        if randomOrders in orders:
            for a in motoboys:
                if motoboy is not None:
                    if str(motoboy.getStore()) == store.getId() and randomOrders in orders:
                        setOrders(motoboy, store, store.getId(), orders, randomOrders)
                    elif motoboy.getStore() == "all" and randomOrders in orders:
                        setOrders(motoboy, store, store.getId(), orders, randomOrders)

        if len(store1.getOrders()) == 0 and len(store2.getOrders()) == 0 and len(store3.getOrders()) == 0:
            break


def setOrders(motoboy, store, idStore, orders, randomOrders):
    motoboy.setOrders(idStore, orders[randomOrders])
    store.removeOrders(randomOrders)


if __name__ == "__main__":
    motoboy = input("Digite o id do motoboy para pesquisa: ")
    main(motoboy)
