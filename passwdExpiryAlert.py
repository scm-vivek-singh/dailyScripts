import boto3
from datetime import datetime

client = boto3.client('iam')

def getUsers():
    userPasswdAge = {}
    response = client.get_credential_report()
    output = str(response['Content'])
    for _userReport in output.split['\\n']:
        userReport = _userReport.split(',')
        passwdAge = userReport[5]
        userPasswdAge[userReport[1]] = passwdAge
    return userPasswdAge


getUsers()
