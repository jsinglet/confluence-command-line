from setuptools import setup

with open('README.md') as f:
    long_description = ''.join(f.readlines()[1:]).strip()

setup(
    name='confluence-command-line',
    long_description=long_description,
    version='0.3',
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
