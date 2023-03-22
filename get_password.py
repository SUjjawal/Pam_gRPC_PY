from source import resource


if __name__ == '__main__' :

    resource_id = 1201
    account_id = 1201
    reason="testing from python"
    ticket_id=30
    res = resource.getPassword(resource_id,account_id,reason,ticket_id)
    print(res.responseMessage)
  
