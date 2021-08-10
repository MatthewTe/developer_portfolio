# Importing Flask Blueprinting Modules:
from flask import Blueprint, render_template
from flask import current_app as app

# Blueprink Configuration:
core_bp = Blueprint(
    "core_bp", __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/core"
)

@core_bp.route("/", methods=["GET"])
def portfolio_home():
    """
    View that renders the front end of the portfolio's homepage.
    """
    return render_template("home.html")


@core_bp.route("/velkozz_project", methods=["GET"])
def velkozz_project():
    """
    The View that renders the template for the Velkozz Django Rest Framework Project. 
    """
    return render_template("velkozz_project.html")

@core_bp.route("/ml_paper_implementations", methods=["GET"])
def ml_implementations():
    """
    The View that renders the front-end for all Machine Learning research paper implementations.
    """
    return render_template("ml_papers.html")