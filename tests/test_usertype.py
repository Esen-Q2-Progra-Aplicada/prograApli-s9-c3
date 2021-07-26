import pytest
from core.pyba_database import PybaDatabase
from logic.user_type_logic import UserTypeLogic

skipInsertTest = False
""" @pytest.fixture
def setup():
    database = PybaDatabase()
    sql = "truncate table user;"
    success = database.executeNonQueryBool(sql)
    sql = "truncate table user_type;"
    success = database.executeNonQueryBool(sql) """


def test_usertype_table_getAll():
    logic = UserTypeLogic()
    userTypeList = logic.getAll()
    assert len(userTypeList) > 0


def test_usertype_table_getId_invalid():
    logic = UserTypeLogic()
    userTypeList = logic.getRegisterById(5)
    assert userTypeList == []


def test_usertype_table_getId_valid():
    logic = UserTypeLogic()
    userTypeList = logic.getRegisterById(1)
    assert len(userTypeList) > 0


@pytest.mark.skip(reason="one time test for increment")
def test_mysql_getautoinc_id():
    db = "pizzapalacedb"
    table = "user_type"
    database = PybaDatabase()
    sql = f'SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = "{db}" AND TABLE_NAME = "{table}"'
    idList = database.executeQuery(sql)
    assert len(idList) > 0
    assert idList[0]["AUTO_INCREMENT"] == 4


@pytest.mark.skipif(skipInsertTest, reason="one time test for insert")
def test_usertype_table_insert():
    logic = UserTypeLogic()
    nextId = logic.getNextTableId()
    print(nextId)
    print(type(nextId))
    userType = {
        "name": f"test{nextId}",
        "description": f"desc test{nextId}",
    }
    rows = logic.insert(userType)
    assert rows > 0
    if rows > 0:
        userType = logic.getRegisterById(nextId)
        assert userType["name"] == f"test{nextId}"
