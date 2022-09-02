# Importing dash methods:
import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

# Plotly methods:
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Data manipulation methods:
import pandas as pd

dash.register_page(
    __name__,
    path="/projects",
    name="Projects",
    title="Projects"
)

def layout():

    # Loading and creating plotly CDL Data dashboard:
    wave_df = pd.read_csv("assets/projects/data/Ruby_concat_wave.csv")
    
    # Creating a radialaxis range list for Mean Wave Directon Polar Chart :
    wave_radialaxis_range = [
        min(wave_df['Ruby Waves: Sign. Wave Height']),
        max(wave_df['Ruby Waves: Sign. Wave Height'])]
        
    # Creating radial axis range list for Wind Directon Polar Chart:
    wind_radialaxis_range = [
        min(wave_df['Ruby Waves: Wind speed']),
        max(wave_df['Ruby Waves: Wind speed'])]

        # <-------------------Creating and Formatting Plotly Figures------------------->

    # Creating Main wave subplot:
    ruby_subplots = make_subplots(
        rows=5, cols=2,
        specs = [[{'colspan': 2}, None],
                [{'colspan': 2}, None],
                [{'type':'polar', 'rowspan':2}, {'type':'polar', 'rowspan':2}],
                [None, None],
                [{'colspan': 2}, None]],
        vertical_spacing = 0.10,
        subplot_titles = ('Maximum and Significant Wave Height ',
            'Peak Wave Period', 'Mean Wind Direction', 'Wind Speed', 'Wind Speed'))

    # Adding Trace of Max and Sign Wave Height Timeseries:
    ruby_subplots.add_trace(
        go.Scatter(
            x= wave_df.index,
            y= wave_df['Ruby Waves: Max. Wave Height'],
            name= 'Max Wave Height (m/s)'),
        row = 1,
        col = 1)
    ruby_subplots.add_trace(
        go.Scatter(
            x= wave_df.index,
            y= wave_df['Ruby Waves: Sign. Wave Height'],
            name = 'Significant Wave Height (m/s)'),
        row = 1,
        col = 1)
    ruby_subplots.update_xaxes(title_text='Date', row=1, col=1)
    ruby_subplots.update_layout(yaxis=dict(range=[0, 7]))
    ruby_subplots.update_yaxes(title_text='Meters/Second (m/s)', row=1, col=1)

    # Creating and Formatting the Peak Wave Period Timeseries:
    ruby_subplots.add_trace(
        go.Scatter(
            x = wave_df.index,
            y = wave_df['Ruby Waves: Peak Wave Period'],
            name = 'Peak Wave Period (s)'),
        row = 2,
        col = 1)
    ruby_subplots.update_xaxes(title_text='Date', row=2, col=1)
    ruby_subplots.update_yaxes(title_text='Seconds (s)', row=2, col=1)
    
    # Creating and formatting the Mean Wave Directon and Wind Directon Polar Chart:
    ruby_subplots.add_trace(
        go.Scatterpolar(
            r = wave_df['Ruby Waves: Sign. Wave Height'],
            theta = wave_df['Ruby Waves: Mean Wave Direction'],
            mode = 'markers',
            name = 'Mean Wave Direction and Significant Wave Height ',
            marker_color = wave_df['Ruby Waves: Sign. Wave Height'],
            marker_size = 3),
        row = 3,
        col = 1)
    ruby_subplots.add_trace(
        go.Scatterpolar(
            r = wave_df['Ruby Waves: Wind speed'],
            theta = wave_df['Ruby Waves: Wind direction'],
            mode = 'markers',
            name = 'Wind Speed and Wind Direction',
            marker_color = wave_df['Ruby Waves: Wind speed'],
            marker_size = 3),
        row = 3,
        col = 2)

    # Creating and formatting the Wind Speed Timeseries:
    ruby_subplots.add_trace(
        go.Scatter(
            x = wave_df.index,
            y = wave_df['Ruby Waves: Wind speed'],
            name = 'Wind Speed (m/s)'),
        row = 5,
        col =1)
    ruby_subplots.update_xaxes(title_text='Date', row=4, col=1)
    ruby_subplots.update_yaxes(title_text='Meters/Second (m/s)', row=4, col=1)

    # Formatting the ruby_subplot:
    ruby_subplots.update_layout(
        title_text = 'Ruby Wave Forecast Data Dashboard',
        legend_orientation="h",
        height = 1300,
        # Formatting the Wave Directon polar plot:
        polar1 = dict(
            # Formatting radial axis:
            radialaxis = dict(range = wave_radialaxis_range),
            # Formatting angular axis:
            angularaxis = dict(rotation=90, direction='clockwise', visible=False)
            ),
        # Formatting the Wind Directon polar plot:
        polar2 = dict(
            # Formatting the raidal axis:
            radialaxis = dict(range = wind_radialaxis_range),
            # Formatting the angular axis:
            angularaxis = dict(rotation=90, direction='clockwise', visible=False)
        ),
        template = 'plotly_dark')

    # Containers for each project:
    cdl_dashboard = html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Row(html.H2("Ocean Current, Wind and Wave Dashboard and Data Pipeline")),
                dbc.Row([
                    html.P("I was required to build a front-end data dashboard that displayed time-series data of hourly ocean current, wave and wind height and direction and deploy it for the client. To do this I also had to write back-end data pipelines that aggregated, transformed and periodically uploaded data.", className="lead"), 
                    html.P("In addition to the front-end dashboard I also had to write the back-end pipelines that aggregate all of the company’s separate oceanographic data and make it available in an hourly format for my front-end dashboard to query."),
                    html.P("For the front-end dashboard itself I used the django web framework to create the site, did all the visualizations in plotly and deployed the front-end in a Heroku instance."),
                    html.P("For the back-end I created APIs that aggregated the relevant oceanographic data and ran them periodically on the necessary machines. The pipelines would then take all that data, serialize it and upload it to a gmail server where the front-end dashboard used my custom SMTP API to pull new data hourly from the gmail server."),
                    dbc.Button("See Example Dashboard", color="dark", outline=True, id="expand_example_button")
                    ])
            ]),
            dbc.Col(dbc.CardImg(src="assets/projects/images/Data_dashboard_thumbnail.png"))
        ], justify="between", style={"padding-top":"1.5rem", "padding-bottom":"1.5rem"}),
        
        dbc.Collapse(
            dcc.Graph(figure=ruby_subplots, id="CDL_dash_plot"), is_open=False, id="cdl_dashboard_collapse"
        ),
        html.Hr(className="my-2")
    ])

    zotero_dashboard = html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Row(html.H2("Plotly Zotero Dashboard")),
                dbc.Row([
                    html.P("This is a dashboard that, using the Zotero python API displays information and graphs about the amount and type of sources a user reads and saves to their Zotero account. The dashboard requires a user’s Zotero ID and API key and then queries the Zotero database using its python API. The dashboard is built in Dash and the visualization is done with Plotly.", className="lead"),
                    dbc.Button("Read More", color="dark", outline=True)
                    ])
            ]),
            dbc.Col(dbc.CardImg(src="assets/projects/images/zotero_thumbnail.png"))
        ], justify="between", style={"padding-top":"1.5rem", "padding-bottom":"1.5rem"}),
        
        dbc.Accordion([
            dbc.AccordionItem([html.H5("Test Accordion Content")], title="Dashboard Demonstration")
        ], start_collapsed=True), 
        html.Hr(className="my-2")
    ])

    sipri_dashboard = html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Row(html.H2("SIPRI Global Arms Sales Dashboard")),
                dbc.Row([
                    html.P("The SIPRI dashboard provides a visualization of interesting data collected by the Stockholm International Peace Research Institute. The SIPRI datasets were downloaded and saved as static files (for simplicity) in the Dash application and are visualized using Plotly.", className="lead"),
                    dbc.Button("Read More", color="dark", outline=True)
                    ])
            ]),
            dbc.Col(dbc.CardImg(src="assets/projects/images/SIPRI_thumbnail.jpg"))
        ], justify="between", style={"padding-top":"1.5rem", "padding-bottom":"1.5rem"}),
        
        dbc.Accordion([
            dbc.AccordionItem([html.H5("Test Accordion Content")], title="Dashboard Demonstration")
        ], start_collapsed=True), 
        html.Hr(className="my-2")
    ])

    pico_transceiver_project = html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Row(html.H2("Rasberry Pi Pico Transceiver Protocol")),
                dbc.Row([
                    html.P("Part of a much larger telemetry project that I am experimenting with as a means to transmit data between two endpoints using a Raspberry Pi Pico and an NRF24L01 wireless transceivers which communicate using the SPI protocol", className="lead"), 
                    html.P("As my first foray into micro-controllers and hardware programming the project has been slow going however thanks to the Pico’s use of MicroPython, allowing python3 to be run on micro-controllers progress is being made."),
                    dbc.Button("Read More", color="dark", outline=True)
                    ])
            ]),
            dbc.Col(dbc.CardImg(src="assets/projects/images/nRF24L01_thumbnail.png"))
        ], justify="between", style={"padding-top":"1.5rem", "padding-bottom":"1.5rem"}),
        
        dbc.Accordion([
            dbc.AccordionItem([html.H5("Test Accordion Content")], title="Dashboard Demonstration")
        ], start_collapsed=True), 
        html.Hr(className="my-2")
    ])

    drf_api = html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Row(html.H2("Django REST Framework API")),
                dbc.Row([
                    html.P("The Django REST API is an API service that stores, collects and serves data that I use to power my other projects.", className="lead"), 
                    html.P("The project has gone through many iterations over its lifetime. Currently it is deployed inside the development environment as an API service powered by the Django Rest Framework. The next version of the project will use OAuth with Github tokens but currently uses DRF Token authentication system. Data is provided on a rate limited bases using built in DRF tools. There is a very limited front-end component that consists of the API schema generated by (again) internal DRF tools and the Django Swagger UI extension that can be explored."),
                    html.P("Data is written to the database though the API via external scheduled processes making POST/PUT requests to the API. An example of this would be a pipeline that periodically extracts, serializes and POST reddit posts data to the API. This service is the core of many of my projects and a such new features and refactors and always occurring on a per-needed basis."),
                    dbc.Button("Explore the API", color="dark", outline=True)
                    ])
            ]),
            dbc.Col(dbc.CardImg(src="assets/projects/images/DRF_API_thumbnail.png"))
        ], justify="between", style={"padding-top":"1.5rem", "padding-bottom":"1.5rem"}),
        html.Hr(className="my-2")
    ])

    blog_CRUD_project = html.Div([
        dbc.Row([
            dbc.Col([
                dbc.Row(html.H2("Blog API with Full CRUD functionality and front-end")),
                dbc.Row([
                    html.P("The blog API is powered by my DRF API project. The API provides all the back-end CRUD functionality and the front-end that displays each blog post and allows me to create posts and make edits is built in Dash w/ Plotly. The front-end component of the blog project is a page in this main Dash application.", className="lead"), 
                    dbc.Button("Read More", color="dark", outline=True)
                    ])
            ]),
            dbc.Col(dbc.CardImg(src="assets/projects/images/Blog_API_thumbnail.png"))
        ], justify="between", style={"padding-top":"1.5rem", "padding-bottom":"1.5rem"}),
        
        dbc.Accordion([
            dbc.AccordionItem([html.H5("Test Accordion Content")], title="Dashboard Demonstration")
        ], start_collapsed=True), 
        html.Hr(className="my-2")
    ])

    return html.Div([
        dbc.Container([
            drf_api,
            blog_CRUD_project,
            cdl_dashboard,
            zotero_dashboard,
            sipri_dashboard,
            pico_transceiver_project
        ])
    ])

# CDL Dashboard Callbacks:
@callback(
    Output("cdl_dashboard_collapse", "is_open"),
    Input("expand_example_button", "n_clicks"),
    State("cdl_dashboard_collapse", "is_open")
)
def toggle_cdl_dashboard(n, is_open):
    if n:
        return not is_open
    return is_open