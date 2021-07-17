from flask import render_template, request, redirect
from logic.complement_logic import ComplementLogic


class ComplementRoutes:
    @staticmethod
    def configure_routes(app, templateFolder=""):
        @app.route("/complementCRUD")
        def complementCRUD():
            logic = ComplementLogic()
            complementList = logic.getAll()
            url = f"{templateFolder}complementCRUD.html"
            return render_template(url, complementList=complementList)

        @app.route("/complementFORM", methods=["GET", "POST"])
        def complementFORM():
            if request.method == "GET":
                currentComplement = None
                url = f"{templateFolder}complementFORM.html"
                if request.args.get("type") == "update":
                    logic = ComplementLogic()
                    id = int(request.args.get("id"))
                    currentComplement = logic.getRegisterById(id)
                return render_template(url, complementObj=currentComplement)

            elif request.method == "POST":
                if request.args.get("type") == "update":
                    logic = ComplementLogic()
                    id = request.form["id"]
                    complement = {
                        "description": request.form["description"],
                        "code": request.form["code"],
                        "price": request.form["price"],
                    }
                    rows = logic.update(id, complement)
                elif request.args.get("type") == "new":
                    logic = ComplementLogic()
                    complement = {
                        "description": request.form["description"],
                        "code": request.form["code"],
                        "price": request.form["price"],
                    }
                    rows = logic.insert(complement)
                return redirect("complementCRUD")

        @app.route("/complementDELETE", methods=["POST"])
        def complementDELETE():
            if request.method == "POST":
                logic = ComplementLogic()
                id = request.form["id"]
                rows = logic.delete(id)
                return redirect("complementCRUD")
