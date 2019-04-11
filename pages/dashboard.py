from flask import jsonify, render_template, request, Response
from flask.ext.login import current_user, login_user

from functions import app
from functions.connect_to import getConnection
from models import User

import mysql.connector

@app.route('/dashboard', methods=['GET'])
def dashboard():

    login_user(User.query.get(1))
    
    args = {
            'gift_card_eligible': True,
            'cashout_ok': True,
            'user_below_silver': current_user.is_below_tier('Silver'),
    }
    return render_template("dashboard.html", **args)


@app.route('/community', methods=['GET'])
def community():

    login_user(User.query.get(1))

    connInfo = getConnection('access')
    print(connInfo['database'])
    db = mysql.connector.connect(host=connInfo['host'], user=connInfo['user'], passwd=connInfo['password'], db=connInfo['database'])

    cursor = db.cursor(dictionary=True)    
    cursor.execute('''SELECT * FROM (
    	SELECT * FROM user ORDER BY user_id DESC LIMIT 5
	) sub
	ORDER BY user_id ASC''')
    data = cursor.fetchall()
    phone_num = []
    phone_num.append(["12345", "12463"])
    phone_num.append(["123235"])
    phone_num.append(["145132345", "12466663"])
        
    return render_template("community.html", data=data, phone_num=phone_num)
