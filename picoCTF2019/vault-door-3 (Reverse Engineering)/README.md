# vault-door-3 - Points: 200
<b>Description : </b>This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java<br>
<b>Hints : </b>Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.
# Solved
The source we need to reverse the string with specfici alogrithm
```java
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm11ga4e_u_4_m9rf48");
    }
```
i solve this challenge using <b>Java</b> code
```java
public class HelloWorld{

     public static void main(String []args){
        System.out.println("Hello World");
        
        String password = "jU5t_a_sna_3lpm11ga4e_u_4_m9rf48";
        char[] buffer = new char[32];
        
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        
        String s = new String(buffer);
        System.out.println(s);
        
     }
}
```
Flag : <b>picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_e9af18}</b>