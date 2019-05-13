"""Train a model to classify Foos and Bars.

Usage::

    >>> import klassify
    >>> data = [("green", "foo"), ("orange", "bar")]
    >>> classifier = klassify.train(data)

:param train_data: A list of tuples of the form ``(color, label)``.
:rtype: A :class:`Classifier <Classifier>`
"""
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
    pathname_prefix='/'+os.path.dirname(os.path.abspath(__file__)).split('reports/',1)[1]+'/'.replace(' ', '_')

external_stylesheets = ['common/static/css/bootstrap.min.css']

app = dash.Dash(
    __name__,
    requests_pathname_prefix=pathname_prefix,
    external_stylesheets=external_stylesheets
)

app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
	html.Div([
		html.B('[Dash] '),
		html.Span('Hello World!')
	]),
	html.Br(), 
	html.Div('Test de récupération de l\'emplacement physique du rapport : ' + os.path.dirname(os.path.abspath(__file__)).split('reports/',1)[1]),
	html.Br(), 
  html.Div('Test d\'insertion d\'une image :'),
  html.Img(src='static/img/dash.svg'),
  html.Br(),
  html.Br(),
  dcc.Markdown('''
  [Retour à la page d'accueil](/)
  	''')
])

# Appelé lors d'un lancement isolé (en dehors du server de rapports) 
if __name__ == '__main__':
    app.run_server(debug=True)