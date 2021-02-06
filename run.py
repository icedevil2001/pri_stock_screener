
from flask import Flask, render_template, url_for, flash, redirect
from flask_bootstrap import Bootstrap
import pandas as pd


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'n657h}zMU9?u}EafsdfadsafdsafdsaF6'
    # Bootstrap(app)
    return app


app =  create_app()

df = pd.DataFrame({'A': [0, 1, 2, 3, 4],
                   'B': [5, 6, 7, 8, 9],
                   'C': ['a', 'b', 'c--', 'd', 'e']})




## table html from pandas:
## https://stackoverflow.com/questions/52644035/how-to-show-a-pandas-dataframe-into-a-existing-flask-html-table 


@app.route('/home')
def home_function():
    return  render_template("home.html", title='Home page', tables=[df.to_html(classes='table')], columns=df.columns.values )

@app.route('/')
def index():
    return render_template('layout.html')


@app.route('/fundumental')
def fundumentals():
    
    return render_template('fundumental.html', title='Fundumental Anaylsis')

if __name__ == "__main__":
    app.run( debug=True)