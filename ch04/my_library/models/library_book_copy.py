from odoo import models, fields, api
 
class LibraryBookCopy(models.Model):
    _name = 'library.book.copy'  
    _inherit = 'library.book'     #12
    _description = "Library Book's Copy"
