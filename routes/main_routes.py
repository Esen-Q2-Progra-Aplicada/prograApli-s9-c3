from flask import render_template


class MainRoutes:
    @staticmethod
    def configure_routes(app, templateFolder=""):
        @app.route("/")
        def home():
            url = f"{templateFolder}index.html"
            return render_template(url)
