# Running this code locally might sometimes show SSL certificates error. In that case, run this script to solve that error.

# import ssl
# import certifi
#
# print(f"Python version: {ssl.OPENSSL_VERSION}")
# print(f"Certifi version: {certifi.__version__}")
# print(f"Default cert file: {ssl.get_default_verify_paths().cafile}")
#
# try:
#     ssl.create_default_context().check_hostname = False
#     ssl.create_default_context().verify_mode = ssl.CERT_NONE
#     print("SSL context created successfully")
# except Exception as e:
#     print(f"Error creating SSL context: {e}")

# import certifi
# print(certifi.where())

# this is the code to temporarily disable SSL verification
import ssl
import socket

context = ssl.create_default_context()
with socket.create_connection(("www.google.com", 443)) as sock:
    with context.wrap_socket(sock, server_hostname="www.google.com") as ssock:
        print(ssock.version())
