# InvoiceLines/__manifest__.py
{
    'name': 'Invoice Lines Customization',
    'version': '1.0',
    'summary': 'Adds custom fields and structure to invoice lines.',
    'description': 'This module customizes invoice lines by adding fields such as color, meters, VAT, and computes custom amounts.',
    'author': 'Fredrick Mwenda(Basam)',
    'website': 'https://servolltech.co.ke',
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'views/invoice_line_views.xml',
        'views/report_invoice_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

