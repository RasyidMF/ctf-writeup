import java.math.BigInteger;
import java.util.Base64;
import java.util.Scanner;
import java.util.Stack;

//No decompilers required!

@SuppressWarnings({"JavaDoc", "MagicNumber"})
public class SourceCode
{
    private interface A
    {
        int a();
    }

    private static final Stack<Integer> aa = new Stack<>();
    private static A oo[] = new A[Byte.MAX_VALUE];
    private static byte O[];
    private static BigInteger a = b(0);
    private static BigInteger aaa = b(256);

    public static BigInteger b(int c)
    {
        return new BigInteger("" + c);
    }

    public static BigInteger b(int off, int len)
    {
        byte[] b = new byte[len];
        System.arraycopy(O, off, b, 0, len);
        return new BigInteger(1, b);
    }

    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        oo = new A[] {
            () -> O[4] < O[3] ? e(3, 0) : e(25),
            () -> O[20] = O[0],
            () -> {aa.clear();return 0;},
            () -> e(16, 9, O[O[1] - 1], 25, 5, 19) + (O[5] = (byte)(6 + O[4])),
            () -> O[81] += (O[5] - 103 == 0 ? 5 : 0), // 0
            () -> O[6 + O[4]] = O[5],
            () -> O[O[1] - 1] ^= O[4],
            () -> e(25, 39, 24, 47, 9),
            () -> e(18, 22, 16, 50, 45, 36),
            () -> O[O[1]++] = O[5],
            () -> O[25]++,
            () -> O[25] / 3 - 1,
            () -> e(24, 25, 48, 9, 7),
            () -> e(37, 26, 35, 44, 27, 33, 18, 22, 16, 4), // First execution
            () -> O[25],
            () -> e(44, 27, 9, 0),
            () -> O[5] = O[O[5]],
            () -> O[4] == 0 ? e(41, 24, 28, 30, 23, 25, 20, 9) : e(25, 20, 9),
            () -> O[80],
            () -> O[4]++,
            () -> a.byteValue() - ((a = a.shiftRight(8)).equals(6) ? 6 : 37) + e(22),
            () -> O[5] -= O[2],
            () -> O[5] = O[0],
            () -> (a = a.modPow(b(107, 3), b(93, 14))).byteValue(),
            () -> O[2] = O[0],
            () -> O[5] = O[--O[1]],
            () -> 5,
            () -> O[4] = O[0],
            () -> O[2]--,
            () -> O[25] < O[3] ? e(46, 10, 29) : e(2),
            () -> (O[2] >= 0 ? e(22, 47, 16, 38, 28, 30) : e()) - 31,
            () -> 58 - (O[25] % 3 == 0 ? e(22, 11, 24, 47, 16, 15) : e()),
            () -> O[5] == 0 ? 0 : (O[81] = 1) - 1,
            () -> (O[4] < O[3] ? e(24, 43, 47, 16, 34, 19, 33) : e()) - 31,
            () -> e(24, 21, 32),
            () -> O[81] = O[0],
            () -> e(24, 46, 22, 48, 26, 24, 21, 18, 24, 47, 40) - 26,
            () -> O[25] < O[3] ? e(8, 10, 31, 37) : e(),
            () -> (a = a.shiftLeft(8).add(b(O[5] & 0xFF))).byteValue(),
            () -> 45,
            () -> O[80] = O[5],
            () -> O[3],
            () -> O[O[1]++] = O[0],
            () -> O[5] = O[4],
            () -> 0,
            () -> O[5] == 63 ? e(29) : e(39),
            () -> in.nextLine().length() % 2,
            () -> O[5] += O[2],
            () -> O[5] *= O[2],
            () -> e(O[5]),
            () -> O[O[25] + 6] -= (O[O[25] + 66] = O[5]) + O[80],
        };
        
        O = Base64.getDecoder().decode("AFIADgAAAXY3HR9H80AdMXvtc3EABgwHEQA/Pz8/P0J2IWdyJUlwIWYvRzBvcDhwSEhQNTFfek" +
            "lfa0c/Pz8/Pz8AAAAAAAAAAAAAAAAAAAAxAAAAAAAAAAAAAAAAkoRsQReobCuzXWhg9R8BAAEAAAAAAAAAAAAAAAAAAAAAAAA=");

        System.out.println("Sonnet Auto-Judger 3000 v0.9-BETA");
        System.out.println("Copyright (c) 2017 theKidOfArcrania\n");
        System.out.println("Enter in any sonnet, and I'll tell you how cool it is from a scale of 1 to 10.");
        
        aa.push(13);
        while (!aa.isEmpty())
            O[0] = (byte) oo[aa.pop()].a();

        int rating = O[81];
        System.out.println("Rating: " + rating);
        if (rating == 10)
        {
            System.out.println("WOW!! Your sonnet is SOO cool. Here's a message from our judge: ");
            System.out.print("flag{");
            for (int i = 0; i < 14; i++)
                System.out.print((char)O[i + 'B']);
            System.out.println("}");
        }
        else if (rating < 1)
            System.out.println("Boooo! Your sonnet succckks sooo much!");
        else
            System.out.println("Not bad... but could be better!");
    }

    public static byte e(int... c)
    {
        int i = c.length;
        while (i --> 0)
            aa.push(c[i]);
        return 37;
    }
}

/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.math.BigInteger;
import java.util.Base64;
import java.util.Scanner;
import java.util.Stack;
public class Main
{
    private interface A {
        int a();
    }
    
    private static final Stack<Integer> aa = new Stack<>();
    private static byte O[];
    private static A oo[] = new A[Byte.MAX_VALUE]; // 127
    
    public static BigInteger b(int c)
    {
        return new BigInteger("" + c);
    }
    public static BigInteger b(int off, int len)
    {
        byte[] b = new byte[len];
        System.arraycopy(O, off, b, 0, len);
        return new BigInteger(1, b);
    }
    public static byte e(int... c)
    {
        int i = c.length;
        while (i --> 0)
            aa.push(c[i]);
        return 37;
    }
    
	public static void main(String[] args) {
		System.out.println("Hello World");
		
		O = Base64.getDecoder().decode("AFIADgAAAXY3HR9H80AdMXvtc3EABgwHEQA/Pz8/P0J2IWdyJUlwIWYvRzBvcDhwSEhQNTFfeklfa0c/Pz8/Pz8AAAAAAAAAAAAAAAAAAAAxAAAAAAAAAAAAAAAAkoRsQReobCuzXWhg9R8BAAEAAAAAAAAAAAAAAAAAAAAAAAA=");
		
		e(37, 26, 35, 44, 27, 33, 18, 22, 16, 4);
            
		System.out.println(aa);
	}
}
