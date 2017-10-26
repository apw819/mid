from flask import Flask, request, render_template, make_response, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import Required
import requests
import json

app = Flask(__name__)
app.debug = True 
app.config['SECRET_KEY'] = 'secret key!'

@app.route('/')
def firstpagewithcookie():
	printed = make_response('<p> Hello users! By the way, this site carries a cookie. </p> <h1> Learn More About Your Horoscope Here: </h1> <br> <a href = "/yoursignform" > Your Specific Sign </a> </br> <br> <a href = "/listofsigns" > Each Signs Symbol </a> </br> <br> <a href = "/whatismysignpic" > What Is My Sign? </a> </br> <br> <p> Your Chinese Horoscope. Are you a: <a href = "/chinesehoroscope/Rat" > Rat? </a> <a href = "chinesehoroscope/Ox" > Ox? </a> <a href = "chinesehoroscope/Tiger" > Tiger? </a> <a href = "chinesehoroscope/Rabbit" > Rabbit? </a> <a href = "chinesehoroscope/Dragon" > Dragon? </a> <a href = "chinesehoroscope/Snake" > Snake? </a> <a href = "chinesehoroscope/Horse" > Horse? </a> <a href = "chinesehoroscope/Goat" > Goat? </a> <a href = "chinesehoroscope/Monkey" > Monkey? </a> <a href = "chinesehoroscope/Rooster" > Rooster? </a> <a href = "chinesehoroscope/Dog" > Dog? </a> <a href = "chinesehoroscope/Pig" > Pig? </a>')
	printed.set_cookie('sign', 'Leos')
	return printed

class SignForm(FlaskForm):
    sign = StringField('What is your your sign? Please make sure the first letter is capitalized.', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/yoursignform')
def ursignform():
	simpleForm = SignForm()
	return render_template("yoursign.html", form=simpleForm)

@app.route('/yoursignformresults', methods = ['POST'])
def wtformresults():
	form = SignForm(request.form)
	if request.method == "POST" and form.validate_on_submit():
		sign = form.sign.data
		return render_template("yoursigninfotraits.html".format(sign), sign=request.form["sign"])

@app.route('/listofsigns')
def list():
	symbols = {"Aries":"ram", "Taurus": "bull", "Gemini": "twins", "Cancer": "crab", "Leo": "lion", "Virgo": "maiden", "Libra":"scales", "Scorpio": "scorpion", "Sagittarius":"centaur", "Capricorn": "mountain goat", "Aquarius":"man who carries water", "Pisces": "fish"}
	return render_template('listof12signs.html', symbols=symbols)

@app.route('/whatismysignpic')
def insert_image():
	return render_template ("insertimage.html")

@app.route ('/sign/<ur_sign>')
def ursign(ur_sign):
	twelvelist = ["Aries", "Taurus","Gemini","Cancer", "Leo", "leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
	if ur_sign in twelvelist:
		return render_template("yoursigndynamiclink.html", ursign = ur_sign)
	else:
		return "This is not a correct western horoscope. Please make sure spelling is correct and that the first letter is capitalized."

@app.route ('/chinesehoroscope/<chinese_horoscope>')
def chinese (chinese_horoscope):
	chineselist = ["rat", "Rat", "ox", "Ox", "tiger", "Tiger", "rabbit", "Rabbit", "dragon", "Dragon", "Snake", "snake", "Horse", "horse", "Goat", "goat", "monkey", "Monkey", "rooster", "Rooster", "dog", "Dog", "pig", "Pig"]
	if chinese_horoscope in chineselist:
		return render_template("chinesesection.html", chinesehoroscopes = chinese_horoscope)
	else:
		return "This is not a correct Chinese horoscope. Please make sure spelling is correct and that the first letter is capitalized."

#MAULU: does this count as a dynamic link 2? 

@app.errorhandler(404)
def wrongpage(e):
	return render_template("fourohfourpage.html")

@app.errorhandler(405)
def wrong_page(e):
	return render_template("fourohfive.html")
#you get this error by going directly to the page localhost:5000/yoursignformresults without typing in your sign beforehand 

if __name__ == '__main__':
    app.run()







