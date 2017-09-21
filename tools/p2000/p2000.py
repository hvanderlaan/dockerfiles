#!/usr/bin/env python

""" p2000.py - p2000 pager api script """

from __future__ import print_function

import sys
import re
import argparse
import ConfigParser

try:
    from libp2000 import libp2000
except ImportError:
    sys.stderr.write('[-] could not find libp2000.\n')
    sys.exit(1)

def main(conf):
    """ main function """
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--region', help='security region', default='40')
    parser.add_argument('-l', '--lines', help='number of lines', default='5')
    args = parser.parse_args()

    numlines = args.lines
    url = conf.get('global', 'baseurl') + conf.get('regions', 'region' + args.region)

    # color schema
    fdp = '\033[38;5;9m'
    lfl = '\033[38;5;118m'
    ems = '\033[38;5;220m'
    pdp = '\033[38;5;39m'
    cgd = '\033[38;5;208m'
    rst = '\033[0m'

    data = libp2000.get_p2000_data(url)
    p2000data = libp2000.convert_to_json(data)

    for _ in xrange(int(numlines)):
        if re.match('Ambulance', str(p2000data['p2000'][_]["call_type"])):
            col = ems
        elif re.match('Brandweer', str(p2000data['p2000'][_]["call_type"])):
            col = fdp
        elif re.match('Lifeliner', str(p2000data['p2000'][_]["call_type"])):
            col = lfl
        elif re.match('Politie', str(p2000data['p2000'][_]["call_type"])):
            col = pdp
        else:
            col = cgd

        print('{}{} - {}'. format(col, p2000data['p2000'][_]["date"],
                                  p2000data['p2000'][_]["call_type"]))
        print('{}{}' .format(col, p2000data['p2000'][_]["message"]))
        for i in xrange(len(p2000data['p2000'][_]['called'])):
            print('{}{}' .format(col, p2000data['p2000'][_]['called'][i]))

        print('{}' .format(rst))

if __name__ == "__main__":
    CONF = ConfigParser.ConfigParser()
    CONF.read('p2000.cfg')

    if CONF.get('global', 'refresh') == 'true':
        try:
            while True:
                os.system('clear')
                main(CONF)
                time.sleep(int(CONF.get('global', 'refreshtime')))
        except KeyboardInterrupt:
            sys.exit(0)
    else:
        main(CONF)

    sys.exit(0)
