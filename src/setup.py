#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup, find_packages


setup(
        name = "aptgregator",
        version = "0.0.1",
        description = "__project_description__",
        author = "__author_name__",
        author_email = "__author_email__",
        url = "__project_url__",

        install_requires = [
            'WebCore<2.0',
            'flup',
            'jinja2',
            'IPython>=0.12',
            'psutil',
            ],
        packages = find_packages(exclude=[
            'schema'
            ]),

        zip_safe = False,
        include_package_data = True,
        package_data = {
                '': ['README.md', 'LICENSE'],
                'aptgregator': ['templates/*']
            },

        paster_plugins = ['PasteScript', 'WebCore'],
        entry_points = {
            'paste.paster_command': [
                'manage = aptgregator.commands.manage:ManageCommand',
                'admin = aptgregator.commands.admin:AdminCommand'
                ]
            }
    )
