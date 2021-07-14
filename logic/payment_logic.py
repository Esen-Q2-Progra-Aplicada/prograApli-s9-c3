from core.pyba_logic import PybaLogic


class PaymentLogic(PybaLogic):
    def __init__(self):
        super().__init__()
        self.table = "payment"

    def getSizeByValue(self, value):
        database = self.createDatabaseObj()
        sql = f"select * from size where value={value};"
        rowList = database.executeQuery(sql)
        return rowList

    def getFlavorByCode(self, code):
        database = self.createDatabaseObj()
        sql = f"select * from flavor where code='{code}';"
        rowList = database.executeQuery(sql)
        return rowList

    def getComplementByCode(self, code):
        database = self.createDatabaseObj()
        sql = f"select * from complement where code='{code}';"
        rowList = database.executeQuery(sql)
        return rowList

    def getExtraByCode(self, code):
        database = self.createDatabaseObj()
        sql = f"select * from extra where code='{code}';"
        rowList = database.executeQuery(sql)
        return rowList
