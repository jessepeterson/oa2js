from setuptools import setup, find_packages

setup(
    name='oa2js',
    version='0.0.1',
    url='https://github.com/jessepeterson/os2as',
    author='Jesse Peterson',
    author_email='nobody@example.com',
    description='OpenAPI component schema to JSON schema converter.',
    packages=find_packages(),
    install_requires=['PyYAML'],
    entry_points={
        'console_scripts': [
            'oa2js=oa2js.oa2js:main'
        ]
    },
)
