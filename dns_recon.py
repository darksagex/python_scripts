#!/bin/python3
import dns.resolver
import sys

# Define DNS record types to query
record_types = ["A", "AAAA","NS","MX","CNAME","PTR","TXT","SOA"]

# Handle missing domain argument
try:
    domain = sys.argv[1]
except IndexError:
    print("Syntax Error - python3 dns_tool_v2.py <domain_name>")
    sys.exit(1)


for record in record_types:
    try:
        print(f"\n{record} records for {domain}")
        print("-" * 20)

        answer = dns.resolver.resolve(domain, record)
        for server in answer:
            print(server.to_text())
    except dns.resolver.NoAnswer:
        print("No result was found")
    except dns.resolver.LifetimeTimeout:
        print("The search timed out")
    except dns.resolver.NoNameservers:
        print(f"No nameserver responded for {domain} with {record} record")
    except KeyboardInterrupt:
        print("Escaping")
        sys.exit(0)
    except dns.resolver.NXDOMAIN:
        print(f"{domain} does not exist")
        sys.exit(1)

