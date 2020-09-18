from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
from datetime import date
import random as rnd
import os.path
import string


app = Flask(__name__)
app.permanedent_session_lifetime = timedelta(minutes=180)

app.secret_key = "hello"


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits +  string.digits 
    result_str = ''.join((rnd.choice(letters_and_digits) for i in range(length)))
    return(result_str)


@app.route("/")
def main():
	return redirect(url_for("home"))

@app.route("/home")
def home():
	return render_template("home.html")



@app.route("/newurl/<url>")
def newurl(url):
	print(url)
	for i in url:
		url = url.replace("~", "/")
		url = url.replace(":", "_")
		url = url.replace(",", "?")

	url = url.replace("htps/", "https://")
	url = url.replace("htp/", "http://")


	while (True):
		urlNum = str(get_random_alphanumeric_string(7))

		if os.path.isfile("database/" + urlNum) == False:
			break

	

	fnew = open("database/" + urlNum + ".txt", "x")
	f = open ("database/" + urlNum + ".txt", "w")

	f.write(url)
	f.close()
	return render_template("afterform.html", url=urlNum)

@app.route("/<url>")
def forward(url):
	if os.path.isfile("database/" + url + ".txt") == False:
		return "URL does not exist"
	else:
		f = open("database/" + url + ".txt", "r")
		value = f.read()

		return redirect(value)
		





if __name__ == "__main__":
	app.run(host="0.0.0.0",debug=True)