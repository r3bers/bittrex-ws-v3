#!/usr/bin/python

from setuptools import setup, find_packages

install_requires = \
    [
        'websockets>=4.0.1',
        'signalr-client-aio>=0.0.1.6.1'
    ]

setup(
    name='bittrex-ws-v3',
    version='0.0.0.4.0',
    author='Mikhail Solovjov',
    author_email='mike@solovjov.net',
    license='MIT',
    url='https://github.com/r3bers/bittres-ws-v3',
    packages=find_packages(exclude=['tests*']),
    install_requires=install_requires,
    description='The unofficial Python websocket (AsyncIO) client for the Bittrex Cryptocurrency Exchange v3',
    download_url='https://github.com/r3bers/bittres-ws-v3.git',
    keywords=['bittrex', 'bittrex-signalr', 'orderbook', 'trade', 'bitcoin', 'ethereum', 'BTC', 'ETH', 'client',
              'websocket', 'exchange', 'crypto', 'currency', 'trading', 'async', 'aio'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ]
)
