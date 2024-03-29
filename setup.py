#!/usr/bin/python

# -------------------------------------------------------------------
# MIT License
#
# Copyright (c) 2010-2021 Denis MACHARD
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -------------------------------------------------------------------

import setuptools

VERSION="1.5.0"

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
 
KEYWORDS = ('extensiveautomation automation testautomation testing plugin')
    
setuptools.setup(
    name="extensiveautomation_plugin_gui",
    version=VERSION,
    author="Denis MACHARD",
    author_email="d.machard@gmail.com",
    description="GUI plugin for extensiveautomation server",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://www.extensiveautomation.org/",
    package_dir  = {'': 'src'},
    packages = setuptools.find_packages('src'),
    include_package_data=True,
    platforms='any',
    keywords=KEYWORDS,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance"
    ],
    install_requires=[
                       "extensiveautomation_server",
                       "selenium"
                     ]
)
