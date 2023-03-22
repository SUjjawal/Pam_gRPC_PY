from source import resource


if __name__ == '__main__' :

    resource_id = 1202
    res = resource.getResourceAccountList(resource_id)
    print(res.responseMessage)
  
