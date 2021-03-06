from flask import Flask, jsonify,request
import os
from flaskext.mysql import MySQL

from iota import Iota, Address, TryteString, ProposedTransaction, Tag
from iota.crypto.types import Seed

import ssl
context = ssl.SSLContext()
context.load_cert_chain('/home/saishibu38380/flir/cert.pem', '/home/saishibu38380/flir/key.pem')

#assign a Flask Class
app=Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'sai'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sheeba99'
app.config['MYSQL_DATABASE_DB'] = 'flir'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

url="http://localhost:14265"

@app.route('/')
def welcome():
	return "Welcome to Sai Smart Community, Share Power & Earn Tokens. Go Green. \n Login to continue."
@app.route('/getBalance/<seed>')
def balance(seed):
	#seed='AXVLICISWIOLHJREGKV9JJTBBFJFIPZAGGERYFDQYXBQDLNZWCPQKULCHK9TIOLNHTWUSEGICEZCGGXVA'
	api = Iota(url,seed)
	input = api.get_inputs(start=0, stop=10)
	totalbalance=input['totalBalance']
	data={'balance':totalbalance}
	return data

@app.route('/getUname/<uname>')
def getUname(uname):
	cur = mysql.connect().cursor()
	cur.execute('SELECT DevID,seed,friendlyName FROM `DevInfo` WHERE friendlyName = %s',uname)
	try:	
		data = cur.fetchone()
		uname = data[2]
		seed = data[1]
		DevID = data[0]
		data={'uname':uname,'seed':seed,'DevID':DevID}
		
	except:
		data={'uname':0,'seed':0,'DevID':0}
	return data
if __name__ == '__main__':
#app.run will make the APIs available on this particular IP address and Port 5000
#0.0.0.0  ip means any one can access.
	context = ('local.crt', 'local.key')#certificate and key files
	app.run(debug=True, host="0.0.0.0", port=8080)
# 	ssl_context=("cert.pem", "key.pem")
#     app.run(host="0.0.0.0",port=8080,debug=1)
