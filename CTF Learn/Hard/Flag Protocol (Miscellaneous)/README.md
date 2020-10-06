# Flag Protocol (70 Points)
This one is all about actually CAPTURING the flag. Get the flag transmitter running and capture the flag. Solvable without reverse engineering. https://mega.nz/#!TWR1AIRa!i-6-Ttl7fcugosewb_bYAsL0LqAy2mBLz_Yz8p0IW3Y
# Solved
Diberikan sebuah file framework dari <b>.NET</b>, disini saya menggunakan <b>dnspy</b> untuk mengdecompile source tersebut kemudian saya menemukan
```csharp
using System;
using System.Net;
using System.Net.Sockets;
using System.Threading;

namespace FlagProtocol
{
	// Token: 0x02000003 RID: 3
	internal class Program
	{
		// Token: 0x0600000A RID: 10 RVA: 0x00002151 File Offset: 0x00000351
		private static bool _TheFlagCanBeCapturedWithoutReversing()
		{
			return true;
		}

		// Token: 0x0600000B RID: 11 RVA: 0x00002154 File Offset: 0x00000354
		[TheFlagIs("CTFlearn{aHR0cHM6Ly93d3cueW91dHViZS5jb20vd2F0Y2g/dj1kUXc0dzlXZ1hjUQ==}")]
		private static void Main(string[] args)
		{
			if (!Program._TheFlagCanBeCapturedWithoutReversing())
			{
				return;
			}
			Console.WriteLine("Transmitting flag...");
			IPEndPoint endPoint = new IPEndPoint(IPAddress.Broadcast, 6969);
			UdpClient udpClient = new UdpClient();
			udpClient.EnableBroadcast = true;
			for (;;)
			{
				for (int i = 0; i < Program._indexes.Length; i++)
				{
					byte[] array = new FlagPacket
					{
						SequenceSize = (byte)Program._indexes.Length,
						SequenceNumber = Program._indexes[i],
						FlagByte = Program._pieces[i]
					}.ToBytes();
					udpClient.Send(array, array.Length, endPoint);
					Thread.Sleep(500);
				}
			}
		}

		// Token: 0x04000005 RID: 5
		private static byte[] _indexes = new byte[]
		{
			20,
			0,
			24,
			19,
			5,
			11,
			9,
			8,
			16,
			4,
			13,
			21,
			2,
			3,
			23,
			15,
			10,
			17,
			6,
			1,
			14,
			7,
			18,
			22,
			12
		};

		// Token: 0x04000006 RID: 6
		private static byte[] _pieces = new byte[]
		{
			100,
			67,
			125,
			51,
			97,
			117,
			121,
			123,
			116,
			101,
			99,
			95,
			70,
			108,
			51,
			112,
			48,
			117,
			114,
			84,
			52,
			110,
			114,
			109,
			95
		};
	}
}
```
Diketahui bahwa variable <b>indexs</b> adalah posisi dari variabel <b>pieces</b>. Inilah code yang saya gunakan
```python
index = [
    20, 0, 24, 19, 5, 11, 9, 8, 16, 4, 13, 21, 2, 3, 23, 15, 10, 17, 6, 1, 14, 7, 18, 22, 12
]
pieces = [
    100, 67, 125, 51, 97, 117, 121, 123, 116, 101, 99, 95, 70, 108, 51, 112, 48, 117, 114, 84, 52, 110, 114, 109, 95
]


r = []
for x in range(len(pieces)):
    r.append("")

for x in range(len(pieces)):
    r[index[x]] = chr(int(pieces[x]))

print ''.join(r)
```
```console
$ python solve.py
CTFlearn{y0u_c4ptur3d_m3}
```
Flag : <b>CTFlearn{y0u_c4ptur3d_m3}</b>