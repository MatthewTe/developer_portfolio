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
    return html.Div(["Dev Docs"])