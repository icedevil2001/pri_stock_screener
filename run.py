
from flask import Flask, json, render_template, url_for, flash, redirect, request, jsonify, send_from_directory
from flask.helpers import send_file 
from flask_bootstrap import Bootstrap
import pandas as pd
from forms.myform import FundumentalForm
from pathlib import Path
from Screener.fundumental import fundumental_anaysis
# from Screener.util import df_download 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'n657h}zMU9?u}EafsdfadsafdsafdsaF6'
    app.config['UPLOAD_DIRECTORY'] = str(Path('exported').resolve())
    # Bootstrap(app)
    return app

exported_dir =  Path('exported')

if not exported_dir.exists():
    exported_dir.mkdir(parents=True)

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
        
        tinkers = [x.strip().upper() for x in form.tinker.data.split(',') if len(x)>1]

        try: 
        
            df = fundumental_anaysis(tinkers)
            df.to_csv('exported/fundumental.csv')
            tables=[df.to_html(classes='table')]
            return render_template( 
                'fundumental.html',
            title='Fundumental Anaylsis',
            form=form,
            tables=tables )
        except Exception as e:

            flash(f'Error {e}|| -- One of the stock was not found ', 'danger')
            return redirect( url_for( "fundumentals" ) )

    return render_template(
        'fundumental.html',
         title='Fundumental Anaylsis',
        form=form,
    )


@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def downloadFile(filename):
    print('***',filename)
    return send_from_directory(directory=exported_dir, filename=filename,  as_attachment=True, )



if __name__ == "__main__":
    app.run( debug=True)