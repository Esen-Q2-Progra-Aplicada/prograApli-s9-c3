from flask import Flask
from routes.main_routes import MainRoutes
from routes.pizza_order_routes import PizzaOrderRoutes
from routes.size_routes import SizeRoutes
from routes.flavor_routes import FlavorRoutes
from routes.complement_routes import ComplementRoutes
from routes.extra_routes import ExtraRoutes
import pytest


@pytest.fixture()
def create_webapp():
    app = Flask(__name__, template_folder="../templates")
    mainTemplateFolder = "/main/"
    adminTemplateFolder = "/admin/"
    pizzaTemplateFolder = "/pizzaProcess/"

    MainRoutes.configure_routes(app, templateFolder=mainTemplateFolder)
    PizzaOrderRoutes.configure_routes(app, templateFolder=pizzaTemplateFolder)
    SizeRoutes.configure_routes(app, templateFolder=adminTemplateFolder)
    FlavorRoutes.configure_routes(app, templateFolder=adminTemplateFolder)
    ComplementRoutes.configure_routes(app, templateFolder=adminTemplateFolder)
    ExtraRoutes.configure_routes(app, templateFolder=adminTemplateFolder)
    client = app.test_client()
    return client


def test_pizzapalace_home_exists(create_webapp):
    client = create_webapp
    response = client.get("/")
    print(response)
    assert response.status_code == 200


def test_pizzapalace_home_title(create_webapp):
    client = create_webapp
    response = client.get("/")
    assert response.status_code == 200
    if response.status_code == 200:
        assert b"<h1>pizza palace</h1>" in response.data


def test_pizzapalace_sizeCrud_main(create_webapp):
    client = create_webapp
    response = client.get("/sizeCRUD")
    assert response.status_code == 200


def test_pizzapalace_sizeCrud_title(create_webapp):
    client = create_webapp
    response = client.get("/sizeCRUD")
    assert response.status_code == 200
    if response.status_code == 200:
        assert b"<h1>size crud</h1>" in response.data


def test_pizzapalace_sizeCrud_form_new(create_webapp):
    client = create_webapp
    response = client.get("/sizeFORM")
    assert response.status_code == 200
    if response.status_code == 200:
        assert b"<h1>size new</h1>" in response.data


def test_pizzapalace_sizeCrud_form_update(create_webapp):
    client = create_webapp
    data = {"type": "update", "id": "3"}
    response = client.post("/sizeFORM", data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b"size" in response.data
    assert b'value="3"' in response.data
    assert b"24.00" in response.data


def test_pizzapalace_flavorCrud_main(create_webapp):
    client = create_webapp
    response = client.get("/flavorCRUD")
    assert response.status_code == 200


def test_pizzapalace_flavorCrud_title(create_webapp):
    client = create_webapp
    response = client.get("/flavorCRUD")
    assert response.status_code == 200
    if response.status_code == 200:
        assert b"<h1>flavor crud</h1>" in response.data


def test_pizzapalace_flavorCrud_form_new(create_webapp):
    client = create_webapp
    response = client.get("/flavorFORM")
    assert response.status_code == 200
    if response.status_code == 200:
        assert b"<h1>flavor new</h1>" in response.data


def test_pizzapalace_flavorCrud_form_update(create_webapp):
    client = create_webapp
    data = {"type": "update", "id": "4"}
    response = client.post("/flavorFORM", data=data, follow_redirects=True)
    assert response.status_code == 200
    assert b'value="4"' in response.data
    assert b"Mixed" in response.data
    assert b"mixed" in response.data
