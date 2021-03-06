import os
from setuptools import setup
import buysafe

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()
VERSION = buysafe.__version__

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-buysafe',
    version=VERSION,
    packages=['buysafe'],
    include_package_data=True,
    install_requires=['django'],
    license='BSD License',
    description='Django wrapper for SunTech BuySafe (TM).',
    long_description=README,
    url='http://github.com/uranusjr/django-buysafe',
    author='Tzu-ping Chung',
    author_email='uranusjr@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
