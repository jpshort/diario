#-*- coding: utf-8 -*-

from odoo import models,fields,api

class AccountInvoice(models.Model):
    _name    = 'account.invoice'
    _inherit = 'account.invoice'
    efectivo = fields.Boolean(string="Efectivo",default=False)
 
    @api.onchange('efectivo')
    def _cambiar_diario(self):
        
        id_aux = self.journal_id

        for ids in self.partner_id:
            codigo = ids.id
            break

        domain = [('id','=',codigo)]
        partners = self.env['res.partner']
        tipo_comprobante = partners.search(domain).sale_fiscal_type
   
        if tipo_comprobante and tipo_comprobante.lower() == 'final':       
            journals = self.env['account.journal']

            if self.efectivo:
                id_needed = journals.search([('efectivo', '=', 'True')]).id  
                if not id_needed:
                    id_needed = id_aux

            else:                        
                id_needed = journals.search([('default_journal', '=', 'True')]).id	   
                if not id_needed:
                    id_needed = id_aux
        else:
            journals = self.env['account.journal']
            id_needed = journals.search([('default_journal', '=', 'True')]).id	   
            if not id_needed:
                id_needed = id_aux
             
 
        self.journal_id  = id_needed
 


class AccountJournal(models.Model):
    _name= 'account.journal'
    _inherit = 'account.journal'

    efectivo = fields.Boolean(string="Efectivo",default=False)
    default_journal = fields.Boolean(string="Diario por Defecto",default= False)    
   

class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    sale_fiscal_type = fields.Char(default = 'final')
