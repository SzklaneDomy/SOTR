from flask import render_template, url_for, request, redirect
from web_app import app
from web_app import get_stats

@app.route("/", methods=["GET", "POST"])
@app.route("/home.html", methods=["GET", "POST"])
def home():

	if request.method == "POST":
		band_name = request.form['band']
		if get_stats.return_stats(band_name) == "albums_not_found":
			# TODO make something
			print("Albums not found")

	return render_template('home.html')
