from flask import render_template, request


class MainRoutes:
    @staticmethod
    def configure_routes(app, templateFolder=""):
        @app.route("/")
        def home():
            url = f"{templateFolder}index.html"
            return render_template(url)

        @app.route("/register", methods=["GET", "POST"])
        def register():
            if request.method == "GET":
                url = f"{templateFolder}register.html"
                return render_template(url)
            elif request.method == "POST":
                return "posted"
