# Recklinghausen (20 Points)
This is the 4th in a series of Beginner Reversing Challenges. If you are new to Reversing, you may want to solve Reykjavik, then Riyadh then Rangoon before solving this challenge. This is a 20 point challenge and is different in two ways from the previous 10 point challenges. Once you get into gdb, b *main+offset is your friend! Good Luck!
<br>
Once you solve the challenge you can use the flag to decrypt the souces.zip.enc file provided, if you are interested in seeing the source programs used to create the challenge.
<br>
The readme file includes some online resources if you are new to Reversing and Assembler.
# Solved
Mari kita cek source nya
```cpp
    else if ( (unsigned __int8)CheckMsg((const char *)v4->m128i_i64) )
    {
      GetMessage(buffer, 6u);
      sub_10D0(1LL, "%s : %s\n", buffer, v4);
      if ( ~(strlen((const char *)v4->m128i_i64) + 1) == -35LL )
      {
        v5 = _mm_loadu_si128(v4);
        v6 = _mm_cmpgt_epi8((__m128i)0LL, v5);
        v7 = _mm_unpacklo_epi8(v5, v6);
        v8 = _mm_unpackhi_epi8(v5, v6);
        v9 = _mm_loadu_si128(v4 + 1);
        v10 = _mm_cmpgt_epi8((__m128i)0LL, v9);
        v11 = _mm_unpacklo_epi8(v9, v10);
        v12 = _mm_unpackhi_epi8(v9, v10);
        v13 = _mm_cmpgt_epi16((__m128i)0LL, v8);
        v14 = _mm_unpacklo_epi16(v8, v13);
        v15 = _mm_unpackhi_epi16(v8, v13);
        v16 = _mm_cmpgt_epi16((__m128i)0LL, v7);
        v17 = _mm_add_epi32(
                _mm_add_epi32(v15, v14),
                _mm_add_epi32(_mm_unpackhi_epi16(v7, v16), _mm_unpacklo_epi16(v7, v16)));
        v18 = _mm_cmpgt_epi16((__m128i)0LL, v11);
        v19 = _mm_cmpgt_epi16((__m128i)0LL, v12);
// Dan lain-lain
```
Jika kita menjalankan <b>ltrace</b> kita hanya didapatkan <b>2 Exit Error Code</b> yaitu
```
1 dan 7
```
Sebelum itu saya mengecheck isi dari fungsi <b>CheckMsg</b> untuk mendapatkan pesan-pesan yang telah terenkripsi
```cpp
_int64 __fastcall CheckMsg(const char *a1)
{
  __int64 v1; // r8
  __int64 result; // rax
  __int64 v3; // rax

  __asm { endbr64 }
  v1 = strlen_0();
  result = 0LL;
  if ( (unsigned __int8)msg5 == v1 )
  {
    if ( msg5 )
    {
      v3 = 0LL;
      while ( byte_50E2[v3] == ((unsigned __int8)byte_50E1 ^ a1[v3]) )
      {
        if ( (unsigned __int8)msg5 <= (int)++v3 )
          goto LABEL_8;
      }
      result = 0LL;
    }
    else
    {
LABEL_8:
      result = 1LL;
    }
  }
  return result;
}
```
```
.data:00000000000050E1 byte_50E1       db 7Eh
.data:00000000000050E2 ; _BYTE byte_50E2[46]
.data:00000000000050E2 byte_50E2       db 3Dh, 2Ah, 38h, 12h, 1Bh, 1Fh, 0Ch, 10h, 5, 2Ch, 0Bh
.data:00000000000050E2                                         ; DATA XREF: GetMessage(char *,uint)+AB3↑o
.data:00000000000050E2                                         ; CheckMsg(char const*)+2E↑o
.data:00000000000050E2                 db 16h, 0Ch, 18h, 1Bh, 0Dh, 0Ah, 0Dh, 0Eh, 17h, 1Bh, 12h
.data:00000000000050E2                 db 1Bh, 21h, 38h, 1Bh, 0Dh, 0Ah, 17h, 8, 1Fh, 12h, 3, 0Dh
```
Bisa kita lihat instruksi pada
```cpp
byte_50E2[v3] == ((unsigned __int8)byte_50E1 ^ a1[v3])
```
Teks yang terenkripsi adalah hasil encoded <b>XOR</b>, saya mengdecode menggunakan python script
```python
byte_50E2 = [
    0x3D, 0x2A, 0x38, 0x12, 0x1B, 0x1F, 0x0C, 0x10, 0x5, 0x2C, 0x0B,
    0x16, 0x0C, 0x18, 0x1B, 0x0D, 0x0A, 0x0D, 0x0E, 0x17, 0x1B, 0x12,
    0x1B, 0x21, 0x38, 0x1B, 0x0D, 0x0A, 0x17, 0x8, 0x1F, 0x12, 0x3
]

r = ""

for x in byte_50E2:
    r += chr(x ^ 0x7E)

print r
```
```
CTFlearn{Ruhrfestspiele_Festival}
```
Saya mencoba input flag ini ternyata benar, saya kira fake :3<br>
Flag : <b>CTFlearn{Ruhrfestspiele_Festival}</b>