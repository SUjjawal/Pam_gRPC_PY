from source import resource


if __name__ == '__main__' :

    resourceCustomField = []
    resourceCustomFieldObj = {'customLabel':'Age', 'customValue':'38'}
    resourceCustomField.append(resourceCustomFieldObj)
    resourceCustomFieldObj1 = {'customLabel':'Class', 'customValue':'8'}
    resourceCustomField.append(resourceCustomFieldObj1)
    print(resourceCustomField)

    accountCustomField =[]
    resourceCustomFieldObj = {'customLabel':'Hello', 'customValue':'Hello'}
    resourceCustomField.append(resourceCustomFieldObj)
    resourceCustomFieldObj1 = {'customLabel':'Hello1', 'customValue':'Hello1'}
    resourceCustomField.append(resourceCustomFieldObj1)
    resourceCustomFieldObj2 = {'customLabel':'Hello2', 'customValue':'Hello2'}
    resourceCustomField.append(resourceCustomFieldObj2)

    res = resource.createResource("Ujjawal13","Windows","Rahul12","Rohit@123","testing","Strong","Strong",True,"chennai","PMP","ujjawal-0040",None,"resource Desc",None,None,resourceCustomField,accountCustomField)
    #resource_name,resource_type,account_name,pass_word,notes,resource_password_policy,account_password_policy,is_privatekey_enabled,
    #               location,department,dns_name,domain_name,resource_desc,resource_url,owner_name
    print(res.responseMessage)
  
