from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("template.html", string_input="Welcome to the Jedi Onboarding")

@app.route("/<name>/<lname>")
def jedi_name(name, lname):
    jedi_name = []
    jedi_name.append(name)
    jedi_name.append(lname)
    return render_template('template.html', string_input="Hello {}{}!".format(jedi_name[0][:3], jedi_name[1][:3]))

@app.route("/hello")
def hello():
    return render_template('template.html', string_input="please enter your name in uri")

if __name__ == '__main__':
    app.run()
