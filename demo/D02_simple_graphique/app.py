import dash
import dash_core_components as dcc
import dash_html_components as html

import os, sys
# ajoute à sys.path l'emplacement du script
sys.path.append(os.path.join(os.path.dirname(__file__), ""))

# Nécessaire 
if __name__ == '__main__':
    pathname_prefix='/'
else:
        # Récupère le chemin d'accès du rapport à partir du dossier 'reports/' et remplace les espaces par des underscores 
    pathname_prefix='/'+os.path.dirname(os.path.abspath(__file__)).split('reports'+os.sep,1)[1].replace(' ', '_')+'/'

external_stylesheets = ['static/css/bWLwgP.css']

app = dash.Dash(
    __name__,
    requests_pathname_prefix=pathname_prefix,
    external_stylesheets=external_stylesheets
)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ), 
    html.Br(),
    html.Br(),
    dcc.Markdown('''[Retour à la page d'accueil](/)''')
])

if __name__ == '__main__':
    app.run_server(debug=True)