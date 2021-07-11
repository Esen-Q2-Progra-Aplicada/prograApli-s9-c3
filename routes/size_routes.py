from flask import render_template, request
from logic.size_logic import SizeLogic


class SizeRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/sizeCRUD")
        def sizeCRUD():
            logic = SizeLogic()
            sizeList = logic.getAll()
            return render_template("sizeCRUD.html", sizeList=sizeList)

        @app.route("/sizeNEW", methods=["GET", "POST"])
        def sizeNEW():
            if request.method == "GET":
                if request.args.get("type") == "update":
                    pass
                return render_template("sizeNEW.html")
            elif request.method == "POST":
                if request.args.get("type") == "update":
                    pass
                elif request.args.get("type") == "new":
                    logic = SizeLogic()
                    size = {
                        "description": request.form["description"],
                        "value": request.form["value"],
                        "price": request.form["price"],
                    }
                    rows = logic.insert(size)
                return f"size new posted rowsAffected: {rows}"

        @app.route("/sizeUPDATE", methods=["GET", "POST"])
        def sizeUPDATE():
            if request.method == "GET":
                return render_template("sizeUPDATE.html")
            elif request.method == "POST":
                return "size update posted"

        @app.route("/sizeDELETE", methods=["GET", "POST"])
        def sizeDELETE():
            if request.method == "GET":
                return render_template("sizeDELETE.html")
            elif request.method == "POST":
                return "size delete posted"
