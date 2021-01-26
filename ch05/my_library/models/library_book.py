import logging
from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

logger = logging.getLogger(__name__)


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    date_release = fields.Date('Release Date')
    cost_price = fields.Float('Book Cost')
    author_ids = fields.Many2many(
        'res.partner',
        string='Authors'
    )
    category_id = fields.Many2one('library.book.category', string='Category')
    manager_remarks = fields.Text('Manager Remarks')
    old_edition = fields.Many2one('library.book', string='Old Edition')
    state = fields.Selection([
        ('draft', 'Unavailable'),
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost')],
        'State', default="draft")

    #1 定義模型方法及使用API裝飾器
    @api.model
    def is_allow_transition(self, old_state, new_state):
        allowed = [('draft', 'available'),
                   ('available', 'borrowed'),
                   ('borrowed', 'available'),
                   ('available', 'lost'),
                   ('borrowed', 'lost'),
                   ('lost', 'available')]
        return (old_state, new_state) in allowed

    def change_state(self, new_state):
        for book in self:
            if book.is_allow_transition(book.state, new_state):
                book.state = new_state
            else:
                #2 錯誤的訊息
                message = _('Moving from %s to %s is not allowed') %(book.state, new_state)
                raise UserError(message)

    def make_available(self):
        self.change_state('available')

    def make_borrowed(self):
        self.change_state('borrowed')

    def make_lost(self):
        self.change_state('lost')

    def log_all_library_members(self):
        library_member_model = self.env['library.member'] # 空
        all_members = library_member_model.search([])
        print('ALL MEMBERS:', all_members)
        return True

    #5 更新
    def change_release_date(self):
        self.ensure_one()
        self.date_release = fields.Date.today()

    #6 搜尋紀錄
    def find_book(self):
        domain = [
            '|',
                '&', ('name', 'ilike', 'Book Name'),
                    ('category_id.name', 'ilike', 'Category Name'),
                '&', ('name', 'ilike', 'Book Name 2'),
                    ('category_id.name', 'ilike', 'Category Name 2'),
        ]
        books = self.search(domain)
        logger.info('Books found: %s', books)
        return True

    #8 過濾紀錄
    def filter_books(self):
        all_books = self.search([])
        filtered_books = self.book_with_multiple_authors(all_books)
        logger.info('Filtered Books: %s', filtered_books)

    @api.model
    def book_with_multiple_authors(self, all_books):
        def predicate(book):
            if len(book.author_ids) > 1:
                return True
        return all_books.filtered(predicate)

    #9 搜尋記錄關聯
    def mapped_books(self):
        all_books = self.search([])
        books_authors = self.get_author_names(all_books)
        logger.info('Books Authors: %s', books_authors)

    @api.model
    def get_author_names(self, all_books):
        return all_books.mapped('author_ids.name')

    #10 搜尋排序
    def sort_books(self):
        all_books = self.search([])
        books_sorted = self.sort_books_by_date(all_books)
        logger.info('Books before sorting: %s', all_books)
        logger.info('Books after sorting: %s', books_sorted)

    @api.model
    def sort_books_by_date(self, all_books):
        return all_books.sorted(key='date_release') #reverse=True

    #12 繼承原生，權限不能修改欄位
    @api.model
    def create(self, values):
        if not self.user_has_groups('my_library.group_librarian'):
            if 'manager_remarks' in values:
                raise UserError(
                    'You are not allowed to add manager_remarks'
                )
        return super(LibraryBook, self).create(values)

    def write(self, values):
        if not self.user_has_groups('my_library.group_librarian'):
            if 'manager_remarks' in values:
                raise UserError(
                    'You are not allowed to modify manager_remarks'
                )
        return super(LibraryBook, self).write(values)

    #13 自定義搜尋方式
    def name_get(self):
        result = []
        for book in self:
            authors = book.author_ids.mapped('name')
            name = '%s (%s)' % (book.name, ', '.join(authors))
            result.append((book.id, name))
        return result

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = [] if args is None else args.copy()
        if not(name == '' and operator == 'ilike'):
            args += ['|', '|', '|',
                     ('name', operator, name),
                     ('isbn', operator, name),
                     ('author_ids.name', operator, name)]
            return super(LibraryBook, self)._name_search(
                name=name, args=args, operator=operator,
                limit=limit, name_get_uid=name_get_uid
            )
      
    #14 read_group
    def grouped_data(self):
        data = self._get_average_cost()
        logger.info('Grouped Data %s' %data)

    def _get_average_cost(self):
        grouped_result = self.read_group(
            [('cost_price', '!=', False)], # Domain
            ['category_id', 'cost_price:avg'], # Fields to access
            ['category_id'] # group by
        )
        return grouped_result

#3 獲取其他模型的空紀錄
class LibraryMember(models.Model):
    _name = 'library.member'
    _inherits = {'res.partner': 'partner_id'}
    _description = 'Library Member'

    partner_id = fields.Many2one('res.partner', ondelete='cascade', required=True)
    date_start = fields.Date('Member Since')
    date_end = fields.Date('Termination Date')
    member_number = fields.Char()
    date_of_birth = fields.Date('Date of Birth')

