import initData


class Stores:
    def __init__(self, id):
        self._id = id
        self._orders = initData.data["store"][id]["orders"]

    def getId(self):
        return self._id

    def getOrders(self):
        return self._orders

    def removeOrders(self, order):
        self._orders.pop(order)