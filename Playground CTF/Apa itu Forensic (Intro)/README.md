# Apa itu Forensic? (50 Points)
Forensic adalah salah satu ketgori CTF dimana peserta diberikan sebuah file, lalu peserta diminta untuk melakukan analisis file tersebut, misal struktur filenya, isi dari filenya, format filenya, dll, hingga peserta berhasil menemukan flag yang tersembunyi. File dapat berupa gambar, zip, pcap, dll.<br>
Coba download gambar yang terlampir, lalu coba cari flag tersembunyi pada gambar tersebut
# Solved
Jalankan command ini
```
strings kangchenjunga.jpg | grep "PlaygroundCTF{"
```
```
<rdf:li photoshop:LayerName="PlaygroundCTF{tH15_1s_f0r3ns1c5_3z}" photoshop:LayerText="PlaygroundCTF{tH15_1s_f0r3ns1c5_3z}"/> </rdf:Bag> </photoshop:TextLayers> </rdf:Description> </rdf:RDF> </x:xmpmeta>
```
Flag : <b>PlaygroundCTF{tH15_1s_f0r3ns1c5_3z}</b>
