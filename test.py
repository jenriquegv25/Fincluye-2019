# -*- coding: utf-8 -*-

from __future__ import print_function    # (at top of module)
import sys
import time
import requests
from matplotlib import pyplot as plt

import markdown


# Note: in order to use this example, you need to have at least one account
# that you can send money from (i.e. be the owner).
# All properties are now kept in one central place

from default import *


# You probably don't need to change those
import lib.obp
obp = lib.obp

obp.setBaseUrl(BASE_URL)
obp.setApiVersion(API_VERSION)

# Login and set authorized token
obp.login(USERNAME, PASSWORD, CONSUMER_KEY)


user = obp.getCurrentUser()
user_id = user['user_id']

our_bank = OUR_BANK 


def getAccounts():
    # Prepare headers
    response = requests.get(u"https://fincluye.openbankproject.com/obp/v4.0.0/banks/fincluye.0001.mx.fincluye/accounts", headers=obp.mergeHeaders(obp.DL_TOKEN, obp.CONTENT_JSON))
    return response.json()

def get_transactions(accounts):
    out=[]
    for account in accounts:
        ide =account['id']
        transactions = obp.getTransactions(our_bank,ide)
        out.append([account["label"]])
        for t in transactions:
            out[-1].append(float(t['details']['value']['amount']))
    return out


plot_name="fincluyeapp/index/static/index/images_plot/plot_"
plot_number=0
def plot_transactions(transactions):
    global plot_number,plot_name
    for data in transactions:
        plt.title(data[0])
        plt.scatter(range(len(data[1:])),data[1:])
        plt.savefig('{}{}.png'.format(plot_name,plot_number))
        plt.close()
        plot_number+=1   
    return plot_number

def kyc(*args):
    return True


def generate_report(): 
    global plot_number
    accounts = getAccounts()
    transactions = get_transactions(accounts)
    number = plot_transactions(transactions)
    document="""# Análisis \n##Accounts"""
    for account in accounts:
        document+= "\n- "+account["label"]
    document+="\n##Transferencias por cuenta \n"

    for i in range(plot_number):
        document+="![]({}{}.png)\n".format("images_plot/plot_",i)

    html = markdown.markdown(document)
    with open('fincluyeapp/static/index/analisis.html',"w") as fil:
        fil.write(html)

    return html




generate_report()
