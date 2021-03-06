#!/usr/bin/env python
# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:

from setuptools import setup, find_packages

setup(
    name = "crash",
    version = "0.1",
    packages = find_packages(),
    package_data = {
        '' : [ "*.dist" "*.txt" ],
    },

    install_requires = [],

    author = "Jeff Mahoney",
    author_email = "jeffm@suse.com",
    description = "Python Linux Kernel Crash dump forensic tools",
    license = "GPL v2 only",

)
