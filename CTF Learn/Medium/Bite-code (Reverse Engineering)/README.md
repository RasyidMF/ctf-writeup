# Bite-code (60 Points)
I dunno what bytecode is. Could you tell me what input of 'checkNum' will return true? The flag is just a 32-bit signed integer as a decimal (nothing else.) https://mega.nz/#!qfATFaKR!zaTNExq3Bm1MjJnePjTGQyvnvLX_xZxhbGaMv_ypaxo
# Solved
Kita di berikan sebuah instruksi dari hasil compiler java
```java
public static boolean checkNum(int);
    descriptor: (I)Z
    flags: ACC_PUBLIC, ACC_STATIC
    Code:
      stack=2, locals=3, args_size=1
         0: iload_0
         1: iconst_3
         2: ishl
         3: istore_1
         4: iload_0
         5: ldc           #2                  // int 525024598
         7: ixor
         8: istore_2
         9: iload_1
        10: iload_2
        11: ixor
        12: ldc           #3                  // int -889275714
        14: if_icmpne     21
        17: iconst_1
        18: goto          22
        21: iconst_0
        22: ireturn
      LineNumberTable:
        line 3: 0
        line 4: 4
        line 5: 9
      StackMapTable: number_of_entries = 2
        frame_type = 253 /* append */
          offset_delta = 21
          locals = [ int, int ]
        frame_type = 64 /* same_locals_1_stack_item */
          stack = [ int ]
```
Convert menjadi
```java
public class HelloWorld{

     public static void main(String []args){
        int a = 525024598;
		int b = -889275714;

		for (int i = Integer.MIN_VALUE; i < Integer.MAX_VALUE; i++) {
			int s1 = (i << 3) ^ (a ^ i);
			if (s1 == b) {
				System.out.println("Result: " + i);
				break;
			}
		}
     }
}
```
```
$javac HelloWorld.java
$java -Xmx128M -Xms16M HelloWorld
Result: -1352854872
```
Flag : <b>-1352854872</b>