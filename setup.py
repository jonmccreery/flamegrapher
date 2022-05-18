from setuptools import setup, find_packages
from os import path

setup(
    name='flamegrapher',
    version=0.1,
    description='A flamegraph generator in python',
    authon='Jon McCreery',
    license='MIT',
    packages=find_packages(),

    install_requires=[
        '',
    ],
    entry_points={
        'console_scripts': ['flamegrapher=flamegrapher:main']
    }
)
