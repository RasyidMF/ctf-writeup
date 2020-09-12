# Expr Or Call (25 Points)
Adakah jalan (commands) menuju bendera diantara alat dynamic debuggers ?
P.S: Akan sangat disayangkan bila soal ini di-solve menggunakan Decompiler , such waste time :)
Pembuat Soal: malwareslayer
# Solved
Break point pada address <b>0x000000000800120f</b>, kemudian jalankan command ini
```
jump flag # 0x0000000008001162 in flag ()
```
Dan akan mendapatkan pesan
```
Continuing at 0x8001154.
DiskoCTF{when_there's_symbols_why_should_disassemble_it?}

Program received signal SIGSEGV, Segmentation fault.
```
Flag : <b>DiskoCTF{when_there's_symbols_why_should_disassemble_it?}</b>
