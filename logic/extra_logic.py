from core.pyba_logic import PybaLogic


class ExtraLogic(PybaLogic):
    def __init__(self):
        super().__init__()
        self.table = "extra"

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

    def insert(self, extra):
        database = self.createDatabaseObj()
        sql = (
            f"insert into {self.table} (id, description, code, price) "
            + f"values(0,'{extra['description']}', '{extra['code']}', {extra['price']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def update(self, id, extra):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE {self.table} "
            + f"SET description = '{extra['description']}', "
            + f"code = '{extra['code']}', price = '{extra['price']}'  "
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def delete(self, id):
        database = self.createDatabaseObj()
        sql = f"delete from {self.table} where id={id}"
        rows = database.executeNonQueryRows(sql)
        return rows
