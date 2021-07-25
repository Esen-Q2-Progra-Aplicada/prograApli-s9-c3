from flask import Flask
from routes.main_routes import MainRoutes
from routes.pizza_order_routes import PizzaOrderRoutes
from routes.size_routes import SizeRoutes
from routes.flavor_routes import FlavorRoutes
from routes.complement_routes import ComplementRoutes
from routes.extra_routes import ExtraRoutes


def test_pizzapalace_home_exists():
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
    response = client.get("/")
    print(response)
    assert response.status_code == 200
