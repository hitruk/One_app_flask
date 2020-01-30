from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    return "Hello World from Flask Page"


@application.route("/help")
def helppage():
    return "<h3>this is help<h3>"


@application.route("/users")
def userspage():
    return "<h3>users page<h3>"


@application.route("/user/<username>")
def show_user_page(username):
    return "Hellow " + username.upper()


@application.route("/path/<path:subpath>")
def print_subpath(subpath):
    return "Subpath is: " + subpath


@application.route("/kvadrat/<int:x>")
def calc_kvadrat(x):
    return "Kvadrat ot: " + str(x) + "=" + str(x * x)


@application.route("/htmlpage")
def page_html():
    myfile = open("mypage.html", mode='r')
    page = myfile.read()
    myfile.close()
    return page


if __name__ == "__main__":
    application.run()
