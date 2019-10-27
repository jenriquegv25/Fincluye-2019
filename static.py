import requests


class User:
	def __init__(self,name,mail,birthday):
		self.name=name
		self.mail=mail
		self.bir=bird

def json2user(dic):
	if isinstance(dic,dict):
		return User(dic["name"],dic["mail"],dic["birthday"])
	return dic


dummy1={
	"name":"Nombre inventado uno",
	"mail":"Correo@inventado.com",
	"birthday":"13-09-1983",
	"costumer_id" : "pendint",
	"kyc": False,
	"transactions": [(1,122),(2,134),(4,123),(5,233),(6,342),(7,23),(8,432)]
  
}



dummy2={
	"name":"Nombre inventado dos",
	"mail":"dos@inventado.com",
	"birthday":"13-12-1963",
	"costumer_id" : "pendint",
	"kyc": True,
	"transactions": [(1,12),(2,134),(4,8),(5,233),(6,342),(7,23),(8,42)]
}


dummy3={
	"name":"Nombre inventado uno",
	"mail":"tres@inventado.com",
	"birthday":"29-04-1978",
	"costumer_id" : "pendint",
	"kyc": False,
	"transactions": [(1,234),(2,134),(4,3),(5,23),(6,32),(7,23),(8,32)]
}

dummys=[dummy1,dummy2,dummy3]

LOGGING     = True

CONTENT_JSON  = { 'content-type'  : 'application/json' }

BASE_URL    = "https://fincluye.openbankproject.com"

def mergeHeaders(x, y):
	z = x.copy()
	z.update(y)
	return z

def setToken(t):
	global DL_TOKEN 
	DL_TOKEN = { 'Authorization' : 'DirectLogin token=%s' % t}


# Logger
def log(m):
    if LOGGING:
        print(m)

def login():
	username="omega16"
	password="Omega16-_-12"
	consumer_key="nd1inyhsr35phlirthmrhywb4j4fhd2gkm5cl4dd"
	login_url = '{0}/my/logins/direct'.format(BASE_URL)
	login_header  = { 'Authorization' : 'DirectLogin username="%s",password="%s",consumer_key="%s"' % (username, password, consumer_key)}
	# Login and receive authorized token
	log('Login as {0} to {1}'.format(login_header, login_url))
	r = requests.post(login_url, headers=login_header)
	if (r.status_code != 201):
	    log("error: could not login")
	    log("text: " + r.text)
	    return r.text
	t = r.json()['token']
	log("Received token: {0}".format(t))
	setToken(t)
	return t
 
def get_customer_by_number(number):
	print("customer_number",number)
	response=requests.post("https://fincluye.openbankproject.com/obp/v4.0.0/banks/fincluye.0001.mx.fincluye/customers/customer-number",data={"customer_number":number},headers={ 'Authorization' : 'DirectLogin token={}'.format(DL_TOKEN)})
	return response

def get_data_Customer(name,mail):
	for i in dummys:
		i["mail"]==mail
		return i

def add_KYC(name,mail,document):
	customer=get_data_Customer(name,mail)
	customer["kyc"]=document

def get_Transactions(name,mail,from_date,to_date):
	user = get_data_Customer(name,mail)
	return user["transactions"]


def model_Transactions(name,mail,from_date,to_date):
	data =getTransactions(name,mail,from_date,to_date)







#To From
def getCustomer(user):
	user=json2user(user)
	return get_data_Customer(user.name,user.mail)


def addKYC(user,document):
	user=json2user(user)
	add_KYC(user.name,user.mail,document)


def checkKYC(user):
	user=json2user(user)
	user=get_data_Customer(user.name,user.mail)
	return user['kyc']
	

def getTransactions(user,from_date,to_date):
	user=json2user(user)
	return getTransactions(user.name,user.mail,from_date,to_date)



def modelTransactions(user,from_date,to_date):
	return model_Transactions(user.name,user.mail,from_date,to_date)




def test():
	t=login()
	customer=get_customer_by_number("594226459")
	print(customer,customer.text)
	return customer



