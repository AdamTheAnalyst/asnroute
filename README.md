# ASNRoute

A slightly unreliable script for tcp tracerouting to a host, then resolving ASN and GeoIP data for each hop along the path.

I like this for tracking changes in bgp routes between me and high profile hosts. Some interesting ones to try tracing in different countries are wikileaks.org and www.torproject.org.

## Usage

Note: You will have to add an IPStack.com API key to API_KEY in asnroute.py before running.

Usage:

    pip install -r requirements.txt
    ./asnroute.py <ip address/domain> <port>

Note: Sometimes the script will hang if the ttl is set to over 10, and you will need to ctrl+c out of it to get the output. If you can fix this raise a PR.


## Example

    (env) C02V402XHTD7:asnroute adambradbury$ python ./asnroute.py wikileaks.org 80
    [*] Tracing wikileaks.org on port 80
    Begin emission:
    Finished sending 10 packets.

    Received 151 packets, got 10 answers, remaining 0 packets
    1 10.245.0.1 1568099169.702303 1568099169.706412
    2 89.197.176.25 1568099169.7103438 1568099169.714666
    3 172.21.31.48 1568099169.717906 1568099169.7262871
    4 195.66.224.109 1568099169.724848 1568099169.729152
    5 195.66.225.9 1568099169.732502 1568099169.737409
    6 31.169.49.181 1568099169.739564 1568099169.75964
    7 195.35.109.53 1568099169.7470348 1568099169.768418
    8 195.35.109.53 1568099169.755392 1568099169.774035
    {
        "time": "2019-09-10 08:06:12.813063",
        "target": "wikileaks.org",
        "port": 80,
        "hops": {
            "1": {
                "ip": "10.245.0.1",
                "hostname": null,
                "country_name": null,
                "country_code": null,
                "as_announced": false
            },
            "2": {
                "ip": "89.197.176.25",
                "hostname": "89-197-176-25.virtual1.co.uk",
                "country_name": "United Kingdom",
                "country_code": "GB",
                "as_announced": true,
                "as_description": "VIRTUAL1",
                "as_country_code": "GB",
                "as_number": 47474,
                "first_ip": "89.197.0.0",
                "last_ip": "89.197.255.255"
            },
            "3": {
                "ip": "172.21.31.48",
                "hostname": null,
                "country_name": null,
                "country_code": null,
                "as_announced": false
            },
            "4": {
                "ip": "195.66.224.109",
                "hostname": "linx1-lond-thn.virtual1.co.uk",
                "country_name": "United Kingdom",
                "country_code": "GB",
                "as_announced": false
            },
            "5": {
                "ip": "195.66.225.9",
                "hostname": "195.66.225.9",
                "country_name": "United Kingdom",
                "country_code": "GB",
                "as_announced": false
            },
            "6": {
                "ip": "31.169.49.181",
                "hostname": "te-0-0-0-5.ncs-dpu-osl.blix.com",
                "country_name": "Norway",
                "country_code": "NO",
                "as_announced": true,
                "as_description": "BLIX",
                "as_country_code": "NO",
                "as_number": 50304,
                "first_ip": "31.169.48.0",
                "last_ip": "31.169.55.255"
            },
            "7": {
                "ip": "195.35.109.53",
                "hostname": "wikileaks.org",
                "country_name": "Norway",
                "country_code": "NO",
                "as_announced": true,
                "as_description": "BLIX",
                "as_country_code": "NO",
                "as_number": 50304,
                "first_ip": "195.35.109.0",
                "last_ip": "195.35.109.255"
            }
        }
    }
