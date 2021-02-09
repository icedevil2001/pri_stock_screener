
from flask import Flask, json, render_template, url_for, flash, redirect, request, jsonify 
from flask_bootstrap import Bootstrap
import pandas as pd
from forms.myform import FundumentalForm
from pathlib import Path
from screener.fundumental import fundumental_anaysis

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


@app.route('/fundumental', methods=['POST', "GET"])
def fundumentals():
    form = FundumentalForm()
    if(request.method == 'POST') and form.validate_on_submit():
        tinkers = [x for x in form.tinker.data.split(',') if len(x)>1]
        print(tinkers)
        df = fundumental_anaysis(tinkers)
        df.to_csv('exported/fundumental.csv')
        print(Path(__file__))
        return render_template(
            'fundumental.html', 
            title='Fundumental Anaylsis',
            form=form,
            tables=[df.to_html(classes='table')],
            columns=df.columns.values
             )
    
    return render_template(
        'fundumental.html',
         title='Fundumental Anaylsis',
          form=form, tables=None, columns=None
          )

if __name__ == "__main__":
    app.run( debug=True)