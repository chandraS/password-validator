from setuptools import setup, find_packages

NAME = "password_validator"
VERSION = "0.0.1"
DESCRIPTION = 'Password validator to check input password against Digital Identity Guidelines'

REQUIRES = [
    'pytest==5.4.3',
	'setuptools>=40.0',
]

classifiers = [
	'Programming Language :: Python :: 3',
	'License :: MIT License'
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author_email="chandra.shikhar@gmail.com",
    url="https://github.com/chandraS",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["*.tests", "tests", "tests.*"]),
    scripts=[],
	license='MIT',
	keywords='password_validator',
	classifiers = classifiers,
	entry_points={
        'console_scripts': [
            'password_validator = main:main',
        ],
    }

)
