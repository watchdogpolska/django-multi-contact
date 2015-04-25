import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-multi-contact',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='Django-multi-contact is a simple Django app to conduct contact form.',
    long_description=README,
    url='http://github.com/watchdogpolska/multi-contact/',
    author='Adam Dobrawy',
    author_email='naczelnik@jawnosc.tk',
    zip_safe=False,
    install_requires=[
        'django',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
