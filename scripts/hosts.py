#!/usr/bin/env python

import argh

# This will eventually need to get away from chef and to ansible (jwagner)
from chef import Node, autoconfigure


def hosts(env=None, name=None):
    autoconfigure()
    if name:
        nodes = (node for node in Node.list() if name in Node(node).name)
    else:
        nodes = (
            node for node in Node.list() if Node(node).chef_environment == env)

    file = open("hosts", "w")
    file.write("[hosts]\n")

    map(lambda n: file.write("{0}\n".format(Node(n)['ipaddress'])), nodes)

argh.dispatch_command(hosts)
