class PaymentManager:
    def __init__(self, session):
        self.session = session

    def processPriceList(self):
        orderData = self.createOrderData()
        return orderData

    def checkSizePrice(self, size):
        price = 0.0
        if size == 1:
            price = 10.0
        elif size == 2:
            price = 17.0
        elif size == 3:
            price = 14.0
        return price

    def checkFlavorPrice(self, flavor):
        price = 0.0
        if flavor == "peperoni":
            price = 1.0
        elif flavor == "hawaiana":
            price = 2.0
        elif flavor == "meatlovers":
            price = 3.0
        elif flavor == "mixed":
            price = 5.0
        return price

    def checkComplementPrice(self, complement):
        price = 0.0
        if complement == "deditos":
            price = 4.0
        elif complement == "panajo":
            price = 5.0
        elif complement == "nuditos":
            price = 2.0
        return price

    def checkExtraPrice(self, extraList):
        print(extraList)
        extraPriceList = []
        total = 0
        if "postre" in extraList:
            extraPriceList.append({"item": "postre", "price": 4.0})
            total += 4.0
        if "wings" in extraList:
            extraPriceList.append({"item": "wings", "price": 5.0})
            total += 5.0
        if "bebida" in extraList:
            extraPriceList.append({"item": "bebida", "price": 2.0})
            total += 2.0
        return tuple((extraPriceList, total))

    def createOrderData(self):
        orderData = []
        # size
        size = int(self.session.get("size"))
        orderData.append(
            {
                "type": "size",
                "value": size,
                "price": self.checkSizePrice(size),
            }
        )
        # flavor
        flavor = self.session.get("flavor")
        orderData.append(
            {
                "type": "flavor",
                "value": flavor,
                "price": self.checkFlavorPrice(flavor),
            }
        )
        # complement
        complement = self.session.get("complement")
        orderData.append(
            {
                "type": "complement",
                "value": complement,
                "price": self.checkComplementPrice(complement),
            }
        )
        # extra
        extraList = self.session.get("extra")
        extraPriceList, total = self.checkExtraPrice(extraList)
        orderData.append({"type": "extra", "value": extraPriceList, "total": total})
        return orderData
