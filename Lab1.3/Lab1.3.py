from pysnmp.hlapi import *

snmp1 = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmp2 = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')

result = getCmd(SnmpEngine(),
                CommunityData('public', mpModel=0),
                UdpTransportTarget(('10.31.70.107', 161)),
                ContextData(),
                ObjectType(snmp1))

for i in result:
    print(i)

result2 = nextCmd(SnmpEngine(),
                  CommunityData('public', mpModel=0),
                  UdpTransportTarget(('10.31.70.107', 161)),
                  ContextData(),
                  ObjectType(snmp2), lexicographicMode=False)

for i in result2:
    print(i)