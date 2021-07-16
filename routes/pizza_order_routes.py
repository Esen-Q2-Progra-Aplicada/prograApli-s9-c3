from flask import render_template, request, redirect, session
from logic.payment_manager import PaymentManager
from logic.size_logic import SizeLogic
from logic.flavor_logic import FlavorLogic
from logic.complement_logic import ComplementLogic
from logic.extra_logic import ExtraLogic


class PizzaOrderRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/size", methods=["GET", "POST"])
        def size():
            if request.method == "GET":
                logic = SizeLogic()
                sizeList = logic.getAll()
                print(sizeList)
                return render_template("size.html", sizeList=sizeList)
            elif request.method == "POST":
                selectedSize = request.form["size"]
                session["size"] = selectedSize
                return redirect("flavor")

        @app.route("/flavor", methods=["GET", "POST"])
        def flavor():
            if request.method == "GET":
                logic = FlavorLogic()
                flavorList = logic.getAll()
                print(flavorList)
                return render_template("flavor.html", flavorList=flavorList)
            elif request.method == "POST":
                selectedFlavor = request.form["flavor"]
                session["flavor"] = selectedFlavor
                return redirect("complement")

        @app.route("/complement", methods=["GET", "POST"])
        def complement():
            if request.method == "GET":
                logic = ComplementLogic()
                complementList = logic.getAll()
                return render_template("complement.html", complementList=complementList)
            elif request.method == "POST":
                selectedComplement = request.form["complement"]
                session["complement"] = selectedComplement
                return redirect("extra")

        @app.route("/extra", methods=["GET", "POST"])
        def extra():
            if request.method == "GET":
                logic = ExtraLogic()
                extraList = logic.getAll()
                return render_template("extra.html", extraList=extraList)
            elif request.method == "POST":
                extraString = request.form.getlist("extra")
                session["extra"] = extraString
                return redirect("payment")

        @app.route("/payment")
        def payment():
            payment = PaymentManager(session)
            orderPriceList = payment.processPriceList()
            return render_template("payment.html", orderPriceList=orderPriceList)
