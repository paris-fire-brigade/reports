from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route("/")
def root():
	return "<b>[Flask]</b> Hello World! <br><br> \
    Test de récupération d'une constante déclarée dans <big><code>config.py</code></big> : <b><i>" + app.config['MA_CONSTANTE'] + "</i></b> <br><br><br>  \
    <a href='/'>Retour à la page d'accueil</a>"

if __name__ == "__main__":
	app.run()
