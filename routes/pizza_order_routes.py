from flask import render_template, request, redirect, session
from logic.payment_logic import PaymentManager


class PizzaOrderRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/size", methods=["GET", "POST"])
        def size():
            if request.method == "GET":
                return render_template("size.html")
            elif request.method == "POST":
                selectedSize = request.form["size"]
                session["size"] = selectedSize
                return redirect("flavor")

        @app.route("/flavor", methods=["GET", "POST"])
        def flavor():
            if request.method == "GET":
                return render_template("flavor.html")
            elif request.method == "POST":
                selectedFlavor = request.form["flavor"]
                session["flavor"] = selectedFlavor
                return redirect("complement")

        @app.route("/complement", methods=["GET", "POST"])
        def complement():
            if request.method == "GET":
                return render_template("complement.html")
            elif request.method == "POST":
                selectedComplement = request.form["complement"]
                session["complement"] = selectedComplement
                return redirect("extra")

        @app.route("/extra", methods=["GET", "POST"])
        def extra():
            if request.method == "GET":
                return render_template("extra.html")
            elif request.method == "POST":
                extraString = request.form.getlist("extra")
                session["extra"] = extraString
                return redirect("payment")

        @app.route("/payment")
        def payment():
            payment = PaymentManager(session)
            orderPriceList = payment.processPriceList()
            print(orderPriceList)
            return render_template("payment.html", orderPriceList=orderPriceList)
