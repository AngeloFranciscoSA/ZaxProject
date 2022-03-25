import initData


class Motoboy:

    def __init__(self, id):
        self._id = id
        self._commission = initData.data['motoboy'][id]['commission']
        self._store = initData.data['motoboy'][id]['store']
        self._orders = []
        self._salary = 0

    def calculateSalary(self):
        self._salary += len(self._orders) * self._commission
        return self._salary

    def getId(self):
        return self._id

    def getInformation(self):
        print('Motoboy ID: {}'.format(self._id))
        print('Store: {}'.format(self._store))
        print('Commission: {}'.format(self._commission))
        print('Orders: {}'.format(self._orders))
        print('Salary: {}\n'.format(self.calculateSalary()))

    def getCommission(self):
        return self._commission

    def getStore(self):
        return self._store

    def getOrders(self):
        return self._orders

    def setOrders(self, store, orders):
        order = {
            'store': store,
            'value': orders['value'],
            'commission': orders['commission']
        }
        self._orders.append(order)
