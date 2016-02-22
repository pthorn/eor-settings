import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = [
]

setup(
    name='eor-settings',
    version='0.0.1',
    description='A settings library',
    long_description='',
    classifiers=[
        "Programming Language :: Python",
    ],
    author='p.thorn.ru@gmail.com',
    author_email='p.thorn.ru@gmail.com',
    url='https://github.com/pthorn/eor-settings',
    keywords='web wsgi bfg pylons pyramid',
    packages=find_packages('.', exclude=['test*']),
    tests_require=['nose2'],
    test_suite="nose2.collector.collector",
    include_package_data=True,
    zip_safe=True,
    install_requires=requires,
)
