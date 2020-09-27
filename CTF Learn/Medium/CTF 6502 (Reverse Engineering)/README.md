# CTF 6502 (40 Points)
Welcome to the CTF 6502 challenge!<br>
In this CTF challenge, the MOS 6502 has returned. This time it doesn't power a home video game console or computer system like the Nintendo Entertainment System or the Commodore 64.
<br>
This time it's hiding our flag! Let's travel back in time to the beginning of the home computer revolution, whip out our programming manual and get our hands dirty with some good old 6502-assembly.
<br>
Implement the missing opcode in the OPCODE_0x49-method and fix the machine code in the program-variable.
<br>
When you're done you should be able to read the flag in the memory dump at memory address 0x0040.
<br>
Good luck, I'll see you in the future!
<br>
(The Program.cs-file is attached. Run it any way you prefer. Or use .NET Fiddle to run it in your browser here: https://dotnetfiddle.net/VDGK8P)
# Solved
Mari kita cek source nya
```csharp
class Program {

    static readonly byte[] ram = new byte[0xB0];

    static readonly byte[] flag = {
        0x4B,0x5C,0x4E,0x64,0x6D,0x69,0x7A,0x66,
        0x73,0x60,0x38,0x65,0x3B,0x57,0x6B,0x38,
        0x65,0x78,0x7D,0x7C,0x3B,0x7A,0x57,0x7A,
        0x3B,0x7E,0x38,0x64,0x7D,0x7C,0x39,0x38,
        0x66,0x75
    };

    static readonly byte[] program = {
        0xa2, 0x00,                 // LDX #$00
        0xb5, 0x00,                 // LDA $00,X
        0x00, 0x00,
        0x95, 0x40,                 // STA $40,X
        0xe8,                       // INX
        0xe0, (byte)flag.Length,    // CPX #${flag.Length}
        0xd0, 0xf5,                 // BNE $0604
        0xa9, 0xff                  // LDA #$ff
    };

    public static byte OPCODE_0x49(byte value, byte accumulator) {
        return 0xFF;
    }

    static void Main(string[] args) {
        Console.WriteLine("***********************************************************************");
        Console.WriteLine("* Welcome to the CTF 6502 challenge!                                  *");
        Console.WriteLine("*                                                                     *");
        Console.WriteLine("* This 6502 assembly program should process the flag data and make it *");
        Console.WriteLine("* readable, but the data in the memory dump looks corrupted.          *");
        Console.WriteLine("* I guess there's a bug in the assembly program, or maybe in the      *");
        Console.WriteLine("* emulator? This `OPCODE_0x49`-method looks strange...                *");
        Console.WriteLine("***********************************************************************\n");

        Console.WriteLine("- Loading flag data into memory location 0x0000 ...");
        Array.Copy(flag, 0, ram, 0, flag.Length);

        Console.WriteLine("- Loading program into memory location 0x0080 ...");
        Array.Copy(program, 0, ram, 0x0080, program.Length);

        Console.WriteLine("- Setting the program counter (PC) to 0x0080 and executing program ...\n");

        var cpu = new MOS6502(ram) {
            PC = 0x80
        };

        while (cpu.PC != (0x80 + program.Length)) {
            cpu.Step();
        }

        Console.WriteLine("- Dumping memory...\n");
        DumpMemory();
    }

    // No code below this comment needs to be modified to solve the challenge.

    static void DumpMemory() {
        for (int i = 0; i < 0xB0; i += 0x10) {
            Console.Write($"0x{i:X4}  ");

            for (int j = 0; j < 0x10; j++) {
                if (j == 0x08) Console.Write(" ");
                Console.Write($"{ram[i + j]:X2} ");
            }

            Console.Write(" ");

            for (int j = 0; j < 0x10; j++) {
                var c = (char)ram[i + j];
                if (c == 0) c = '.';
                Console.Write($"{c}");
            }

            Console.WriteLine("");
        }
    }
}
```
Jika saya ekseskusi file tersebut
```
***********************************************************************
* Welcome to the CTF 6502 challenge!                                  *
*                                                                     *
* This 6502 assembly program should process the flag data and make it *
* readable, but the data in the memory dump looks corrupted.          *
* I guess there's a bug in the assembly program, or maybe in the      *
* emulator? This `OPCODE_0x49`-method looks strange...                *
***********************************************************************

- Loading flag data into memory location 0x0000 ...
- Loading program into memory location 0x0080 ...
- Setting the program counter (PC) to 0x0080 and executing program ...

- Dumping memory...

0x0000  4B 5C 4E 64 6D 69 7A 66  73 60 38 65 3B 57 6B 38  K\Ndmizfs`8e;Wk8
0x0010  65 78 7D 7C 3B 7A 57 7A  3B 7E 38 64 7D 7C 39 38  ex}|;zWz;~8d}|98
0x0020  66 75 00 00 00 00 00 00  00 00 00 00 00 00 00 00  fu..............
0x0030  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
0x0040  4B 5C 4E 64 6D 69 7A 66  73 60 38 65 3B 57 6B 38  K\Ndmizfs`8e;Wk8
0x0050  65 78 7D 7C 3B 7A 57 7A  3B 7E 38 64 7D 7C 39 38  ex}|;zWz;~8d}|98
0x0060  66 75 00 00 00 00 00 00  00 00 00 00 00 00 00 00  fu..............
0x0070  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
0x0080  A2 00 B5 00 00 00 95 40  E8 E0 22 D0 F5 A9 FF 00  ¢.µ...@èà"Ðõ©ÿ.
0x0090  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
0x00A0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  ................
```
<i>Disini saya menyelesaikan challenge ini tanpa menggunakan fungsi dari <b>OPCODE_0x49</b></i> akan tetapi saya solve menggunakan code ini
```python
flag = [
	0x4B , 0x5C , 0x4E , 0x64 , 0x6D , 0x69 , 0x7A , 0x66 ,
	0x73 , 0x60 , 0x38 , 0x65 , 0x3B , 0x57 , 0x6B , 0x38 ,
	0x65 , 0x78 , 0x7D , 0x7C , 0x3B , 0x7A , 0x57 , 0x7A ,
	0x3B , 0x7E , 0x38 , 0x64 , 0x7D , 0x7C , 0x39 , 0x38 ,
	0x66 , 0x75
]

# flag_temp = "CTF\ear^kX0]3Oc0]put3rOr3v0\ut10^m"
# flag_temp1 = "CTFlearn[H0m3?c0mput3r?r3v0lut10n]"
# flag_temp2 = "CTFlearn{X0]3Oc0]put3rOr3v0lut10n}"
# flag_temp3 = "CTFlearn[H0m3_c0mput3r_r3v0lut10n]"

res = ""

def checkCharacter(c):
    character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_@{}()-"
    if c in character:
        return True
    else: return False

for i in range(100):

    isOk = True

    for x in range(len(flag)):
        charac = str(chr(flag[x] - i))
        # if not checkCharacter(charac):
        #     isOk = False
        #     break
        # else:
        res += charac

    if isOk == True:
        print (str(i) + "." + res)
    res = ""
```
```
8.CTF\ear^kX0]3Oc0]put3rOr3v0\ut10^m
```
Disini saya mencoba membrute karakter tersebut, bertahap-tahap saya mencari teks yang masuk diakal
```
CTF\ear^kX0]3Oc0]put3rOr3v0\ut10^m => Failed
CTFlearn[H0m3?c0mput3r?r3v0lut10n] => Failed
CTFlearn{X0]3Oc0]put3rOr3v0lut10n} => Failed
CTFlearn[H0m3_c0mput3r_r3v0lut10n] => Success
```
Sebenarnya ada cara yg mudah untuk meraih flag yaitu
```python
for x in flag:
    res += chr(x ^ 8)

print res
```
```
CTFlearn{h0m3_c0mput3r_r3v0lut10n}
```
Setelah saya input flag tersebut, tidak berhasil! Disini ada 3 huruf yang berbeda yaitu
```
CTFlearn{h0m3_c0mput3r_r3v0lut10n}
CTFlearn[H0m3_c0mput3r_r3v0lut10n]

1. { => [
2. H => h
3. } => ]
```
Saya tidak tau juga kenapa salah 1 flag ini tidak dapat di input. <br>
Flag : <b>CTFlearn[H0m3_c0mput3r_r3v0lut10n]</b>