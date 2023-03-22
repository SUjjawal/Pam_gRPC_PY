from source import resource


if __name__ == '__main__' :

    resourceTypes = []
    resourceTypeObj = {'resourceType':'Windows'}
    resourceTypes.append(resourceTypeObj)
    res = resource.getAllResourceTypes("MSP",resourceTypes)
    print(res.responseMessage)
  
