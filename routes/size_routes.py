from flask import render_template, request, redirect
from logic.size_logic import SizeLogic


class SizeRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/sizeCRUD")
        def sizeCRUD():
            logic = SizeLogic()
            sizeList = logic.getAll()
            return render_template("sizeCRUD.html", sizeList=sizeList)

        @app.route("/sizeFORM", methods=["GET", "POST"])
        def sizeFORM():
            if request.method == "GET":
                currentSize = None
                if request.args.get("type") == "update":
                    logic = SizeLogic()
                    id = int(request.args.get("id"))
                    currentSize = logic.getRegisterById(id)
                    print(currentSize)
                return render_template("sizeFORM.html", sizeObj=currentSize)

            elif request.method == "POST":
                if request.args.get("type") == "update":
                    logic = SizeLogic()
                    id = request.form["id"]
                    size = {
                        "description": request.form["description"],
                        "value": request.form["value"],
                        "price": request.form["price"],
                    }
                    rows = logic.update(id, size)
                elif request.args.get("type") == "new":
                    logic = SizeLogic()
                    size = {
                        "description": request.form["description"],
                        "value": request.form["value"],
                        "price": request.form["price"],
                    }
                    rows = logic.insert(size)
                return redirect("sizeCRUD")

        @app.route("/sizeDELETE", methods=["POST"])
        def sizeDELETE():
            if request.method == "POST":
                logic = SizeLogic()
                id = request.form["id"]
                rows = logic.delete(id)
                return redirect("sizeCRUD")
