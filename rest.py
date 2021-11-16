from flask import Flask, jsonify,request
import os
from flaskext.mysql import MySQL

from iota import Iota, Address, TryteString, ProposedTransaction, Tag
from iota.crypto.types import Seed

#assign a Flask Class
app=Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'sai'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sheeba99'
app.config['MYSQL_DATABASE_DB'] = 'flir'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

url="http://sai-iota.duckdns.org:14265"

@app.route('/home')
def welcome():
	return "Welcome to Sai Smart Community, Share Power & Earn Tokens. Go Green. \n Login to continue."
@app.route('/getBalance')
def balance():
	seed='AXVLICISWIOLHJREGKV9JJTBBFJFIPZAGGERYFDQYXBQDLNZWCPQKULCHK9TIOLNHTWUSEGICEZCGGXVA'
	api = Iota(url,seed)
	input = api.get_inputs(start=0, stop=10)
	totalbalance=input['totalBalance']
	return str(totalbalance)

@app.route('/getUname/<uname>')
def balance(uname):
	cur = mysql.connect().cursor()
	cur.execute('SELECT friendlyName FROM `DevInfo` WHERE friendlyName = %s;'uname)
	uname = cur.fetchone()
	return uname
if __name__ == '__main__':
#app.run will make the APIs available on this particular IP address and Port 5000
#0.0.0.0  ip means any one can access.
	context = ('local.crt', 'local.key')#certificate and key files
	app.run(debug=True, host="0.0.0.0", port=8080, ssl_context=("cert.pem", "key.pem"))
#     app.run(host="0.0.0.0",port=8080,debug=1)
