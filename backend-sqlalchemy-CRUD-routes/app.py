from flask import Flask, render_template, request, redirect, session, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from model.users import Users
from model.users import db

from form import RegisterForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:Nopassword%4003@localhost/test"
)

loginmanager = LoginManager()
loginmanager.init_app(app)
loginmanager.login_view = "login"


@loginmanager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        user = Users(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return render_template(
            "login.html", message="Registration successful! Please log in."
        )
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    user = Users.query.filter_by(username=username).first()
    if user and user.check_password(request.form.get("password")):
        login_user(user)
        print(user.id)
        return redirect(url_for("dashboard", user_id=user.id))
    return render_template("login.html", error="Invalid credentials")


@app.route("/dashboard<int:user_id>")
@login_required
def dashboard(user_id):
    return render_template("dashboard.html", user_id=user_id, current_user=current_user.username)


@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect("/login")


@app.route("/delete_account/<int:user_id>", methods=["GET", "POST"])
@login_required
def delete_account(user_id):
    user = Users.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
    session.pop("user_id", None)
    return redirect("/login")


@app.route("/update_email/<int:user_id>", methods=["POST", "GET"])
@login_required
def update_email(user_id):
    if request.method == "POST":
        new_email = request.form.get("new_email")
        print(f"New Email is {new_email}")
        user = Users.query.get(user_id)
        if user:
            user.email = new_email
            db.session.commit()
            return redirect(url_for("dashboard", user_id=user_id))
    user = Users.query.get(user_id)
    if user:
        return render_template("update_email.html", user=user)


@app.route("/fetch_all")
@login_required
def fetch_all():
    users = Users.query.all()
    for user in users:
        print("list of users#################:", user.username)
    return render_template("fetch_all_users.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)
