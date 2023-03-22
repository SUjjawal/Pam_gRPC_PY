from source import grpc_client
import socket
import ssl
from source import user_pb2
from source import util_pb2

class User:
    def __init__(self):
        frm = "user"
        self.ip_add = socket.gethostbyname(socket.gethostname())
        self.client = grpc_client.getClient(frm)
        self.card_detail = util_pb2.CertificateDetail(thumbPrint=self.client.thumbprint,
                                                          pfxPassword=self.client.password)
        

def createUser(user_name,first_name,last_name,full_name,email,policy,role,is_supper_admin,password,department,location,is_api_user,host_name,expiry_date):
    usr = User()
    usr_request = user_pb2.CreateUser(
        userName=user_name,
        firstName=first_name,
        lastName=last_name,
        fullName=full_name,
        email=email,
        policy=policy,
        role=role,
        isSupperAdmin=is_supper_admin,
        password=password,
        department=department,
        location=location,
        isApiUser=is_api_user,
        hostName=host_name,
        expiryDate=expiry_date,
        grcpUser=usr.client.cert_hostname,
        ipAddress=usr.ip_add,
        certDetail=usr.card_detail
    )
    res_reply = usr.client.stub.createUser(usr_request)
    return res_reply

def getUserId(user_name):
    usr = User()
    usr_request = user_pb2.UserName(userName=user_name,
        grcpUser=usr.client.cert_hostname,
        ipAddress=usr.ip_add,
        certDetail=usr.card_detail
    )
    res_reply = usr.client.stub.getUserId(usr_request)
    return res_reply

def deleteUser(user_id):
    usr = User()
    usr_request = user_pb2.UserID(userId=user_id,
        grcpUser=usr.client.cert_hostname,
        ipAddress=usr.ip_add,
        certDetail=usr.card_detail
    )
    res_reply = usr.client.stub.deleteUser(usr_request)
    return res_reply


