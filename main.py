import MySQLdb

def pass_check(barcode, passcode):
	sql = "SELECT * FROM users WHERE barcode = " + barcode
		try:
    	# Execute the SQL command
    	cursor.execute(sql)
    	# Fetch all the rows in a list of lists.
    	results = cursor.fetchall()
    	for row in results:
        barcodetemp = row[0]
        passcodetemp = row[1]
	if passcode != passcodetemp:
    		print("wrongcode")
    		return "false"
	return "true"

def priv_check(id):
	sql = "SELECT * FROM users WHERE id = " + id
		try:
    	# Execute the SQL command
    	cursor.execute(sql)
    	# Fetch all the rows in a list of lists.
    	results = cursor.fetchall()
    	for row in results:
        role = row[5]
	if role == 1:
		return "normal"
	elif role == 2:
		return "operator"
	elif role == 3:
		return "admin"
	elif: role == 0:
		return "prob"
	else:
		print("a unexpected error occured, please contact a operator")
		return "error"

def get_id(barcode):
	sql = "SELECT * FROM users WHERE barcode = " + barcode
		try:
    	# Execute the SQL command
    	cursor.execute(sql)
    	# Fetch all the rows in a list of lists.
    	results = cursor.fetchall()
    	for row in results:
        id = row[2]
	return id

def get_status_small(id):
	sql = "SELECT * FROM users WHERE id = " + id
		try:
    	# Execute the SQL command
    	cursor.execute(sql)
    	# Fetch all the rows in a list of lists.
    	results = cursor.fetchall()
    	for row in results:
        stat = row[6]
	return stat
	
def get_status_big(id):
	presql = "SELECT * FROM users WHERE id = " + id
		try:
    	# Execute the SQL command
    	cursor.execute(sql)
    	# Fetch all the rows in a list of lists.
    	results = cursor.fetchall()
    	for row in results:
        stat = row[7]
	return stat

def register_user(barcode)
	sql = SELECT * FROM 
#open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

print("please scan barcode or manually insert code followed by enter")
barcode = input()
please enter passcode
passcode = input()
check = pass_check(barcode = barcode, passcode = passcode)
if check != "true"
	print("code not recognised")
	print("do you want to register")
	stat = input()
else
	print("code recognised")
