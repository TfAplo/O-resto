from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__, template_folder='templates')
app.secret_key = "dev"

@app.route('/')
def accueil():
    return render_template('accueil.html')

if __name__ == "__main__":
	app.run(debug = True)
