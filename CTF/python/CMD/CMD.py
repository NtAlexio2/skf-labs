import os
from flask import Flask, request, render_template
from ctf import get_flag_by_user_input


app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/")
def start():
    return render_template("index.html")


@app.route("/home", methods=['POST'])
def home():
    sizeImg = request.form['size']
    os.system('convert static/img/bones.png -resize ' +
              sizeImg+'% static/img/bones.png')
    flag = get_flag_by_user_input(sizeImg)
    return render_template("index.html", flag=flag)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')