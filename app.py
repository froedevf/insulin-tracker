from flask import Flask, render_template, request
import psycopg2
import databasehelper
import datetime as dt

app = Flask(__name__)
@app.route("/", methods=['GET'])
def index():
    # Read input params
    userName = request.args.get("n")
    item = request.args.get("i")
    
    # Validate/Find the username
    try:
        userId = databasehelper.queryUserId(userName=userName)
    except:
        return render_template("error.html", msg="UserName {0} not found, please register!".format(userName))

    # Find out if vial is already activated
    ts = dt.now()
    
    res = activate_or_age( ts, userId, item )
    
    return render_template("index.html", userId=userId, userName=userName, item=item)
    
if __name__ == "__main__":
	app.run(debug=True)