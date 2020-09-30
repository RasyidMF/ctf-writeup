# Monthly Expenses (50 Points)
Untuk hitung pengeluaran bulanan lebih mudah menggunakan spreadsheet :)
<br>
Pembuat Soal: n080e
# Solved
Diberikan sebuah teks
```
DiskoCTF{
Expenses
Lodging,$6.11
Motor Vehicle,$4.92
Insurance,$6914.04
Depreciation,$704.40
Property Tax,$1.07
Heating,$8.46
Software Licenses,$6.67
Security Alarm,$435.02
Office Supplies,$43.34
Cooling,$6.53
Entertainment,$6.29
Mortgage Interest,$52.69
Bank Fees,$6744.99
Gas,$9.72
Electricity,$2.13
Phone,$99
}
```
Steganography yang digunakan adalah <b>Spreadsheet</b>, Untuk mengdecode nya saya menggunakan url ini https://www.spammimic.com/spreadsheet.php?action=decode
```
Your spreadsheet Expenses Lodging,$6.11 Motor Vehicle,$… decodes to:
DiskoCTF{secret_alias_rahasia}
```
Flag : <b>DiskoCTF{secret_alias_rahasia}</b>
