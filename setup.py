from setuptools import setup

setup(
    name='confluence-command-line',
    version='0.1',
    entry_points = {
        'console_scripts': ['ccl=confluencecommandline.confluence_command_line:main'],
    },
    packages=['confluencecommandline',
              'confluencecommandline.commands'],
    url='https://github.com/jsinglet/confluence-command-line',
    license='MIT',
    author='John L. Singleton',
    author_email='jsinglet@gmail.com',
    install_requires=[
          'PyYAML',
          'requests',
          'urllib3'
    ],
    description='Confluence Command Line (ccl) is a suite of command line utilities designed to make working with confluence faster and easier. '
)
