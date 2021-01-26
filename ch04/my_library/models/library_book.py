from odoo import models, fields, api
from datetime import timedelta

#14.抽象模型
class BaseArchive(models.AbstractModel):
    _name = 'base.archive'
    _description = 'Abstract Archive'

    active = fields.Boolean(default=True)

    def do_archive(self):
        for record in self:
            record.active = not record.active

class LibraryBook(models.Model):
    #1 模型
    _name = 'library.book'
    _inherit = ['base.archive']   #14
    _description = 'Library Book'
    _order = 'date_release desc, name'
    _rec_name = 'short_name'
    name = fields.Char('Title', required=True)
    category_id = fields.Many2one('library.book.category')
    short_name = fields.Char('Short Title',translate=True, index=True)
    notes = fields.Text('Internal Notes')
    state = fields.Selection(
        [('draft', 'Not Available'),
        ('available', 'Available'),
        ('lost', 'Lost')],
        'State', default="draft")
    #2 新增欄位
    description = fields.Html('Description', sanitize=True, strip_style=False)
    cover = fields.Binary('Book Cover')
    out_of_print = fields.Boolean('Out of Print?')
    date_release = fields.Date('Release Date')
    date_updated = fields.Datetime('Last Updated')
    author_ids = fields.Many2many('res.partner', string='Authors')
    pages = fields.Integer('Number of Pages',
        groups='base.group_user',
        states={'lost': [('readonly', True)]},
        help='Total book page count', company_dependent=False)
    reader_rating = fields.Float(
        'Reader Average Rating',
        digits=(14, 4), # Optional precision (total, decimals),
        )
    cost_price = fields.Float('Book Cost', digits='Book Price')  #3 小數位數
    currency_id = fields.Many2one(    #4 貨幣字段
        'res.currency', string='Currency')
    retail_price = fields.Monetary(
        'Retail Price',
        # optional: currency_field='currency_id',
    )
    publisher_id = fields.Many2one(    #5 關聯欄位m2o
        'res.partner', string='Publisher',
        # optional:
        ondelete='set null',
        context={},
        domain=[],
    )
    age_days = fields.Float(     
        string='Days Since Release',
        compute='_compute_age',   #8
        inverse='_inverse_age',
        search='_search_age',
        store=False, # optional
        compute_sudo=False # optional
     )
    publisher_id = fields.Many2one(
        'res.partner', string='Publisher')
    publisher_city = fields.Char(
        'Publisher City',
        related='publisher_id.city',   #9 related_fields
        readonly=True)

    ref_doc_id = fields.Reference(     #10 reference_fields
        selection='_referencable_models',
        string='Reference Document')

    active = fields.Boolean('Active', default=True)

    def name_get(self):
        result = []
        for record in self:
            rec_name = "%s (%s)" % (record.name, record.date_release)
            result.append((record.id, rec_name))
        return result

    #7 條件判斷方式1
    _sql_constraints = [
        ('name_uniq', 'UNIQUE(name)', 'Book title must be unique.'),
        ('positive_page', 'CHECK(pages>0)', 'No. of pages must be positive')
    ]

    #7 條件判斷方式2
    @api.constrains('date_release')
    def _check_release_date(self):
        for record in self:
            if record.date_release and record.date_release > fields.Date.today():
               raise models.ValidationError('Release date must be in the past')

    #8 計算天數
    @api.depends('date_release')
    def _compute_age(self):
        today = fields.Date.today()
        for book in self:
            if book.date_release:
                delta = today - book.date_release
                book.age_days = delta.days
            else:
                book.age_days = 0
     
    #8 計算欄位
    def _inverse_age(self):
        today = fields.Date.today()
        for book in self.filtered('date_release'):
            d = today - timedelta(days=book.age_days)
            book.date_release = d
 
    #8 計算欄位的搜尋
    def _search_age(self, operator, value):
        today = fields.Date.today()
        value_days = timedelta(days=value)
        value_date = today - value_days
        # age_days > value -> date < value_date
        operator_map = {
            '>': '<', '>=': '<=',
            '<': '>', '<=': '>=',
        }
        new_op = operator_map.get(operator, operator)
        return [('date_release', new_op, value_date)]

    #10 關聯的模型
    @api.model
    def _referencable_models(self):
        models = self.env['ir.model'].search([
            ('field_id.name', '=', 'message_ids')])
        return [(x.model, x.name) for x in models]

    #11 第一種繼承
    class ResPartner(models.Model):
        _inherit = 'res.partner'
        _order = 'name'
        published_book_ids = fields.One2many(   #5.o2m
            'library.book', 'publisher_id',
            string='Published Books')
        authored_book_ids = fields.Many2many(   #5.m2m
             'library.book',
             string='Authored Books',
             # relation='library_book_res_partner_rel' # optional
         )
        count_books = fields.Integer( 'Number of Authored Books',
        compute='_compute_count_books' )

    @api.depends('authored_book_ids')
    def _compute_count_books(self):
        for r in self:
            r.count_books = len(r.authored_book_ids)

    #13 第三種代理繼承,可以同步
    class LibraryMember(models.Model):
        _name = 'library.member'
        _inherits = {'res.partner': 'partner_id'}
        partner_id = fields.Many2one(
            'res.partner',
            ondelete='cascade')
        date_start = fields.Date('Member Since')
        date_end = fields.Date('Termination Date')
        member_number = fields.Char()
        date_of_birth = fields.Date('Date of birth')
    

