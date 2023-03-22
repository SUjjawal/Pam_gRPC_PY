from source import resource


if __name__ == '__main__' :

    resource_id = 1202
    account_id = 1504
    res = resource.deleteAccount(resource_id,account_id)
    print(res.responseMessage)
  
