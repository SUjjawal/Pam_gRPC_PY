from source import resource


if __name__ == '__main__' :

    resourceCustomField = []
    resourceCustomFieldObj = {'customLabel':'Age', 'customValue':'60'}
    resourceCustomField.append(resourceCustomFieldObj)
    resourceCustomFieldObj1 = {'customLabel':'Class', 'customValue':'23'}
    resourceCustomField.append(resourceCustomFieldObj1)
    print(resourceCustomField)
    resourceId=1202
    accountId=1504
    accountDetails = []

    account1={
      "accountName": "Praveen",
      "password": "Praveen@1234",
      "accountPassPolicy": "Strong",
      "notes": "Added fro python",
      "customField": resourceCustomField
    }

    accountDetails.append(account1)
    print(accountDetails)
    res = resource.editAccount(resourceId,accountId,account1)
    print(res.responseMessage)
  
