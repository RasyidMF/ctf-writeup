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
