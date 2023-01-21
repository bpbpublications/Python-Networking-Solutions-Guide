from pysnmp.hlapi import *

host = "10.10.10.1"
snmp_community = "public"
snmp_oid = "1.3.6.1.4.1.9.2.1.8.0"

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData(snmp_community, mpModel=1),
           UdpTransportTarget((host, 161)),
           ContextData(),
           ObjectType(ObjectIdentity(snmp_oid)),     )      )

for oid, val in varBinds:
    print(oid.prettyPrint()," - ", val.prettyPrint())
