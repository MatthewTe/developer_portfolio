# Importing dash methods:
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.CYBORG],
    external_scripts=["https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js"],
    suppress_callback_exceptions = True,
    requests_pathname_prefix="/",
    #requests_pathname_prefix="/dev/"
    #url_base_pathname="/dev/"
)
#server = app.server

app.layout = dbc.Container([
    dbc.Nav([
        dbc.NavItem(dbc.NavLink(page["name"], href=page["relative_path"], style={"color":"white"})) for page in dash.page_registry.values()
    ], style={"padding-top":"1rem"}),

    dash.page_container
])


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8000, debug=True)
