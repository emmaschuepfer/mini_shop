from flask import Flask
from flask import render_template


# http://flask.pocoo.org/
app = Flask(__name__)


shirts = 10



@app.route("/", methods=["GET"])
def index():
    return render_template("shop.html")


@app.route("/buy", methods=["POST"])
def buy():
	global shirts
	shirts = max(shirts-1, 0)
	return "success"

@app.route("/inventory", methods=["GET"])
def inventory():
	global shirts
	#~ return {"shirts": shirts}
	return str(shirts)
	


#~ app.run(host="0.0.0.0", port=8080) # local network
app.run(host="127.0.0.1", port=8080) # localhost
