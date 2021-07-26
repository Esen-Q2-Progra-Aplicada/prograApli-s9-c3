from core.pyba_logic import PybaLogic


class UserTypeLogic(PybaLogic):
    def __init__(self):
        super().__init__()
        self.table = "user_type"

    def getAll(self):
        database = self.createDatabaseObj()
        sql = f"select * from {self.table};"
        rowList = database.executeQuery(sql)
        return rowList

    def getRegisterById(self, id):
        database = self.createDatabaseObj()
        sql = f"select * from {self.table} where id={id};"
        result = database.executeQuery(sql)
        if len(result) != 0:
            return result[0]
        else:
            return []

    def getNextTableId(self):
        database = self.createDatabaseObj()
        idDict = database.getTableAutoIncrementId(self.table)
        return idDict["AUTO_INCREMENT"]

    def insert(self, userType):
        database = self.createDatabaseObj()
        sql = f"insert into {self.table} (id,name,description) values(0,'{userType['name']}','{userType['description']}');"
        rows = database.executeNonQueryRows(sql)
        return rows

    def update(self, id, userType):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE {self.table} "
            + f"SET name = '{userType['name']}', description = '{userType['description']}'  "
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def delete(self, id):
        database = self.createDatabaseObj()
        sql = f"delete from {self.table} where id={id}"
        rows = database.executeNonQueryRows(sql)
        return rows
