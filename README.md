# CSE421 – Computer Networks Lab (BRAC University)

Lab work from CSE421 : Computer Networks (Summer 2025) at BRAC University. Covers socket
programming in Python, application-layer protocol analysis in Cisco Packet
Tracer and Wireshark, network simulation with ns-3, and router
configuration, DHCP, and routing in Cisco Packet Tracer.

Each lab folder contains my solutions. Labs 01 and 02 also include the
lab's task sheet and reading materials in a `materials/` folder.

## Lab 01 – Socket Programming in Python

TCP client-server programs using Python's `socket` module. Every program
uses a fixed 64-byte header that carries the message length, followed by
the message itself, and the client sends `End` to close the connection.
[Task sheet](Lab01/materials/Lab01_Tasks.pdf) · [Reading materials](Lab01/materials/Lab01_Reading_Materials.pdf) · [Slides](Lab01/materials/Socket_Programming_Slides.pdf)

| Task | Description | Files |
|------|-------------|-------|
| 1 | **Client info:** the client sends its device name and IP address when it connects, and the server prints them | [server1.py](Lab01/task1_client_info/server1.py) · [client1.py](Lab01/task1_client_info/client1.py) |
| 2 | **Vowel counter:** the server counts the vowels in each message and replies "Not enough vowels", "Enough vowels I guess", or "Too many vowels" | [server2.py](Lab01/task2_vowel_counter/server2.py) · [client2.py](Lab01/task2_vowel_counter/client2.py) |
| 3 | **Multi-threaded vowel counter:** the same server, handling several clients at once with one thread per connection | [server.py](Lab01/task3_multithreaded_vowel_counter/server.py) · [client1.py](Lab01/task3_multithreaded_vowel_counter/client1.py) · [client2.py](Lab01/task3_multithreaded_vowel_counter/client2.py) |
| 4 | **Salary calculator:** the client sends hours worked, and the server replies with the salary (Tk 200/hour up to 40 hours, then Tk 8000 + Tk 300 for each extra hour) | [server4.py](Lab01/task4_salary_calculator/server4.py) · [client4.py](Lab01/task4_salary_calculator/client4.py) |

**How to run:** start the server, then the client in a second terminal on the same machine.

```bash
python3 server2.py
python3 client2.py
```

## Lab 02 – Packet Analysis and Network Simulation

[Reading materials](Lab02/materials/Lab02_Reading_Materials.pdf)

| Task | Description | Report |
|------|-------------|--------|
| 1 | **HTTP, SMTP, and POP3 in Cisco Packet Tracer:** captured a web request and an email exchange in simulation mode, and examined the PDUs of the HTTP request/response and the SMTP and POP3 messages | [Report](Lab02/task1_packet_tracer_http_smtp_pop3_report.pdf) · [Task sheet](Lab02/materials/task1_http_smtp_pop3.pdf) |
| 2 | **Packet analysis with Wireshark:** captured live traffic, filtered HTTP packets, and explained an HTTP request and response layer by layer (HTTP, TCP ports/flags/sequence numbers, IPv4, Ethernet) | [Report](Lab02/task2_wireshark_packet_analysis_report.pdf) · [Task sheet](Lab02/materials/task2_wireshark_packet_analysis.pdf) |
| 3 | **Network simulation with ns-3:** a two-node point-to-point network with a UDP echo client and server, extended with FlowMonitor to measure throughput and delay. Ran it with four packet sizes (132, 1255, 2310, and 5521 bytes) and graphed packet size against throughput | [first.cc](Lab02/first.cc) · [Report](Lab02/task3_ns3_report.pdf) · [Task sheet](Lab02/materials/task3_ns3_introduction.pdf) |

## Lab 03 – Basic Router Configuration and DHCPv4

| Activity | Description | Files |
|----------|-------------|-------|
| Basic router configuration | Cabled a two-router network, erased and reloaded the routers, then configured hostnames, passwords, a message-of-the-day banner, and the Ethernet and serial interfaces, and verified connectivity | [Lab with answers](Lab03/basic_router_configuration.pdf) · [Packet Tracer file](Lab03/basic_router_configuration.pka) |
| Configuring DHCPv4 using Cisco IOS | Configured a router as a DHCPv4 server with address pools and excluded addresses | [Packet Tracer file](Lab03/dhcpv4_using_cisco_ios.pka) |
| Configuring DHCPv4 using a DHCP server | Configured a dedicated server to hand out addresses through DHCPv4 | [Packet Tracer file](Lab03/dhcpv4_using_dhcp_server.pka) |

## Lab 04 – Static Routing and RIPv2

| Activity | Description | Files |
|----------|-------------|-------|
| IPv4 static and default routes | Configured recursive and directly attached static routes and a default route, then verified connectivity | [Instructions](Lab04/static_and_default_routes_instructions.pdf) · [Packet Tracer file](Lab04/static_and_default_routes.pka) |
| Floating static routes | Configured IPv4 and IPv6 floating static routes as backup paths and tested failover | [Instructions](Lab04/floating_static_routes_instructions.pdf) · [Packet Tracer file](Lab04/floating_static_routes.pka) |
| RIPv2 | Configured the RIPv2 dynamic routing protocol | [Packet Tracer file](Lab04/ripv2.pka) |

The `.pka` files open in **Cisco Packet Tracer**.

## Tools
Python 3 · Cisco Packet Tracer · Wireshark · ns-3 (C++)
