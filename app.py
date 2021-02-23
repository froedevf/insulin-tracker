from flask import Flask, render_template
import psycopg2
import databasehelper

app = Flask(__name__)
@app.route("/")
def index():
	# Load current count
    f = open("count.txt", "r")
    count = int(f.read())
    f.close()
	
	# Increment the count
    count += 1

	# Overwrite the count
    f = open("count.txt", "w")
    f.write(str(count))
    f.close()

    userName = 'davekatz'
    userId = databasehelper.queryUserId(userName=userName)

    return render_template("index.html", count=count, userId=userId, userName=userName)
    
if __name__ == "__main__":
	app.run()