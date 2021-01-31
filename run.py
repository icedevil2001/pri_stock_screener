
from flask import Flask, render_template, url_for, flash, redirect


app = Flask(__name__)

app.config['SECRET_KEY'] = 'n657h}zMU9?u}EafsdfadsafdsafdsaF6'



@app.route('/home')
def home_function():
    return 'Hello World' #render_template("home.html", posts=posts, title='Home page')




if __name__ == "__main__":
    app.run( debug=True)