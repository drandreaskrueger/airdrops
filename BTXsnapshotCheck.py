#!env/py3/bin/python3

'''
              airdrops/BTXsnapshotCheck.py
              
@summary:     queries bitcore.cc/check.php for BTX snapshot balance

@author:      Andreas Krueger
@see:         https://github.com/drandreaskrueger/airdrops
@contact:     https://bitcointalk.org/index.php?action=profile;u=860710
@license:     MIT license + donationware, see README.md
@since:       Created on 19 Oct 2017
@version:     v0.1.0
'''

from __future__ import print_function # so it runs identically in Python 2

import requests # pip install requests    # web queries
from lxml import html # pip install lxml  # parsing html DOM
import click # pip install click          # command line interface


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
    """
    for each line in filename call the balance checker
    """
    with open(filename) as f:
        addresses=f.readlines()

    for addr in addresses:
        addr=addr.strip()
        print (addr, BTXcheck(addr))


@click.command()
@click.option('--address', '-a', help='Single bitcoin address (then --file is ignored).')
@click.option('--file', '-f', default="addresses.txt", help='File with addresses, one per line.')
def CLI(file, address):
    """
    command line interface
    """
    if address:
        print (address, BTXcheck(address))
    elif file:
        iterateAddresses(file)


if __name__ == '__main__':
    CLI()
    
    
    