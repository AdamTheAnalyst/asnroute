from scapy.all import *
from datetime import datetime
import sys
import requests
import json


API_KEY = "ce96c02f576e0387c4d4297b25c93f91"

class ASNRouteClient():

    def __init__(self):

        pass

    def geoip_lookup(self, ip):

        r = requests.get(
            "http://api.ipstack.com/{}".format(
                ip
            ),
            params={
                "access_key": API_KEY,
                "format": 1,
                "hostname": 1
            })
        return r.json()

    def as_lookup(self, ip):

        r = requests.get(
            "https://api.iptoasn.com/v1/as/ip/{}".format(
                ip
            )
        )
        return r.json()

    def format_result(self, hop_ip, geoip, asn):

        if (asn["announced"]):
            return {
                "ip": hop_ip,
                "hostname": geoip["hostname"],
                "country_name": geoip["country_name"],
                "country_code": geoip["country_code"],
                "as_announced": asn["announced"],
                "as_description": asn["as_description"],
                "as_country_code": asn["as_country_code"],
                "as_number": asn["as_number"],
                "first_ip": asn["first_ip"],
                "last_ip": asn["last_ip"]
            }

        else:

            return {
                "ip": hop_ip,
                "hostname": geoip["hostname"],
                "country_name": geoip["country_name"],
                "country_code": geoip["country_code"],
                "as_announced": asn["announced"],
            }

    def trace(self, target, port):

        print("[*] Tracing {} on port {}".format(target, port))

        result, unans = sr(
            IP(dst=target, ttl=(1, 10)) / TCP(dport=port, flags="S"),
            verbose=1
        )

        results = {
            "time": str(datetime.now()),
            "target": target,
            "port": port,
            "hops": {}
        }

        for snd, rcv in result:

            print(snd.ttl, rcv.src, snd.sent_time, rcv.time)

            if snd.ttl != 1:
                if str(rcv.src) == results["hops"][snd.ttl-1]["ip"]:
                    break

            results["hops"][snd.ttl] = self.format_result(
                rcv.src,
                self.geoip_lookup(rcv.src),
                self.as_lookup(rcv.src)
            )

        print(json.dumps(results, indent=4))

if __name__ == "__main__":

    client = ASNRouteClient()
    if len(sys.argv) != 3:
        print("{} <ip address/domain> <port>".format(__file__))
        sys.exit(1)
    client.trace(sys.argv[1], int(sys.argv[2]))