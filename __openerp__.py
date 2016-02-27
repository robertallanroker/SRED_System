# -*- coding: utf-8 -*-
{
    'name': "sred_system",

    'summary': """
        Makes many modifcations and updates to core system and
        implements a new module for an SRED Services provider.
        """,

    'description': """
        Green Light Inovations Partners has developed a new module that allows SRED,
        Service providers to manage work loads and collaborate easier with clients.
        We modify projects module so that specialized SRED tracking is in place which
        in turn allows new or existing odoo customers to receive eligable refunds from the
        Canadian government for thier RD efforts.
    """,

    'author': "Green Light Innovation Partnes",
    'website': "http://www.GreenLightIP.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Projects, SRED, Applications, Canada',

    'version': '3.0',
    'sequence': 11,

    # any module necessary for this one to work correctly
    'depends': ['web',
        'base',                     ## Primary Base Libraries
        'base_setup',               ## Primary Base Setup



        'calendar',                 ## Everyone needs a calendar
        'project',                  ## Basic Project Management and Tasks
        'crm',
        'account',                  ## Accounting Core
        'account_accountant',
        'analytic',                 ## CRM wont work without Analytics
        'board',                    ## Dashboards
        'gamification',             ## Have fun with goals
        'google_calendar',          ## Google Calendar Integration - Very Buggy
        'google_drive',
        'mail',
        'resource',
        'document',



        'association',



        'hr',
        'hr_recruitment',
        'hr_payroll',
        'hr_timesheet_sheet',

        'marketing_campaign',
        'mass_mailing',
        'link_tracker',
        'membership',
        'survey',
        'survey_crm',


        'note',
        'portal',
#       'subscription',


        'web_analytics',
        'web_editor',
        'web_kanban',
        'web_settings_dashboard',
        'web_kanban_gauge',
        'web_diagram',
        'web_diagram',
        'portal_gamification',
        'web_planner',



        'website',
        'website_google_map',
        'website_event',
        'website_hr',
        'website_livechat',
        'website_mail',
        'website_mail_channel',
        'website_slides',
        'website_blog',
        'website_form',
        'website_forum',
        'website_blog',
        'website_portal',
        'website_twitter',
        'website_forum_doc',


        'bus',                          ## Instant Messaging, send messages to other users
        'im_livechat',
#

        'l10n_multilang'],
    #'js': ['static/src/js/view_list.js'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
  #      'fixes/fix_im_chat_bug.xml',
        'data/load_data/load_data.xml',
        'modifications/to_views/view_reorganize.xml',
        'views/sred_system.xml',
        'views/views.xml',
        'views/view_work_folders.xml',
        'views/view_contracts.xml',
        'views/view_sred_claim.xml',
        'views/view_menus.xml',
        'reports/templates.xml',
   #      'views/mail_templates.xml'
        'modifications/to_views/mods_to_crm_leads.xml',
        'modifications/to_views/mods_to_res_partner.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'load_demo_data/demo.xml',


    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}