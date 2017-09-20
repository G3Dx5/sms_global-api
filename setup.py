import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
]

tests_require = [
    'pytest',
    'pytest-cov',
]

setup(
    name='sms_global',
    version='0.1',
    description='SMS Interaction ',
    long_description=README, 
    classifiers=[
        'Programming Language :: Python',
    ],
    author='Gabe',
    author_email='',
    url='',
    keywords='sms api',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'sms_global = sms_global.script:main',
        ],
    },
)
