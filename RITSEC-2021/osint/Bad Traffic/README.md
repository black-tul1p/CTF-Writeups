# Description

### Title: Bad Traffic

That APT might’ve compromised our networks. We’ve included a PCAP of suspicious activity. What tool is the APT using to steal data? (Wrap the answer in RS{})

# Solution

Looking through the packet capture file, we can see some DNS requests. Looking at the text segment of these packets, we see `group`, `passwd`, and `shadow` at the end of each DNS query. This appears to be some type of DNS exfiltration and a very popular tool used for DNS exfiltration is called DNSteal. From this, we get the flag.

### Flag

`RS{dnsteal}`
