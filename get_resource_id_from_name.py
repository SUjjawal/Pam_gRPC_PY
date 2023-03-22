from source import resource


if __name__ == '__main__' :
    resource_name = "ujjawal7"
    res = resource.getResourceIDFromName(resource_name)
    print(res.responseMessage)
  
