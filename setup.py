from setuptools import setup, find_packages
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='social-commerce',
version='0.0.3',
description='Django project template using pinax and satchmo',
author='Harley Bussell',
author_email='modmac@gmail.com',
url='http://github.com/hbussell/social-commerce-project',
classifiers=[
  "License :: OSI Approved :: GNU General Public License (GPL)",
  "Programming Language :: Python",
  "Development Status :: 4 - Beta",
  "Intended Audience :: Developers",
  "Framework :: Django",
  "Environment :: Console",
  "Topic :: Software Development",
  "Topic :: System :: Software Distribution"

],
keywords='pinax-project',
zip_safe=False,
license='GPL',
install_requires=[
'setuptools',
],
packages = find_packages(),
include_package_data = True,
)
