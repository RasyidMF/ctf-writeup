# Encode Encoding (60 Points)
Looks like this file is broken. Can you fix it and decode a flag? Hint: Decoders can help
# Solved
Source
```java
    package chat.client;

import java.util.HashMap;
import java.util.Random;

public class DecryptionMaster {
   private static String FLAG = "";
   private static String CFLAG = "";
   private static String pf = "";
   private static HashMap<Character, Integer> MAP = new HashMap();
   private static final char[] ALPHABET_LOWER = "abcdefghijklmnoprstuvwxyz".toCharArray();
   private static final char[] ALPHABET_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();

   private static void mapMaker() {
      for(int i = 0; i < ALPHABET_UPPER.length; ++i) {
         MAP.put(ALPHABET_UPPER[i], i);
      }

   }

   private static void secretkey() {
      Random rand = new Random();
      int random = rand.nextInt(133);

      for(int i = 0; i < 132; ++i) {
         CFLAG = CFLAG + ALPHABET_LOWER[random];
         CFLAG = CFLAG + ALPHABET_UPPER[rand.nextInt(random + 1)];
         String hex = "";

         for(int ii = 0; i < CFLAG.toCharArray().length; ++ii) {
            hex = Integer.toHexString(CFLAG.toCharArray()[ii]);
         }

         if (hex == "56645f4630625f6879335f62753561307777386973337d4a414d736c6879757b64") {
            FLAG = hex;
            CFLAG = hex;
            break;
         }
      }

   }

   private static void flagMaker() {
      for(int i = 0; i < ALPHABET_LOWER.length; ++i) {
         Random rand = new Random();
         int randomNum = rand.nextInt(0 - ALPHABET_UPPER.length + 1);
         FLAG = FLAG + ALPHABET_LOWER[(Integer)MAP.get(ALPHABET_UPPER[randomNum])];
      }

      if (FLAG == "Q2NgMzMgMzNgkjNg") {
         pf = pf + FLAG;
      } else if (FLAG == "gzMgczNgczNgAzMg" && pf.contains("Q2NgMzMgMzNgkjNg")) {
         pf = pf + FLAG;
      } else if (FLAG == "EjNgUzMgUzNgIjNg" && pf.contains("gzMgczNgczNgAzMg")) {
         pf = pf + FLAG;
      } else if (FLAG == "YWNgMzMgkzNggjNg" && pf.contains("EjNgUzMgUzNgIjNg")) {
         pf = pf + FLAG;
      } else if (FLAG == "YWNgIjNgAzMgYDNgYWNgQjNgYTNgQjNgI2NgUzNgkzNggjNgMmNgMzNgQGNgEDNgEGN" && pf.contains("YWNgMzMgkzNggjNg")) {
         pf = pf + FLAG;
      }

      if (FLAG != CFLAG) {
         flagMaker();
      }

   }

   public static void main(String[] args) {
      mapMaker();
      flagMaker();
      secretkey();
      System.out.println(FLAG);
   }
}
```
Disini setelah saya analisa bahwa fungsi dari <b>flagMaker</b> tidak memiliki fungsi sama-sekali dari challenge ini akan tetapi fungsi <b>secretKey</b> lah!. Disini saya memperhatikan Hex <b>56645f4630625f6879335f62753561307777386973337d4a414d736c6879757b64</b>
```
Vd_F0b_hy3_bu5a0ww8is3}JAMslhyu{d
```
Disini saya mengetahui bahwa flag yang terenkripsi yaitu
```
JAMslhyu{dVd_F0b_hy3_bu5a0ww8is3}
```
Kemudian saya mencari angka silang antara J -> C, adalah 7 shift. Kemudian saya demonstrasi lagi untuk karakter ke 2 bahwa hasilnya T. Kemudian karena saya tau bahwa enkripsi ini adalah <b>Caesar Cipher</b> saya menggunakan https://www.dcode.fr/caesar-cipher untuk mendapatkan flag
```
+7	CTFlearn{wOw_Y0u_ar3_un5t0pp8bl3}
```
Flag : <b>CTFlearn{wOw_Y0u_ar3_un5t0pp8bl3}</b>