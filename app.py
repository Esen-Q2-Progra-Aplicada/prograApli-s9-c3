from flask import Flask
from routes.main_routes import MainRoutes
from routes.pizza_order_routes import PizzaOrderRoutes
from routes.size_routes import SizeRoutes


app = Flask(__name__)
app.secret_key = "Ba1p2a3s4s5w6o7r8d9++"
MainRoutes.configure_routes(app)
PizzaOrderRoutes.configure_routes(app)
SizeRoutes.configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
