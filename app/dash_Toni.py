import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from sqlalchemy import create_engine

# Connexió a l
sqlEngine = create_engine("mysql+pymysql://" + 'sistemesbd' + ":" + 'bigdata2223' + "@" + '192.168.193.133:3306' + "/" + 'alumnes')
dbConnection = sqlEngine.connect()
df = pd.read_sql('SELECT * FROM Toni', dbConnection)

    
    
# Initialize the app
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.config.suppress_callback_exceptions = True

navbar = dbc.Navbar(
    [dbc.NavbarBrand("WEB SCRAPPING NATURAL GAS FEATURES", className="ms-2",style={'textAlign': 'center','height':'80px'})
    ],
    color="info",
    dark=True
)


# fig = px.bar(df, x=df.index, y=['Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre'], title='Datos numéricos para los meses de marzo a septiembre')
# Crea una lista de líneas, una para cada columna del DataFrame
lineas = []
for col in df.columns:
    linea = go.Scatter(
        x=df.index,
        y=df[col],
        mode='lines',
        name=col
    )
    lineas.append(linea)

# Crea una figura con todas las líneas

fig = go.Figure(data=lineas)



app.layout =  html.Div(children=[navbar,
    dbc.Row([
        dcc.Graph(
            id='ventas-mensuales',
            figure=fig
        )
        ]),
    dbc.Row([
        dbc.Col(html.Div([dbc.Alert("Dissenyat per Toni Amer", color="dark")]),width=12)
    ])
    ])

if __name__ == '__main__':
    app.run_server(debug=True)