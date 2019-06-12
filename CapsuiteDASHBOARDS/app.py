from flask import Flask, render_template, url_for, flash, redirect
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf import FlaskForm
from flask_nav import Nav
from flask_nav.elements import *
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

class UserManagementForm(FlaskForm):
    firstname = StringField('Firstname',
                           validators=[DataRequired(), Length(min=2, max=20)])

    surname = StringField('Surname',
                           validators=[DataRequired(), Length(min=2, max=20)])

    gender = RadioField('Gender', choices=[('M','Male'), ('F','Female')])

    employee = StringField('Employee Number', 
                                   validators=[DataRequired(), Length(min=5, max=10)])

    position = StringField('Position',
                            validators=[DataRequired(), Length(min=5, max=20)])

    userrole = SelectField('User Role', choices=[('cd','Credit Analyst'),('sa','Sales Agent')]) 

    
    supervisor = StringField('Supervisor', 
                              validators=[DataRequired(), Length(min=5, max=20)])

    department = StringField('Depertment',
                            validators=[DataRequired(), Length(min=5, max=20)])

    email = StringField('Email',
                        validators=[DataRequired(), Email()])

    username = StringField('Username', 
                                   validators=[DataRequired(), Length(min=5, max=20)])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    phone= StringField('Phone 1',
                           validators=[DataRequired(), Length(min=2, max=20)])

    phone2 = StringField('Phone 2',
                           validators=[DataRequired(), Length(min=2, max=20)])

    submit = SubmitField('ADD USER')


class ProductsForm(FlaskForm):
    productname = StringField('Product Name',
                           validators=[DataRequired(), Length(min=2, max=20)])

    productID = StringField('Product ID',
                           validators=[DataRequired(), Length(min=2, max=20)])

    productcategory = StringField('Product Category', 
                                   validators=[DataRequired(), Length(min=5, max=10)])

    productdescription = StringField('Product Description', 
                                   validators=[DataRequired(), Length(min=5, max=10)])
    
    submit = SubmitField('ADD PRODUCT')




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/usermanagement", methods=['GET', 'POST'])
def usermanagement():
    form = UserManagementForm()
 
    return redirect(url_for('home'))
    return render_template('usermanagement.html', title='User Management', form=form)

@app.route("/products", methods=['GET', 'POST'])
def products():
    form = ProductsForm()
    
    return render_template('products.html', title='Products', form=form)



    app.run(debug=True)
