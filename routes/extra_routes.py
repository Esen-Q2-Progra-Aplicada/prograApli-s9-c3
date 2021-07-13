from flask import render_template, request, redirect
from logic.extra_logic import ExtraLogic


class ExtraRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/extraCRUD")
        def extraCRUD():
            logic = ExtraLogic()
            extraList = logic.getAll()
            return render_template("extraCRUD.html", extraList=extraList)

        @app.route("/extraFORM", methods=["GET", "POST"])
        def extraFORM():
            if request.method == "GET":
                currentExtra = None
                if request.args.get("type") == "update":
                    logic = ExtraLogic()
                    id = int(request.args.get("id"))
                    currentExtra = logic.getRegisterById(id)
                    print(currentExtra)
                return render_template("extraFORM.html", extraObj=currentExtra)

            elif request.method == "POST":
                if request.args.get("type") == "update":
                    logic = ExtraLogic()
                    id = request.form["id"]
                    extra = {
                        "description": request.form["description"],
                        "code": request.form["code"],
                        "price": request.form["price"],
                    }
                    rows = logic.update(id, extra)
                elif request.args.get("type") == "new":
                    logic = ExtraLogic()
                    extra = {
                        "description": request.form["description"],
                        "code": request.form["code"],
                        "price": request.form["price"],
                    }
                    rows = logic.insert(extra)
                return redirect("extraCRUD")

        @app.route("/extraDELETE", methods=["POST"])
        def extraDELETE():
            if request.method == "POST":
                logic = ExtraLogic()
                id = request.form["id"]
                rows = logic.delete(id)
                return redirect("extraCRUD")
