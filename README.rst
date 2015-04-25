=====
django-multi-contact
=====

Django-multi-contact is a simple Django app to conduct contact form. Visitor can select recipient from address book. Address book was managed by django admin.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "contact" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'contact',
    ]

2. Include the django-multi-contact URLconf in your project urls.py like this::

    url(r'^contact/', include('contact.urls')),

3. Run `python manage.py migrate` to create the django-mulit-contact models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to manage a address book (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/contact/ to send emails.
