import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='beefish',
    version="0.1.2",
    description='simple file encryption using pycrypto',
    long_description=readme,
    author='Mohan Sha',
    author_email='mohansha@outlook.com',
    url='http://github.com/MohanSha/beefish/',
    py_modules=['beefish'],
    install_requires=['pycrypto'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    scripts = ['beefish.py'],
)
