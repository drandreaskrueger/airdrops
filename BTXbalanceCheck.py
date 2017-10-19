#!env/py3/bin/python3

'''
Created on 19 Oct 2017

@author: andreas
'''

from __future__ import print_function

import requests # pip install requests
from lxml import html # pip install lxml
import click # pip install click


def BTXcheck(address):
    """
    queries bitcore.cc/check.php
    and returns 0 if there is an "alert alert-danger = empty address
    or returns the BTC value at the BTX snapshot block
    """
    
    url="https://bitcore.cc/claim.php#"
    data={"check" : address}
    r=requests.post(url, data)
    
    # print (r.content)
    # print (r.text)
    
    tree = html.fromstring(r.content)

    node = tree.xpath('//div[@class="alert alert-danger"]' )
    if len(node):
        return 0.0
    
    node = tree.xpath('//input[@name="amount"]' )
    value = node[0].attrib['value']
    
    return float(value)
    

def iterateAddresses(filename):
    with open(filename) as f:
        addresses=f.readlines()

    for addr in addresses:
        addr=addr.strip()
        print (addr, BTXcheck(addr))


@click.command()
@click.option('--address', '-a', help='Single bitcoin address (then --file is ignored).')
@click.option('--file', '-f', default="addresses.txt", help='File with addresses, one per line.')

def CLI(file, address):
    if address:
        print (address, BTXcheck(address))
    elif file:
        iterateAddresses(file)

if __name__ == '__main__':
    CLI()
    