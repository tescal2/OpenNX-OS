#!/usr/bin/env python

import sys

def getRouter(rtr):
   router1 = {'os_version':'3.1.1','hostname':'nyc_router1','model':'Nexus 9372PX-E', \
   'domain':'cisco.com','mgmt_ip':'10.10.16.07'}
   router2 = dict( os_version='3.2.1', hostname='rtp_router2',model='Nexus 9372PX-E', \
   	domain='cisco.com', mgmt_ip='10.03.19.14')
   router3 = dict( os_version='3.1.1', hostname='ROUTER3',model='Nexus 9504', \
   	domain='lab.cisco.com', mgmt_ip='10.06.25.90')
   
   router_list = [router1,router2,router3]
   for router in router_list:
       if rtr == router['hostname']:
           return router
   return 'No router found.'

if __name__ == "__main__":

    args = sys.argv

    #print args

    result1 = getRouter(args[1])
    
    print 'HOSTNAME:', result1['hostname']

    value = args[2]

    print value.upper() + ': ' + result1[value]

#Darius Made A Change
