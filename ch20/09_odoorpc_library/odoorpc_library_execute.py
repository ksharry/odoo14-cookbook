import odoorpc

db_name = 'odoo'
user_name = 'odoo'
password = '213aa7dd283b40337c5f5dcbe88af9b0817c5e82'

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8069)
odoo.login(db_name, user_name, password)  # login

books_info = odoo.execute('library.book', 'search_read',
    [['name', 'ilike', 'odoo']], ['name', 'date_release'])
print(books_info)