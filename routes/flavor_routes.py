from flask import render_template, request, redirect
from logic.flavor_logic import FlavorLogic


class FlavorRoutes:
    @staticmethod
    def configure_routes(app):
        @app.route("/flavorCRUD")
        def flavorCRUD():
            logic = FlavorLogic()
            flavorList = logic.getAll()
            return render_template("flavorCRUD.html", flavorList=flavorList)

        @app.route("/flavorFORM", methods=["GET", "POST"])
        def flavorFORM():
            if request.method == "GET":
                currentFlavor = None
                if request.args.get("type") == "update":
                    logic = FlavorLogic()
                    id = int(request.args.get("id"))
                    currentFlavor = logic.getRegisterById(id)
                    print(currentFlavor)
                return render_template("flavorFORM.html", flavorObj=currentFlavor)

            elif request.method == "POST":
                if request.args.get("type") == "update":
                    logic = FlavorLogic()
                    id = request.form["id"]
                    flavor = {
                        "description": request.form["description"],
                        "code": request.form["code"],
                        "price": request.form["price"],
                    }
                    rows = logic.update(id, flavor)
                elif request.args.get("type") == "new":
                    logic = FlavorLogic()
                    flavor = {
                        "description": request.form["description"],
                        "code": request.form["code"],
                        "price": request.form["price"],
                    }
                    rows = logic.insert(flavor)
                return redirect("flavorCRUD")

        @app.route("/flavorDELETE", methods=["POST"])
        def flavorDELETE():
            if request.method == "POST":
                logic = FlavorLogic()
                id = request.form["id"]
                rows = logic.delete(id)
                return redirect("flavorCRUD")
