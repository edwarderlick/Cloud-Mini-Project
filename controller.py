from flask import Flask, request, render_template, g, redirect, url_for, flash, jsonify
from flask import session as flask_session
import model
import jinja2
import os
from datetime import datetime, date, timedelta
import requests

# APP INFO

app = Flask(__name__)
app.secret_key = "THISISMYTESTINGKEY"
app.jinja_env.undefined = jinja2.StrictUndefined

# Routes

@app.route("/db")
def db_hits():
	"""Will show how many hits by querying the db."""
	
	#Adds the current hit to the database
	current_hit = model.Hit(hit_date=datetime.now())
	model.sqla_session.add(current_hit)
	model.sqla_session.commit()

	#Determines how many hits the database has had.
	hits = model.sqla_session.query(model.Hit).count()

	return render_template("mysqlhit.html", hits=hits)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)