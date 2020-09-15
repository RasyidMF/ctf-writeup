# vault-door-4 - Points: 250
<b>Description : </b>This vault uses ASCII encoding for the password. The source code for this vault is here: VaultDoor4.java<br>
<b>Hints : </b>Use a search engine to find an "ASCII table". You will also need to know the difference between octal, decimal, and hexademical numbers.
# Solved
Lets check the source
```java
import java.util.*;

class VaultDoor4 {
    public static void main(String args[]) {
        VaultDoor4 vaultDoor = new VaultDoor4();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // I made myself dizzy converting all of these numbers into different bases,
    // so I just *know* that this vault will be impenetrable. This will make Dr.
    // Evil like me better than all of the other minions--especially Minion
    // #5620--I just know it!
    //
    //  .:::.   .:::.
    // :::::::.:::::::
    // :::::::::::::::
    // ':::::::::::::'
    //   ':::::::::'
    //     ':::::'
    //       ':'
    // -Minion #7781
    public boolean checkPassword(String password) {
        byte[] passBytes = password.getBytes();
        byte[] myBytes = {
            106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
            0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
            0142, 0131, 0164, 063 , 0163, 0137, 067 , 0141,
            '1' , 'c' , '8' , 'c' , '6' , '6' , '8' , 'b' ,
        };
        for (int i=0; i<32; i++) {
            if (passBytes[i] != myBytes[i]) {
                return false;
            }
        }
        return true;
    }
}

```
We can see function <b>checkPassword</b> help us to get the flag, but before that we must convert that byte into string so i using python script to do this
```python
flag = [
    106 , 85, 53, 116, 95, 52, 95, 98,
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
    98, 89, 116, 51 , 115, 95, 55 , 97,
    '1' , 'c' , '8' , 'c' , '6' , '6' , '8' , 'b' ,
]
r = ""
for x in flag:
    t = type(x)
    if t == int:
        r += chr(x)
    elif t == str:
        r += x

print ("picoCTF{" + r + "}")
```
Flag : <b>picoCTF{jU5t_4_bUnCh_0f_bYt3s_7a1c8c668b}</b>
