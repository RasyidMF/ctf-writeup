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

