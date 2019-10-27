
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




