# -*- coding: utf-8 -*-
# 9. 新增設定是否自行租借書籍

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_self_borrow = fields.Boolean(string="Self borrow", implied_group='my_library.group_self_borrow')
