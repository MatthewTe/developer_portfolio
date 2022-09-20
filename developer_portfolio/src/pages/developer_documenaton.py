# Importing dash methods:
import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path="/docs",
    name="Documentation",
    title="Documentation"
)

def layout():
    return html.Div([
        html.H3("Welcome to my Developer Environment"),
        html.P(["The dev environment is where I set up and deploy all of my projects that I think are semi-finished and worthy of inclusion into my software portfolio. If you are interested in reading more about an individual project, check out my project ", html.A("section.", href=dash.page_registry["pages.projects"]["relative_path"])]),
        html.P("It should be noted that I also use several of the currently deployed portfolio projects in my day to day (for example the flask blog) and as such new features and bug fixes are continuously being added as needed to improve usability."),
        html.P(["What I call the developer environment is an internal docker bridge network containing all my projects as containerized applications. This network is hosted on a DigitalOcean droplet with the entry-point being an nginx server that serves as a reverse proxy to all my apps. As I struggle through the deployment and maintenance of this environment I try to make weekly posts about the issues I am working through and the features I am working on. If there isn’t a blog post, my progress on the environment can be tracked through its .", html.A("GitHub project",href="https://github.com/users/MatthewTe/projects/6/views/1")]),
    ])