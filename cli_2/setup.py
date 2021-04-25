from setuptools import setup
setup(
    name = 'cli_2',
    version = '0.1.0',
    packages = ['cli_2'],
    entry_points = {
        'console_scripts': [
            'cli_2 = cli_2.__main__:main'
        ]
    })