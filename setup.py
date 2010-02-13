from setuptools import setup, find_packages
import os
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='social-commerce',
version='0.0.6',
description='Django project template using pinax and satchmo',
author='Harley Bussell',
author_email='modmac@gmail.com',
url='http://github.com/hbussell/social-commerce-project',
classifiers=[
  "License :: OSI Approved :: MIT License",
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
license='MIT',
install_requires=[
'setuptools',
],
packages = find_packages(),
include_package_data = True,
)
