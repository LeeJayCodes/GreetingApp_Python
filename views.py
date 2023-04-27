# from flask import Blueprint, render_template, request, flash, session


# views = Blueprint(__name__, "views")


# @views.route("/")
# def index():
#     if 'name' in session:
#         flash('Hi, ' + session['name'] + ', Welcome back!')
#         return render_template("index.html")
#     else:
#         flash("Tell me your name!")
#         return render_template("index.html")

# @views.route("/greet", methods=["POST", "GET"])
# def greet():
#     name = str(request.form['name']).capitalize()
#     flash("Hi " + str(request.form['name']).capitalize()+ ", great to see you!")
#     session['name'] = name
#     return render_template("index.html")

from flask import Blueprint, render_template, request, flash, make_response

views = Blueprint(__name__, "views")

@views.route("/")
def index():
    name = request.cookies.get('name')
    if name:
        flash(f"Hi {name}! Welcome back!")
    else:
        flash("Tell me your name!")
    return render_template("index.html")

@views.route("/greet", methods=["POST", "GET"])
def greet():
    name = str(request.form['name']).capitalize()
    flash(f"Hi {name}, great to see you!")
    response = make_response(render_template("index.html"))
    response.set_cookie('name', name)
    response.set_cookie('name', name, max_age=60)
    return response    