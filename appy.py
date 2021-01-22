from flask import Flask, abort, render_template, redirect, url_for, request, make_response
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
from urllib.parse import urlparse, urljoin
import requests
# from secret import SECRET_KEY, TABLEAU_AUTH, USERS_LIST, PASSWORD_LOGIN

app = Flask(__name__)
app.config['secret_key'] = b'randomstring'
login_manager = LoginManager(app)
users = ["npipkins@yahoo.com"]
password_login = "password_1"
# Tableau server
# server = TSC.Server('http://10.0.55.1')
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

# Wrong assumption
# Used to by Flask to check which is the current logged user.
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

# Route to redirect - when the onload event occurs - to the login page directly
@app.route("/")
def hello():
    # See line 40
    return redirect(url_for('login'))

@app.route("/api/data")
def data():

    return jsonify(table_df.to_dict(orient='records'))

# Must establish server link, probably rename select-dashboard
@app.route("/homepage")
@login_required
def homepage(): #index with all the dashboards
    # with server.auth.sign_in(TABLEAU_AUTH):
    #     workbooks, pagination_item = server.workbooks.get()
               
    #     wblist = [wb for wb in workbooks]
    #     for x in wblist:      
    #         server.workbooks.populate_preview_image(x)
    #         if x.project_name == "yourWorkspace":
    #             with open(folder_path  + "/{}.jpg".format(x.name), "wb") as img_file:   #generate thumbnails of all dashboards
    #                 img_file.write(x.preview_image)
    return render_template("select-dashboard.html")

# Successive app routes, flaskin it
@app.route("/Economic_Impact")    #page of a single dashboard
@login_required
def dashboard():
    # Verify data storage type/structure here
    return render_template("Economic_Impact.html")

@app.route("/Green_Frogs")    #page of a single dashboard
@login_required
def frogs():
    # Verify data storage type/structure here
    return render_template("Economic_Impact.html")

@app.route("/Invasion!")    #page of a single dashboard
@login_required
def invasion():
    return render_template("dashboard.html")

# Ends Session for Tableau I suppose
@app.route('/logout')
def sign_out():
    logout_user()
    return redirect(url_for('login'))

# Promise? Get-Response
@app.route('/get_token')
def get_token():
    resp = make_response()

    token = requests.post("http://10.0.55.1/trusted?username=" + request.cookies.get("username"))
    if (token.status_code != 200 or token.text == '-1'): #200 = OK in HTTP requests
        # Console.log error codes possibly- do check
        return abort(400)

    resp.set_cookie("auth_token", token.text)
    return resp

if __name__ == "__main__":
    app.run(debug=True)




# # Start adding routes here
# session = Session(engine)

# # Try to find TABLEAU EQUIV OF .READ_sql table name in Tableau?
# zebra_econ_df = pd.read_sql(session.query(table.Author, table.Start_Year, table.End_Year, table.Number_of_Years, table.Geographic_Area, table.Dollar_Value, table.Type, table.Specifics, table.Outcomes, con=engine)
# gen_ov_df = pd.read_sql(session.query(table.Author, table.Start_Year, table.End_Year, table.Number_of_Years, table.Geographic_Area, table.Dollar_Value, table.Type, table.Specifics, table.Outcomes, con=engine)
# green_frogs = pd.read_sql(session.query(table.Author, table.Start_Year, table.End_Year, table.Number_of_Years, table.Geographic_Area, table.Dollar_Value, table.Type, table.Specifics, table.Outcomes, con=engine)
# dashie_B = pd.read_sql(session.query(table.Author, table.Start_Year, table.End_Year, table.Number_of_Years, table.Geographic_Area, table.Dollar_Value, table.Type, table.Specifics, table.Outcomes, con=engine)

# session.close() 