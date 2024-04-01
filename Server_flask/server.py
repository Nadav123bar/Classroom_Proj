from flask import Flask,render_template,request, jsonify,redirect
from loguru import logger
import sqlManager
import hashlib
from datetime import datetime

logger.info("demo")

app = Flask("Find_My_Phone")

authorized_users = {}

@app.route('/')
def welcome():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    sql_Manager = sqlManager.SqlDb()
    user_name = request.form.get("user_name")
    password = request.form.get("pass")
    logger.debug(password)
    logger.debug(user_name)

    # For simplicity, comparing the password directly
    if sql_Manager.does_pass_and_username_match(user_name,password):
        key = user_name + password + datetime.now().strftime("%H:%M:%S")
        authorized_users[user_name] = hashlib.sha256(key.encode()).hexdigest()
        return jsonify(success=True, redirect="/map?user_name=" + user_name + "&key=" + (authorized_users[user_name]))
    else:
        return jsonify(success=True, redirect="/")


@app.route('/map')
def map():
    user_name = request.args.get("user_name")
    key = request.args.get("key")
    logger.debug(user_name)
    if (user_name not in authorized_users) or (key != authorized_users[user_name]):
        # Redirect to the login page if not authenticated
        return redirect(('/hacker'))
    return render_template("map.html")


@app.route('/get_location', methods=['POST'])
def getLocation():
    sql_Manager = sqlManager.SqlDb()
    user_name = request.form.get("user_name")
    logger.debug(user_name)
    lat_lng = sql_Manager.get_Location(user_name)[0]
    lat = lat_lng[0]
    logger.debug(lat)
    lng = lat_lng[1]
    logger.debug(lng)

    coordinates = {'lng': lng, 'lat': lat}
    logger.debug(coordinates)
    logger.debug(jsonify(coordinates))
    return jsonify(coordinates)


@app.route("/hacker")
def hacker():
    return "<h1>GO AWAY HACKER</h1>"


@app.route('/set_location', methods=['POST'])
def setLocation():
    logger.debug(request.get_json())
    data = request.get_json()
    lng = data['lng']
    lat = data['lat']
    u_name = data['user_name']
    logger.debug(lng + ',' + lat + ',' + u_name)
    return data

    

if __name__ == '__main__':
    app.run(debug = True)
