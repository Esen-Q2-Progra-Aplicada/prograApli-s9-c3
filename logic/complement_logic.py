from core.pyba_logic import PybaLogic


class ComplementLogic(PybaLogic):
    def __init__(self):
        super().__init__()
        self.table = "complement"

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

    def insert(self, complement):
        database = self.createDatabaseObj()
        sql = (
            f"insert into {self.table} (id, description, code, price) "
            + f"values(0,'{complement['description']}', '{complement['code']}', {complement['price']});"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def update(self, id, complement):
        database = self.createDatabaseObj()
        sql = (
            f"UPDATE {self.table} "
            + f"SET description = '{complement['description']}', "
            + f"code = '{complement['code']}', price = {complement['price']}  "
            + f"WHERE id = {id};"
        )
        rows = database.executeNonQueryRows(sql)
        return rows

    def delete(self, id):
        database = self.createDatabaseObj()
        sql = f"delete from {self.table} where id={id}"
        rows = database.executeNonQueryRows(sql)
        return rows
