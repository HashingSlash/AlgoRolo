#----------#        IMPORTS
import requests
import json
import csv
import datetime
import base64

def saveDB(DB, name):
    DBJson = json.dumps(DB)
    outFile = open(name + '.json', 'w')
    outFile.write(DBJson)
    outFile.close()

def loadDB(fileName):
    inFile = open(fileName, 'r')
    loadFile = json.load(inFile)
    inFile.close()
    return loadFile


try:
    addressDB = loadDB('AlgoAddressDB.json')
    appDB = loadDB('AlgoAppDB.json')
    print('Loaded App and Address DBs')
except:
    addressDB = {}
    appDB = {}
    print('blank App and Address DBs')
    pass

run = 'y'
while run == 'y':
    print('Add new Address or dApp ID?')
    addOrApp = input('(A)ddress or dApp (I)D: ').lower()
    if addOrApp == 'a':
        newAddress = input('Paste address to check: ').upper()
        if newAddress not in addressDB:
            print('Adding new address')
            platform = input('What platform uses this address? (EG: Tinyman, Yieldly, Rand Gallery): ')
            addressDef = input('What is this address used for? (EG: ALGO/USDC Swap, LP Token Staking, AKC/ALGO Sale: ')
            addressDB.update({newAddress: [platform, addressDef]})
            saveDB(addressDB, 'AlgoAddressDB')
            print('updated addressDB')
        else:
            print('Address exists', addressDB[newAddress])
    elif addOrApp == 'i':
        newApp = input('Paste app id: ')
        if newApp not in appDB:
            print('Adding new dApp ID')
            platform = input('What platform uses this app ID? (EG: Tinyman, Yieldly, AlgoFi): ')
            appDef = input('What is this app ID used for? (EG: ALGO/USDC Swap, LP Token Staking, OPUL>OPUL Staking: ')
            appDB.update({newApp : [platform, appDef]})
            saveDB(appDB, 'AlgoAppDB')
            print('updated appDB')
        else:
            print('dApp ID exists', appDB[newApp])
    else:
        print('input error')
    run = input('Run again? (y/n): ')
    print('\n')


