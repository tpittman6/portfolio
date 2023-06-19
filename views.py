from flask import Blueprint, render_template, request, jsonify, redirect, url_for


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/my_projects")
def my_projects():
    return render_template("projects.html")

@views.route("/chat_app")
def about_me():
    return render_template("chat_app.html")

@views.route("/encryption")
def encryption():
    return render_template("encryption.html")






#print json data
@views.route("/json")
def get_json():
    return jsonify({'name': 'Terry', 'age':'30'})

#get and return json data
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

