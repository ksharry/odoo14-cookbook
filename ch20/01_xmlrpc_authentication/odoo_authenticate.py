from xmlrpc import client

server_url = 'http://localhost:8069'
db_name = 'odoo'
username = 'odoo'
password = '213aa7dd283b40337c5f5dcbe88af9b0817c5e82'

common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
user_id = common.authenticate(db_name, username, password, {})

if user_id:
    print("Success: User id is", user_id)
else:
    print("Failed: wrong credentials")