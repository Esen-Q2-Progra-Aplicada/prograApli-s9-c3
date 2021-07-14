from logic.payment_logic import PaymentLogic


class PaymentManager:
    def __init__(self, session):
        self.session = session
        self.payLogic = PaymentLogic()

    def processPriceList(self):
        orderData = self.createOrderData()
        return orderData

    def checkSizePrice(self, size):
        price = 0.0
        sizeList = self.payLogic.getSizeByValue(size)
        if len(sizeList) > 0:
            price = float(sizeList[0]["price"])
        return price

    def checkFlavorPrice(self, flavor):
        price = 0.0
        flavorList = self.payLogic.getFlavorByCode(flavor)
        if len(flavorList) > 0:
            price = float(flavorList[0]["price"])
        return price

    def checkComplementPrice(self, complement):
        price = 0.0
        complementList = self.payLogic.getComplementByCode(complement)
        if complement == "deditos":
            price = 4.0
        elif complement == "panajo":
            price = 5.0
        elif complement == "nuditos":
            price = 2.0
        if len(complementList) > 0:
            price = float(complementList[0]["price"])
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
        orderTotal = 0.0
        # size
        size = int(self.session.get("size"))
        orderData.append(
            {
                "type": "size",
                "value": size,
                "price": self.checkSizePrice(size),
            }
        )
        orderTotal += self.checkSizePrice(size)

        # flavor
        flavor = self.session.get("flavor")
        orderData.append(
            {
                "type": "flavor",
                "value": flavor,
                "price": self.checkFlavorPrice(flavor),
            }
        )
        orderTotal += self.checkFlavorPrice(flavor)

        # complement
        complement = self.session.get("complement")
        orderData.append(
            {
                "type": "complement",
                "value": complement,
                "price": self.checkComplementPrice(complement),
            }
        )
        orderTotal += self.checkComplementPrice(complement)

        # extra
        extraList = self.session.get("extra")
        extraPriceList, total = self.checkExtraPrice(extraList)
        orderData.append({"type": "extra", "value": extraPriceList, "total": total})
        orderTotal += total
        orderData.append({"type": "total order", "price": orderTotal})
        return orderData
