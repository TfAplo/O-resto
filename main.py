from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = "dev"

@app.route('/')
def accueil():
    return render_template('accueil.html')

@app.route('/carte')
def carte():
    return render_template('carte.html')

if __name__ == "__main__":
	app.run(debug = True)
    