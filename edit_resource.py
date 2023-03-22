from source import resource


if __name__ == '__main__' :

    resourceCustomField = []
    resourceCustomFieldObj = {'customLabel':'Age', 'customValue':'878'}
    resourceCustomField.append(resourceCustomFieldObj)
    resourceCustomFieldObj1 = {'customLabel':'Class', 'customValue':'28'}
    resourceCustomField.append(resourceCustomFieldObj1)
    print(resourceCustomField)

    resource_Id=1204
    resource_name="Sarkar421"
    resource_desc="Updated from Python"
    dns_name="sarkar-3333"
    location="Rachi"
    department="SDP"
    resource_url=None
    resource_type="Linux"
    owner_name="Hari"
    resource_password_policy="Strong"
    resource_custom_field=resourceCustomField

    res = resource.editResource(resource_Id,resource_name,resource_desc,dns_name,location,department,resource_url,resource_type,owner_name,resource_password_policy,resource_custom_field)
    print(res.responseMessage)
  
