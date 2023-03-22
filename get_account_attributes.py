from source import resource


if __name__ == '__main__' :

    resource_id = 1201
    account_id = 1201
    res = resource.getAccountAttributes(resource_id,account_id)
    print(res.responseMessage)
  
