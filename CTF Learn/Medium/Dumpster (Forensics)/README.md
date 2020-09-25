# Dumpster (60 Points)
I found a flag, but it was encrypted! Our systems have detected that someone has successfully decrypted this flag, and we stealthily took a heap dump of the program (in Java). Can you recover the flag for me? Here's the source code of the Java program and the heap dump: https://mega.nz/#!rHYGlAQT!48DlH2pSZg10Ei3f-Ivm7RoNBbV16Qw0wN4cWxANUwY
# Solved
Diberikan sebuah code
```java
import java.security.MessageDigest;
import java.util.Arrays;
import java.util.Base64;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class Decryptor
{
	public static final String FLAG = "S+kUZtaHEYpFpv2ixuTnqBdORNzsdVJrAxWznyOljEo=";
	private static class Password
	{
		private byte[] passHash;

		public Password(char[] pass) throws Exception
		{
			MessageDigest digest = MessageDigest.getInstance("SHA-256");
			this.passHash = Arrays.copyOf(digest.digest(new String(pass).getBytes("UTF-8")), 16);
		}
		
		public byte[] encrypt(byte[] msg) throws Exception
		{
			SecretKeySpec spec = new SecretKeySpec(passHash, "AES");
			Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
			cipher.init(Cipher.ENCRYPT_MODE, spec);
			return cipher.doFinal(msg);
		}
		
		public byte[] decrypt(byte[] msg) throws Exception
		{
			SecretKeySpec spec = new SecretKeySpec(passHash, "AES");
			Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
			cipher.init(Cipher.DECRYPT_MODE, spec);
			return cipher.doFinal(msg);
		}
	}
	
	public static void main(String[] args) throws Exception
	{
		Password pass = new Password(System.console().readPassword("Enter password to decrypt flag: "));
		System.out.println(new String(pass.decrypt(Base64.getDecoder().decode(FLAG.getBytes()))));
		Thread.sleep(5000); //We did a heap dump right here.
	}
}
```
Untuk mengdecode Flag dibutuhkan Password, seperti deskripsi yang dikatakan bahwa passwordnya berada di <b>heapdump.hprof</b> dan ini yang saya dapatkan
```java
byte[] pass = {
	7, 95, -34, 16, -89, -86, 73, 108, -128, 71, 43, 41, 100, 40, 53, -24
};
```
Jika sudah mendapatkan password nya, mari kita decode flagnya
```java
import java.security.MessageDigest;
import java.util.Arrays;
import java.util.Base64;

import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
public class HelloWorld
{
     public static void main(String []args)
     {
         try {
            String FLAG = "S+kUZtaHEYpFpv2ixuTnqBdORNzsdVJrAxWznyOljEo=";
            byte[] pass = {
    	        7, 95, -34, 16, -89, -86, 73, 108, -128, 71, 43, 41, 100, 40, 53, -24  
    	    };
    	    SecretKeySpec spec = new SecretKeySpec(pass, "AES");
    		Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
    		cipher.init(Cipher.DECRYPT_MODE, spec);
    		
    		byte[] r = cipher.doFinal(Base64.getDecoder().decode(FLAG.getBytes()));
    		System.out.println(new String(r));
         } catch (Exception ex) {
             
         }
    }
}
```
```
$javac HelloWorld.java
$java -Xmx128M -Xms16M HelloWorld
stCTF{h34p_6ump5_r_c00l!11!!}
```
Flag : <b>stCTF{h34p_6ump5_r_c00l!11!!}</b>