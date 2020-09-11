# shark on wire 1 - Points: 150
<b>Description : </b>We found this packet capture. Recover the flag. You can also find the file in /problems/shark-on-wire-1_0_13d709ec13952807e477ba1b5404e620.<br>
<b>Hints : </b>Try using a tool like Wireshark, What are streams?
# Solved
What is PCAP ? PCAP is short for packet capture. It is not clear from the question if you are asking about the files with pcap extension or PCAP in general as API for capturing network traffic.<br>
To do this im using <b>Wireshark</b> download at https://www.wireshark.org/download.html<br>
After we load file <b>capture.pcap</b>, we will see there is alot packet transferred / sent including TCP / UDP / ARP / etc..<br>
When i want to search for flags using filter HTTPS / searching strings "picoCTF" not exists. So i decide to read protocol UDP by
```
Right click at UDP Protocol -> Follow -> UDP Stream
```
in first section / stream (4) this is what i got
```
fjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdnfjdsakf;lankeflksanlkfdn
```
I'm realized and remember about Hints saying <b>What are streams?</b>. After that i switch to stream (5) and this is what i got
```
picopicopicopico
```
stream (6)
```
picoCTF{StaT31355_636f6e6e}
```
stream (7)
```
picoCTF{N0t_a_fLag}
```
I try input flag in stream (6), and the result success. stream (7) probably <b>Fake Flag</b><br>
Flag : <b>picoCTF{StaT31355_636f6e6e}</b>
