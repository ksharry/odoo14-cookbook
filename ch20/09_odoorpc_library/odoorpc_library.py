import odoorpc

db_name = 'odoo'
user_name = 'odoo'
password = '213aa7dd283b40337c5f5dcbe88af9b0817c5e82'

# Prepare the connection to the server
odoo = odoorpc.ODOO('localhost', port=8069)
odoo.login(db_name, user_name, password)  # login

# User information
user = odoo.env.user
print(user.name)             # name of the user connected
print(user.company_id.name)  # the name of user's company
print(user.email)            # the email of usser

BookModel = odoo.env['library.book']
search_domain = ['|', ['name', 'ilike', 'book'], ['name', 'ilike', 'sql']]
books_ids = BookModel.search(search_domain, limit=5)
for book in BookModel.browse(books_ids):
    print(book.name, book.date_release)

# create the book and update the state
book_id = BookModel.create({'name': 'Test book', 'state': 'draft'})
print("Book state before make_available:", book.state)
book = BookModel.browse(book_id)
book.make_available()
book = BookModel.browse(book_id)
print("Book state before make_available:", book.state)