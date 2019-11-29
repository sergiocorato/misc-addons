# -*- coding: utf-8 -*-
{
    'name': 'Email confirmation on sign up (CRM extension)',
    'summary': 'Automatically creates a lead for every new user',
    'version': '10.0.1.0.0',
    'author': 'IT-Projects LLC',
    'website': "https://it-projects.info",
    'license': 'LGPL-3',
    "price": 10.00,
    "currency": "EUR",
    'depends': [
        'auth_signup_confirmation',
        'crm',
    ],
    'installable': True,
}
