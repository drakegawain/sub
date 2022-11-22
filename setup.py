
from setuptools import setup, find_packages
from sub.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='sub',
    version=VERSION,
    description='Simple freezz',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Thales',
    author_email='thales.souzalopes@gmail.com',
    url='https://github/drakegawain/subzero',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'sub': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        sub = sub.main:main
    """,
)
