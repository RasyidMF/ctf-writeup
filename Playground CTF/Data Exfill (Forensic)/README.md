# Data Exfil (50 Points)
None
# Solved
File yang di beri adalah
```
pcapng capture file - version 1.0
```
Saya menggunakan Wireshark untuk membaca hasil capture tersebut. Pastikan di filter <b>http</b> dan scroll kebawah sampai melihat request
```
100	101.066572547	10.0.2.2	10.0.2.15	HTTP	452	GET /admin.php?password=sniff_my_passwd&cmd=cat%20flag.txt HTTP/1.1
103	101.093452660	10.0.2.15	10.0.2.2	HTTP	83	HTTP/1.1 200 OK  (text/html)
```
Pada capture tersebut terdapat hasil dari request <b>/admin.php?password=sniff_my_passwd&cmd=cat%20flag.txt</b>
```
Frame 103: 83 bytes on wire (664 bits), 83 bytes captured (664 bits) on interface any, id 0
Linux cooked capture
Internet Protocol Version 4, Src: 10.0.2.15, Dst: 10.0.2.2
Transmission Control Protocol, Src Port: 8000, Dst Port: 52919, Seq: 129, Ack: 397, Len: 27
[2 Reassembled TCP Segments (155 bytes): #102(128), #103(27)]
Hypertext Transfer Protocol
    HTTP/1.1 200 OK\r\n
        [Expert Info (Chat/Sequence): HTTP/1.1 200 OK\r\n]
        Response Version: HTTP/1.1
        Status Code: 200
        [Status Code Description: OK]
        Response Phrase: OK
    Host: localhost:8000\r\n
    Connection: close\r\n
    X-Powered-By: PHP/7.0.27-1\r\n
    Content-type: text/html; charset=UTF-8\r\n
    \r\n
    [HTTP response 1/1]
    [Time since request: 0.026880113 seconds]
    [Request in frame: 100]
    [Request URI: http://localhost:8000/admin.php?password=sniff_my_passwd&cmd=cat%20flag.txt]
    File Data: 27 bytes
Line-based text data: text/html (1 lines)
    Bootcamp{data_exf1ltration}
```
Ada beberapa cara yang mudah untuk mengambil flag nya yaitu menggunakan
```
strings sniff.pcapng | grep "{.*}"
```
Flag : <b>Bootcamp{data_exf1ltration}</b>
