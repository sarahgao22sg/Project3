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