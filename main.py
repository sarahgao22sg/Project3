from flask import Flask, abort, render_template, redirect, url_for, request, make_response
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
from urllib.parse import urlparse, urljoin
import requests, tableauserverclient as TSC
from secret import SECRET_KEY, TABLEAU_AUTH, USERS_LIST, PASSWORD_LOGIN

app = Flask(__name__)
app.secret_key = SECRET_KEY
login_manager = LoginManager(app)
users = npipkins@yahoo.com
password_login = password1!

# Tableau server
server = TSC.Server('http://10.0.55.1')
folder_path = "C:/Users/Administrator/Desktop/Flask-WebServer/static/images"

# Class User which extends UserMixin used to register users.5765
# Probably converts to Tableau compatable class/object
class User(UserMixin):
    # Constructor
    def __init__(self, user_id):
        self.id = user_id
        self.name = users[int(user_id)]

    def get(self, name):
        return users.index(name)

        # Check if url to render is safe

# Query address        
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc

# Route for handling the login page logic
# Checks if user exists and password matches
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if (request.method == 'POST'):
        if (request.form['username'] not in users or request.form['password'] != password_login):
            error = 'Invalid Credentials. Please try again.'
        else:
            user = User(users.index(request.form['username']))
            login_user(user)
            next = request.args.get('next')

            if not is_safe_url(next):
                return abort(400)

            resp = make_response(redirect('/homepage'))

# Start adding routes here
session = Session(engine)

zebra_econ_df = pd.read_sql(session.query(table.Author, table.Start_Year, table.End_Year, table.Number_of_Years, table.Geographic_Area, table.Dollar_Value, table.Type, table.Specifics, table.Outcomes, con=engine)

session.close() 