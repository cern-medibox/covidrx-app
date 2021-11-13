import numpy as np
import pandas as pd
import dash
from dash.dependencies import Output, Input, State
from dash import dcc
from dash import html
import plotly
import plotly.graph_objs as go

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
app.title="Covid-19 RX"
server = app.server

app.layout = html.Div([
   html.Div(
        children=[
            #html.P(children="🩻", className="header-emoji"),
            #html.Img(src="assets/xray.png",style={'height':'300px','width':'10px','display': 'block','margin-left':'auto','margin-right': 'auto'}),
            html.H1(
                children="Covid-19 RX", className="header-title"
            ),
            html.P(
                children="Usa un modelo de aprendizaje profundo para evaluar una radiografía y encontrar neumonía causada por Covid-19",
                className="header-description"
            ),
        ],
        className="header",
    ),
    dcc.Upload(
        id='upload-image',
        children=html.Div([
            'Arrastre o ',
            html.A('seleccione un archivo')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-image-upload'),
])

def parse_contents(contents, filename, date):
    return html.Div([
        html.H5(filename),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the upload
        html.Img(src=contents),
        html.Hr(),
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])

@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

if __name__ == "__main__":
    app.run_server(debug=True)
