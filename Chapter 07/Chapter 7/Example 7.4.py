from pysnmp.hlapi import *

host = "10.10.10.1"
snmp_community = "public"
snmp_oid = ["1.3.6.1.4.1.9.2.2.1.1.20.1","1.3.6.1.4.1.9.2.2.1.1.20.2"]

for id in snmp_oid:
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(snmp_community, mpModel=1),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(id)),
               )
    )

    for oid, val in varBinds:
        print(oid.prettyPrint()," - ", val.prettyPrint())
