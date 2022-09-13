# Importing dash methods:
import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    path='/',
    name='About Me'
    )

def layout():

    # Querying all the pages in the project:
    pages = dash.page_registry.values()

    # Header 'Jumbotron' container:
    header_jumbotron = dbc.Container([
        html.H1("Matthew Teelucksingh", className="display-3", style={"padding-top":"1rem"}),
        html.H5("Software Developer & Policy Analyst with a focus on energy economics and climate change.", className="lead"),
        html.Hr(className="my-2"),
        html.P("Welcome to the entry point for my development environment. From here you can access my portfolio for employers, my articles and papers as well as my software projects and any other content relevant to my interests."),
        html.P("With an Education in environment and buisness from the University of Waterloo and work experience as a data engineer I focus on how data science and software development can be applied to solve issues relating to energy economics."),
        html.A(dbc.Button("Are you an employer? Click Here!", color="dark", outline=True, size="lg", className="me-1", id="employment-button"), href="#for-employers")
        ], 
        fluid=True, className="py-3"
    )

    # The main cards below the main jumbotron:
    dev_environment_component = html.A([
        dbc.Container([
            html.H4("Explore the Development Environment"),
            html.Hr(className="my-2"),
            dbc.CardImg(src="assets/landing_page/images/dev_env_img.jpg"),
            html.P("Explore the technical aspects of this development environment. How I use Nginx as a proxy for my mulitple dash applications, my CI/CD pipeline through github workflows to DigitalOcean droplets and why all my projects are structured this way",
            style={"padding-top":"0.5rem"})
        ])
    ], href=dash.page_registry["pages.developer_documenaton"]["relative_path"], style={"text-decoration":"none", "color":"inherit"})


    employment_history_component = dbc.Container([
        html.H3("Stats for Employers", className="display-3"),
        html.Hr(className="my-2"),

        html.H4("Education", style={"padding-top":"0.5rem", "padding-bottom":"1rem", "text-decoration":"underline"}),

        dbc.Row([
            dbc.Col([html.H5("Bachelor Of Environmental Studies")], width=4),
            dbc.Col(html.H5("Graduated May 2022"), width=4)
        ], justify="between"),
        html.P("University of Waterloo, Waterloo, ON", className="lead"),
        html.P("Honours Environment and Business; 4.0 Major GPA.", className="lead"),
        html.Hr(className="my-2"),

        dbc.Row([
            dbc.Col(html.H5("Stustainable Canadian Aviation Capstone"), width=4),
            dbc.Col(dbc.Button("Read Now", color="dark", outline=True), width=4, style={"padding-top":"0.5rem"})
        ], justify="between"),
        html.P("""My research project that evaluates the viability of reducing emissions in the Canadian aviation industry via performance standards that encourage the
            optimization of route and fleet selection. The conclusion was reached by analyzing the history, impacts and characteristics of global emissions 
            regulations on industries with similar economic characteristics to the aviation industry and extracting generalizable characteristics from successful 
            regulations. My final grade for the project was a 95 and the project can be read in full here."""
        ),
        html.Hr(className="my-2"),

        html.H5("Key Courses"),
        dbc.Accordion([
            dbc.AccordionItem([html.P("""The course focused on the pros and cons of different forms of environmental regulations and 
                some of the challenges associated with attempting to solve environmental and social issues through regulation. This 
                course culminated in a research paper proposing energy subsidy reform in the Trinidad and Tobago electivity market.""")], 
            title="Best Practices in Regulations"),

            dbc.AccordionItem([html.P("""Examines different research strategies and designs; define research questions; address ethical issues
                of involving human subjects in business research; identify primary and secondary data sources; and assess the 
                effectiveness of various ways of communicating research results.""")], 
            title="Research Design"),

            dbc.AccordionItem(html.P("""We researched and compared various environmental management systems to the standards set by ISO
                14001 and identified their pros and cons. There was a focus on Environmental Impact Assessments and how each standard 
                addressed the issues created by the tension between development interests and the public good."""),
            title="Environmental Management Systems"),

            dbc.AccordionItem(html.P("""Focused on conducting full cradle-to-grave life cycle assessments via EarthShift Global’s LCA
                software as well as the theoretical underpinnings of how LCA’s are conducted and how boundaries between stages of an 
                LCA are determined."""),
            title="Industrial Ecology: Life Cycle Assessment and Management in Business")

        ], start_collapsed=True),
        html.Hr(className="my-2"),


        
        html.H4("Work History", style={"padding-top":"1rem", "text-decoration":"underline"}),

        dbc.Row([
            dbc.Col(html.A(html.H5("Data Engineer - Coastal Dynamics"), href="http://coastaldynamics.com/"), width=4),
            dbc.Col(html.H5("June 2020 – July 2020"), width=4)
        ], justify="between", style={"padding-top":"1rem"}), 

        html.H5("Trinidad and Tobago"),
        html.P("""I was responsible for creating the APIs necessary for querying unstructured GIS and timeseries data generated 
            by DHI’s hydrodynamic models. Technologies used in creating these APIs include SMTP servers, DHI MIKE Software 
            Development Kit and python API frameworks (Django/Flask)."""),
        html.P("""Used the custom APIs to build Django data dashboards that displayed real-time and forecasted ocean current, wave 
            height and wind data for BHP offshore oil platforms (state the value of the project stuff)."""),
        html.Hr(className="my-2"),


        dbc.Row([
            dbc.Col(html.H5("Field Technician - Coastal Dynamics"), width=4),
            dbc.Col(html.H5("Aug 2018"), width=4)
        ], justify="between", style={"padding-top":"1rem"}), 

        html.H5("Trinidad and Tobago"),
        html.P("""Conducted an underwater survey of macro-organisms along coral reefs as part of an EIA for a Trinidad National 
            Petroleum development project."""),
        html.P("""Performed data collection about the impact of a natural gas development project on mangrove ecosystems."""),
        html.P("""Analysed and recorded sediment grain size via laser diffraction in a Mastersizer for benthic analysis."""),
        html.Hr(className="my-2"),

        dbc.Row([
            dbc.Col(html.A(html.H5("Research Assistant - Operation Wallacea"), href="https://www.opwall.com/in-field-experiences/"), width=4),
            dbc.Col(html.H5("Jun 2018 – July 2018"), width=4)
        ], justify="between", style={"padding-top":"1rem"}), 

        html.H5("Pantai Nirwana, Indonesia"),
        html.P("""Participated in underwater surveys that collected benthic & aquatic organism census data used for reef quality 
        surveys from the Hoga Island Marine Station."""),
        html.P("""Set up, deployed and reviewed data collected from Baited Remote Underwater Video systems that record and monitor Elasmobranches
        as part of the Global Finprint survey initiative that contributed to a peer reviewed article."""),
        html.Hr(className="my-2"),
    ], id="for-employers", style={"padding-top":"1.5rem"})
    
    writings_component = html.A([
        dbc.Container([
            html.H4("Read Everything that I've Written"),
            html.Hr(className="my-2"),
            dbc.CardImg(src="assets/landing_page/images/writing_area_thumbnail.png"),
            html.P("Here you can read all of my writings on particular topics and all of the papers I wrote in university that I am not extremely ashamed of. There are serious articles/essays on topics that interest me as well as more informal stuff about interests of mine. There is documentation about how I built the backend of this blog page in my projects section.",
            style={"padding-top":"0.5rem"})
        ])
    ], href="http://www.matthewteelucksingh.me:81/", style={"text-decoration":"none", "color":"inherit"})

    projects_component = html.A([
        dbc.Container([
            html.H4("Explore my Projects"),
            html.Hr(className="my-2"),
            dbc.CardImg(src="assets/landing_page/images/Pico_Wallpaper.jpg"),
            html.P("Explore my software and hardware projects that I've built over the years. Some of these projects were built at my previous jobs but many of them are projects relevant to my personal interests.",
            style={"padding-top":"0.5rem"})
        ])
    ], href=dash.page_registry["pages.projects"]["relative_path"], style={"text-decoration":"none", "color":"inherit"})

    return html.Div([
        header_jumbotron,

        dbc.Row([
            dbc.Col(dev_environment_component),
            dbc.Col(writings_component),
            dbc.Col(projects_component)
        ], className="mb-4", style={"padding-top":"2rem"}, align="top"),
        
        dbc.Fade([employment_history_component], id="employment_fade", is_in=False, appear=False),
        
    ])

# Callback that toggles the fade for the employment section based on the header button:
@callback(
    Output("employment_fade", "is_in"),
    Input("employment-button", "n_clicks"),
    #State("employment_fade", "is_in")
)
def toggle_employment_fade(n):
    if not n:
        return False
    else:
        return True