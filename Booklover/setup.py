from setuptools import setup, find_packages

setup(
    name='booklover',
    version='1.0.0',
    url='https://github.com/clbelle/DS5100-hw09',
    author='fbv2ub',
    author_email='fbv2ub@virginia.edu',
    description='collects and stores the names of books read by individuals',
    packages=find_packages(),    
    install_requires=['pandas >= 1.1.5']
)
