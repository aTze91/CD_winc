from flask import Flask, render_template, redirect, url_for
import markdown
__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)
markdown.Markdown()


@app.route("/")
def index():
    with open('README.md') as md_file:
        mkd_text = md_file
    return render_template("base.html", title='Index',mkd_text=mkd_text)

@app.route("/about")
def about():
    return render_template("base.html", title='About')

@app.route('/home')
def home():
    return redirect(url_for('index'))

@app.route('/unique/')
def unique():
    return render_template('base.html', title='Unique')
