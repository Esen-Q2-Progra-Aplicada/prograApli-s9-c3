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
        if len(complementList) > 0:
            price = float(complementList[0]["price"])
        return price

    def checkExtraPrice(self, extraList):
        print(extraList)
        extraPriceList = []
        total = 0
        for element in extraList:
            elementDict = self.payLogic.getExtraByCode(element)[0]
            print(elementDict)
            extraPriceList.append(
                {
                    "item": elementDict["description"],
                    "price": float(elementDict["price"]),
                }
            )
            total += float(elementDict["price"])
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
        flavorDescription = self.payLogic.getFlavorByCode(flavor)[0]["description"]
        orderData.append(
            {
                "type": "flavor",
                "value": flavorDescription,
                "price": self.checkFlavorPrice(flavor),
            }
        )
        orderTotal += self.checkFlavorPrice(flavor)

        # complement
        complement = self.session.get("complement")
        complementList = self.payLogic.getComplementByCode(complement)
        complementDescription = complementList[0]["description"]
        orderData.append(
            {
                "type": "complement",
                "value": complementDescription,
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
