class House

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def finel_price(self, discount):
        finel_price = self._price * (100 - discount) / 100
        print(f"Finel price: {finel_price}
        return finel_price