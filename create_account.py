from source import resource


if __name__ == '__main__' :

    resourceCustomField = []
    resourceCustomFieldObj = {'customLabel':'Age', 'customValue':'60'}
    resourceCustomField.append(resourceCustomFieldObj)
    resourceCustomFieldObj1 = {'customLabel':'Class', 'customValue':'23'}
    resourceCustomField.append(resourceCustomFieldObj1)
    #print(resourceCustomField)
    resourceId=1202
    accountDetails = []
    account1={
      "accountName": "Christus",
      "password": "Christus@1234",
      "accountPassPolicy": "Strong",
      "notes": "Added fro python",
      "customField": resourceCustomField
    }
    accountDetails.append(account1)
    account1={
      "accountName": "Priyanka",
      "password": "Priyanka@1234",
      "accountPassPolicy": "Strong",
      "notes": "Added fro python1",
      "customField": resourceCustomField
    }
    accountDetails.append(account1)
    res = resource.createAccounts(resourceId,accountDetails)
    print(res.responseMessage)
  
