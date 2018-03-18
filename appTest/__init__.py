import sqlite3
import os
from flask import Flask, request, session, g, redirect, url_for, abort, flash, render_template
from flask_uploads import patch_request_class

app = Flask(__name__)
app.config.from_pyfile('default.cfg')
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'appTest.db')))
patch_request_class(app, 10*1024*1024)

#from appTest import views

def connect_db():
	conn = sqlite3.connect(app.config['DATABASE'])
	conn.row_factory = sqlite3.Row
	return conn
def get_db(): 
	if not hasattr(g,'sqlite3_db'):
		g.sqlite3_db = connect_db()
	return g.sqlite3_db
def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('resources/schema_users.sql', mode= 'r') as f:
			db.cursor().executescript(f.read())
		db.commit()
def Test():
	return True
	
from appTest import views