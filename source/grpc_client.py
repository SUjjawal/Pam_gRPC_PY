from jproperties import Properties
from OpenSSL import crypto

import grpc
from source import resource_pb2_grpc
from source import user_pb2_grpc
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

class ClientData:
    def __init__(self,frm):
        conf_path = 'D:\\GRPCProj\\grpc.conf'
        configs = Properties()

        with open(conf_path, 'rb') as config_file:
            configs.load(config_file)

        server = configs.get('ServerName').data
        port = configs.get('ServerPort').data
        self.server = server + ":" + port
        self.servercert = configs.get('server_cert').data
        self.clientcert = configs.get('client_cert').data
        self.clientkey = configs.get('client_key').data
        self.password = configs.get('KeyStorePassword').data
        server_ca_cert, client_cert, client_key = prepare_certs(self.servercert, self.clientcert, self.clientkey)
    

        #x509_cert = crypto.load_certificate(crypto.FILETYPE_PEM, client_cert)
        #self.cert_hostname = x509_cert.get_subject().CN
        cert = x509.load_pem_x509_certificate(client_cert, default_backend())
        fingerprint = cert.fingerprint(hashes.SHA1())
        cN_name = cert.subject.get_attributes_for_oid(NameOID.COMMON_NAME)
        self.cert_hostname = cN_name[0].value
        self.thumbprint = fingerprint.hex()
        
        creds = grpc.ssl_channel_credentials(root_certificates=server_ca_cert, private_key=client_key, certificate_chain=client_cert)
        channel = grpc.secure_channel(self.server, creds)
        if(frm=="resource") :
            self.stub = resource_pb2_grpc.ResourceStub(channel)
        else :
            self.stub = user_pb2_grpc.UserStub(channel)
        
       
       

def prepare_certs(server_cert=None, client_key=None, client_ca=None):
    if server_cert is not None:
        with open(server_cert, 'rb') as f:
            server_cert = f.read()
    if client_key is not None:
        with open(client_key, 'rb') as key:
            client_key = key.read()
    if client_ca is not None:
        with open(client_ca, 'rb') as ca:
            client_ca = ca.read()
    return server_cert, client_key, client_ca


def getClient(frm):
    client = ClientData(frm)
    return client