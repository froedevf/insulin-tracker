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
    
    return activate_or_age( userName, item )
    
def activate_or_age( userName, item )
    ''' if a vial is already activated, return the age, otherwise activate and return 0 '''

    # Validate/Find the username
    try:
        userId = databasehelper.queryUserId(userName=userName)
    except:
        return render_template("error.html", msg="UserName {0} not found, please register!".format(userName))

    # Find out if vial is already activated
    ts = dt.datetime.now()
    
    itemCount = databasehelper.query("select count(*) from vials where user_id={0} and id={1}".format(userId, item)
    if itemCount==0:
        # Activate!
        sql = "INSERT INTO vials (id, user_id, counter_start, checks) values ({0},{1},{2},{3})".format( item, userId, ts, 0 )
        return render_template("Activate.html", userName=userName, item=item, ts=ts )
    else:
        # Check!
        sql = "SELECT counter_start FROM vials WHERE user_id={0} and id={1}".format(userId, item)
        act_ts = databasehelper.query(sql)
        age = act_ts - ts
        daysleft = 28 - age.days()
        if dt.timedelta(days=28) > age:
            return render_template("Good.html", userName=userName, item=item, daysleft=daysleft )
        else:
            return render_template("Stale.html", userName=userName, item=item, daysleft=-daysleft )
        
        
    
if __name__ == "__main__":
	app.run(debug=True)