from  flask import Flask , render_template , request ,flash ,redirect ,url_for , session
from models import retrieveUser , insertUser
from werkzeug.exceptions import Aborter
import passlib.hash as phash

list_from_db = retrieveUser()
list_of_hash = []
creds = {}
USERNAMES = {}
for i in list_from_db:
    creds[i[0]] = i[2]
    USERNAMES[i[0]] = i[1]
    list_of_hash.append(i[2])

app = Flask(__name__)
app.secret_key='random_string' # here we have used the random_string as a secret key
user = []

@app.route("/",methods=["GET"])
def login():
    session['logged_in']=False
    return render_template("login.html")

@app.route("/action",methods=["GET","POST"])
def action():
    '''Here we will check which button is clicked'''
    clickBtn = request.form.get("btn")
    mail = request.form["email"]
    passwd = request.form["pass"]
    username = []
    for i in creds:
        if creds[i] == mail:
            username.append(i)

    if clickBtn == 'Login' :
            if not mail or not passwd:
                flash("Enter the Email Address or Password !!")
                return redirect(url_for("login"))
            elif request.form['email'] in creds and phash.bcrypt.verify(passwd,creds[request.form.get("email")]):
                session['logged_in'] = True
                return redirect(url_for("logged_in"))
            else:
                flash("Wrong Credentials!!")
                return redirect(url_for("login"))
    if clickBtn == "Register" :
        return render_template("register.html")

    def same_register():
        return render_template("register.html")

    return same_register()


@app.route("/action/register",methods=['get','post'])
def register():
    clickBtn = request.form.get("btn")
    mail = request.form.get("email")
    uname = request.form.get("uname")
    passwd = request.form.get("pass")
    if clickBtn =="Back":
        return redirect(url_for("login"))

    if clickBtn == "Register" and uname and passwd and mail:
        insertUser(mail, uname, passwd)
        el = retrieveUser()
        return render_template("registered.html",users=el)

    if clickBtn == "Register" and (not uname or not passwd or not mail):
        flash("You must give the values !!!")
        return redirect(url_for('action'))


@app.route("/action/login")
def logged_in():
    if session['logged_in']:
            return render_template("dashboard.html",em=session['logged_in'])
    else:
        flash("Give Creds")
        return render_template("login.html")

@app.route("/action/login/aboutus")
def aboutus():
    if session['logged_in']:
            return render_template("aboutus.html")
    else:
        flash("GIve Creds")
        return render_template("login.html")

