from source import grpc_client
import socket
import ssl
from source import resource_pb2
from source import util_pb2
import json

class Resource:
    def __init__(self):
        frm = "resource"
        self.ip_add = socket.gethostbyname(socket.gethostname())
        self.client = grpc_client.getClient(frm)
        self.card_detail = util_pb2.CertificateDetail(thumbPrint=self.client.thumbprint,
                                                          pfxPassword=self.client.password)


def createResource(resource_name,resource_type,account_name,pass_word,notes,resource_password_policy,account_password_policy,is_privatekey_enabled,
                   location,department,dns_name,domain_name,resource_desc,resource_url,owner_name,resource_custom_field,account_custom_field) :
    res = Resource()
    resource_custom = []
    for custom_field in resource_custom_field:
        resFie = util_pb2.FieldMap(customLabel=custom_field['customLabel'], customValue=custom_field['customValue'])
        resource_custom.append(resFie)

    account_custom = []
    for custom_field in resource_custom_field:
        resFie = util_pb2.FieldMap(customLabel=custom_field['customLabel'], customValue=custom_field['customValue'])
        account_custom.append(resFie)
    
    res_request = resource_pb2.CreateRequest(resourceName=resource_name, 
                                             resourceType=resource_type,
                                             accountName=account_name,
                                             passWord=pass_word, 
                                             notes=notes, 
                                             resourcePasswordPolicy=resource_password_policy,
                                             accountPasswordPolicy=account_password_policy,
                                             isPrivatekeyEnabled=is_privatekey_enabled,
                                             location=location,
                                             department=department,
                                             dnsName=dns_name,
                                             domainName=domain_name,
                                             resourceDesc=resource_desc,
                                             resourceUrl=resource_url,
                                             ownerName=owner_name,
                                             grcpUser=res.client.cert_hostname,
                                             ipAddress=res.ip_add,
                                             resourceCustomField=resource_custom,
                                             accountCustomField=account_custom,
                                             certDetail=res.card_detail)
 
    res_reply = res.client.stub.createResource(res_request)
    return res_reply


def getResourceIDFromName(resource_name):
    res = Resource()
    res_request = resource_pb2.GetResourceIDReq(resourceName=resource_name,
                                             ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.getResourceIDFromName(res_request)
    return res_reply

def editResource(resource_Id,resource_name,resource_desc,dns_name,location,department,resource_url,resource_type,owner_name,resource_password_policy,resource_custom_field) :
    res = Resource()
    resource_custom = []
    for custom_field in resource_custom_field:
        resFie = util_pb2.FieldMap(customLabel=custom_field['customLabel'], customValue=custom_field['customValue'])
        resource_custom.append(resFie)

    res_request = resource_pb2.EditRequest(resourceId=resource_Id,
                                             resourceName=resource_name, 
                                             resourceDesc=resource_desc,
                                             resourceType=resource_type,
                                             resPasswordPolicy=resource_password_policy,
                                             location=location,
                                             department=department,
                                             dnsName=dns_name,
                                             resourceUrl=resource_url,
                                             ownerName=owner_name,
                                             grcpUser=res.client.cert_hostname,
                                             ipAddress=res.ip_add,
                                             resourceCustomField=resource_custom,
                                             certDetail=res.card_detail)
    print(res_request)
    res_reply = res.client.stub.editResource(res_request)
    return res_reply

def deleteResource(resource_id) :
    res = Resource()
    res_request = resource_pb2.DeleteRequest(resourceId=resource_id,
                                             ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.deleteResource(res_request)
    return res_reply

def getResources():
    res = Resource()
    res_request = resource_pb2.GetResourceRequest(ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.getResources(res_request)
    return res_reply

def getAllResourceTypes(org_name,resource_type):
    res = Resource()
    resource_custom = []
    for type in resource_type:
        res_type = resource_pb2.ResourceTypeArray(resourceType=type['resourceType'])
        resource_custom.append(res_type)
   
    res_request = resource_pb2.ResourceTypes(orgName=org_name,
                                             ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             resourceType=resource_custom,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.getResources(res_request)
    return res_reply

def getResIdAccId(resource_name,account_name):
    res = Resource()
    res_request = resource_pb2.ResourceIdAccountId(resourceName=resource_name,
                                             accountName=account_name,
                                             ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.getResIdAccId(res_request)
    return res_reply

def getResourceAccountList(resource_id):
    res = Resource()
    res_request = resource_pb2.ResAccountList(resourceId=resource_id,
                                             ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.getResourceAccountList(res_request)
    return res_reply

def getAccountAttributes(resource_id,account_id):
    res = Resource()
    res_request = resource_pb2.AccountDetail(resourceId=resource_id,
                                             accountId=account_id,
                                             ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.getAccountAttributes(res_request)
    return res_reply

def getPassword(resource_id,account_id,reason,ticket_id):
    res = Resource()
    res_request = resource_pb2.AccountPassword(resourceId=resource_id,
                                             accountId=account_id,
                                             reason=reason,
                                             ticketId=ticket_id,
                                             ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.getPassword(res_request)
    return res_reply

def createAccounts(resource_id,account_details):
    res = Resource()
    account_detail_array = []
    for accounts in account_details:
        resource_custom_field=accounts['customField']
        resource_custom = []
        for custom_field in resource_custom_field:
            custFie = util_pb2.FieldMap(customLabel=custom_field['customLabel'], customValue=custom_field['customValue'])
            resource_custom.append(custFie)

        resFie = resource_pb2.AccountMap(accountName=accounts['accountName'],
                                         password=accounts['password'],
                                         accountPassPolicy=accounts['accountPassPolicy'],
                                         notes=accounts['notes'],
                                         customField=resource_custom
                                         )
        
        account_detail_array.append(resFie)

    res_request = resource_pb2.CreateAccount(resourceId=resource_id,
                                             accountDetails=account_detail_array,
                                             ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.createAccounts(res_request)
    return res_reply

def editAccount(resource_id,account_id,accounts):
    res = Resource()
    resource_custom_field=accounts['customField']
    resource_custom = []
    for custom_field in resource_custom_field:
        custFie = util_pb2.FieldMap(customLabel=custom_field['customLabel'], customValue=custom_field['customValue'])
        resource_custom.append(custFie)

    resFie = resource_pb2.AccountMap(accountName=accounts['accountName'],
                                        password=accounts['password'],
                                        accountPassPolicy=accounts['accountPassPolicy'],
                                        notes=accounts['notes'],
                                        customField=resource_custom
                                        )
    

   
    res_request = resource_pb2.EditAccount(resourceId=resource_id,
                                             accountId=account_id,
                                             accountDetails=resFie,
                                             ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.editAccount(res_request)
    return res_reply

def deleteAccount(resource_id,account_id):
    res = Resource()
    res_request = resource_pb2.AccountDetail(resourceId=resource_id,
                                             accountId=account_id,
                                             ipAddress=res.ip_add,
                                             grcpUser=res.client.cert_hostname,
                                             certDetail=res.card_detail)
    
    res_reply = res.client.stub.deleteAccount(res_request)
    return res_reply



