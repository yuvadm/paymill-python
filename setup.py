__author__ = 'yalnazov'
from setuptools import setup
setup(
    name='paymill',
    version='1.0.0',
    description='Python wrapper for PAYMILL API',
    packages=['paymill'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=['requests >= 2.1.0', 'jsonobject >= 0.4.3']
)
