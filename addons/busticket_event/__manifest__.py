{
    'name': 'Bus Ticket Event',
    'version': '1.0',
    'category': 'Event Management',
    'author': 'Your Name',
    'depends': ['event'],
    'data': [
        'views/event_registration_view.xml',

        'report/event_registration_report.xml',
        'report/event_event_templates.xml',

    ],
    'assets': {
        'web.assets_backend': [
            # '/busticket_event/static/src/scss/event_badge_ticket_report_pdf.scss',
            # '/busticket_event/static/src/scss/style.css',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}

