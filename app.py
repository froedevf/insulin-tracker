from flask import Flask, render_template, request
import psycopg2
from databasehelper import executeSql, query, queryUserId
import datetime as dt

fresh_window = dt.timedelta(seconds=30)
app = Flask(__name__)
@app.route("/", methods=['GET'])
def index():
    # Read input params
    userName = request.args.get("n")
    item = request.args.get("i")
    resetreq = request.args.get("r")
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
    return render_template('chart.html', set=zip(values, labels, colors))
    
    if resetreq == "1":
        return reset( userName, item )
    else:
        return activate_or_age( userName, item )
    
def activate_or_age( userName, item ):
    ''' if a vial is already activated, return the age, otherwise activate and return 0 '''

    # Validate/Find the username
    try:
        userId = queryUserId(userName=userName)
    except:
        return render_template("error.html", msg="UserName {0} not found, please register!".format(userName))

    # Find out if vial is already activated
    ts = dt.datetime.now()
    
    itemCount = query("select count(*) from vials where user_id={0} and id={1}".format(userId, item))
    if itemCount == 0:
        # Activate!
        sql = "INSERT INTO vials (id, user_id, counter_start, checks) values ({0},{1},'{2}',{3})".format( item, userId, ts, 0 )
        executeSql(sql)
        return render_template("activate.html", userName=userName, item=item, ts=ts )
    else:
        # Check!
        sql = "SELECT counter_start FROM vials WHERE user_id={0} and id={1}".format(userId, item)
        act_ts = query(sql)
        age = ts - act_ts
        is_good = fresh_window > age
        timeleft = fresh_window - age
        if fresh_window < dt.timedelta(minutes = 1): # for testing only, fresh window is in seconds
            timeleftstr = "{0} seconds".format( timeleft.total_seconds() )
        else:
            timeleftstr = "{0} days".format( timeleft.days )
        if is_good:
            labels = ["January","February","March","April","May","June","July","August"]
            values = [10,9,8,7,6,4,7,8]
            colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
            return render_template("good.html", userName=userName, item=item, timeleft=timeleftstr, ts=act_ts, set=zip(values, labels, colors) )
        else:
            return render_template("stale.html", userName=userName, item=item, timeexpired=timeleftstr, ts=act_ts, reset=reset )
        

def reset( userName, item ):
    userId = queryUserId(userName=userName)
    sql = "DELETE FROM vials WHERE user_id='{0}' and id='{1}'".format(userId, item)
    executeSql(sql)
    return render_template("reset.html", userName=userName, item=item, ts=dt.datetime.now() )

if __name__ == "__main__":
	app.run(debug=True)