"""
{  "legal_name":"Jack Son Mylner",  
	"mobile_phone_number":"+44 07972 444 876",  
	"email":"JSM@example.com",  
	"face_image":{    "url":"www.openbankproject",    "date":"2017-09-19T00:00:00Z"  },  
	"date_of_birth":"2017-09-19T00:00:00Z",  
	"relationship_status":"single",  
	"dependants":10,  "dob_of_dependants":["2017-09-19T00:00:00Z"],  "credit_rating":{    "rating":"OBP",    "source":"OBP"  },  "credit_limit":{    "currency":"EUR",    "amount":"10"  },  "highest_education_attained":"Master",  "employment_status":"worker",  "kyc_status":true,  "last_ok_date":"2017-09-19T00:00:00Z",  "title":"Dr.",  "branchId":"DERBY6",  "nameSuffix":"Sr"
}

{
    "bank_id": "fincluye.0001.mx.fincluye",
    "customer_id": "ce8d1ea4-f9c4-4734-b56a-efdb5400771f",
    "customer_number": "594226459",
    "legal_name": "Jack Son Mylner",
    "mobile_phone_number": "+44 07972 444 876",
    "email": "jsm@example.com",
    "face_image": {
        "url": "www.openbankproject",
        "date": "2017-09-19T00:00:00Z"
    },
    "date_of_birth": "2017-09-19T00:00:00Z",
    "relationship_status": "single",
    "dependants": 10,
    "dob_of_dependants": [
        "2019-10-27T02:14:57Z"
    ],
    "credit_rating": {
        "rating": "OBP",
        "source": "OBP"
    },
    "credit_limit": {
        "currency": "EUR",
        "amount": "10"
    },
    "highest_education_attained": "Master",
    "employment_status": "worker",
    "kyc_status": true,
    "last_ok_date": "2017-09-19T00:00:00Z",
    "title": "Dr.",
    "branchId": "DERBY6",
    "nameSuffix": "Sr"
}












{  "legal_name":"Alice Balinda Martinez",  
	"mobile_phone_number":"+44 07972 444 876",  
	"email":"abm@example.com",  
	"face_image":{    "url":"www.openbankproject",    "date":"2017-09-19T00:00:00Z"  },  
	"date_of_birth":"2017-09-19T00:00:00Z",  
	"relationship_status":"single",  
	"dependants":10,  "dob_of_dependants":["2017-09-19T00:00:00Z"],  "credit_rating":{    "rating":"OBP",    "source":"OBP"  },  "credit_limit":{    "currency":"EUR",    "amount":"100"  },  "highest_education_attained":"Master",  "employment_status":"worker",  "kyc_status":true,  "last_ok_date":"2017-09-19T00:00:00Z",  "title":"Dr.",  "branchId":"DERBY6",  "nameSuffix":"Sr"
}

{
    "bank_id": "fincluye.0001.mx.fincluye",
    "customer_id": "74de8f87-a7b9-465d-b814-1c52a0f787f0",
    "customer_number": "570194715",
    "legal_name": "Alice Balinda Martinez",
    "mobile_phone_number": "+44 07972 444 876",
    "email": "abm@example.com",
    "face_image": {
        "url": "www.openbankproject",
        "date": "2017-09-19T00:00:00Z"
    },
    "date_of_birth": "2017-09-19T00:00:00Z",
    "relationship_status": "single",
    "dependants": 10,
    "dob_of_dependants": [
        "2019-10-27T02:17:11Z"
    ],
    "credit_rating": {
        "rating": "OBP",
        "source": "OBP"
    },
    "credit_limit": {
        "currency": "EUR",
        "amount": "100"
    },
    "highest_education_attained": "Master",
    "employment_status": "worker",
    "kyc_status": true,
    "last_ok_date": "2017-09-19T00:00:00Z",
    "title": "Dr.",
    "branchId": "DERBY6",
    "nameSuffix": "Sr"
}













{  "legal_name":"Moises Urrutia Torres",  
	"mobile_phone_number":"+44 07972 444 876",  
	"email":"mut@example.com",  
	"face_image":{    "url":"www.openbankproject",    "date":"2017-09-19T00:00:00Z"  },  
	"date_of_birth":"2017-09-19T00:00:00Z",  
	"relationship_status":"single",  
	"dependants":10,  "dob_of_dependants":["2017-09-19T00:00:00Z"],  "credit_rating":{    "rating":"OBP",    "source":"OBP"  },  "credit_limit":{    "currency":"EUR",    "amount":"100"  },  "highest_education_attained":"Master",  "employment_status":"worker",  "kyc_status":true,  "last_ok_date":"2017-09-19T00:00:00Z",  "title":"Dr.",  "branchId":"DERBY6",  "nameSuffix":"Sr"
}



{
    "bank_id": "fincluye.0001.mx.fincluye",
    "customer_id": "3fc33d30-5247-4fa4-8a96-cccec4d1861d",
    "customer_number": "1711901048",
    "legal_name": "Moises Urrutia Torres",
    "mobile_phone_number": "+44 07972 444 876",
    "email": "mut@example.com",
    "face_image": {
        "url": "www.openbankproject",
        "date": "2017-09-19T00:00:00Z"
    },
    "date_of_birth": "2017-09-19T00:00:00Z",
    "relationship_status": "single",
    "dependants": 10,
    "dob_of_dependants": [
        "2019-10-27T02:18:31Z"
    ],
    "credit_rating": {
        "rating": "OBP",
        "source": "OBP"
    },
    "credit_limit": {
        "currency": "EUR",
        "amount": "100"
    },
    "highest_education_attained": "Master",
    "employment_status": "worker",
    "kyc_status": true,
    "last_ok_date": "2017-09-19T00:00:00Z",
    "title": "Dr.",
    "branchId": "DERBY6",
    "nameSuffix": "Sr"
}

"""



