from setuptools import setup, find_packages

setup(
    name='mediacenterd',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/cohoe/mediacenterd',
    license='LICENSE.txt',
    author='Grant Cohoe',
    author_email='grant@grantcohoe.com',
    description='Media Center Daemon',
    install_requires=[
        'PyRIC @ git+https://github.com/cohoe/PyRIC@master',
        'flask-restx'
    ]
)
