# la cifra de - Points: 200
<b>Description : </b>I found this cipher in an old book. Can you figure out what it says? Connect with nc 2019shell1.picoctf.com 1172.<br>
<b>Hints : </b>There are tools that make this easy. Perhaps looking at history will help
# Solved
Message when i connected to the server
```
Ne iy nytkwpsznyg nth it mtsztcy vjzprj zfzjy rkhpibj nrkitt ltc tnnygy ysee itd tte cxjltk

Ifrosr tnj noawde uk siyyzre, yse Bnretèwp Cousex mls hjpn xjtnbjytki xatd eisjd

Iz bls lfwskqj azycihzeej yz Brftsk ip Volpnèxj ls oy hay tcimnyarqj dkxnrogpd os 1553 my Mnzvgs Mazytszf Merqlsu ny hox moup Wa inqrg ipl. Ynr. Gotgat Gltzndtg Gplrfdo

Ltc tnj tmvqpmkseaznzn uk ehox nivmpr g ylbrj ts ltcmki my yqtdosr tnj wocjc hgqq ol fy oxitngwj arusahje fuw ln guaaxjytrd catizm tzxbkw zf vqlckx hizm ceyupcz yz tnj fpvjc hgqqpohzCZK{m311a50_0x_a1rn3x3_h1ah3xflc148k7}

Yse lncsz bplr-izcarpnzjo dkxnroueius zf g uzlefwpnfmeznn cousex mzwkapr, cfd mgip axtfnj 1467 gj Lkty Bgyeiyyl Argprzn.

Ehk Atgksèce Inahkw ts zmprkkzrk xzmkytmkx narqpd zmp Argprzn Oiyh zr Gqmexyt Cousex.

Ny 1508, Jumlntjd Txnehkrtuy nyvkseej yse yt-narqpd zfmurf ceiyl (a sferoc zf ymtfzjo arusahjes) zmlt ctflj qltkw me g hciznnar hzmvtyety zf zmp Volpnèxj Nivmpr.

Hjwlgxz’s yjnoti moupwez fapkfcej ny 1555 ay f notytnafeius zf zmp fowdt. Zmp lubpr nfwvkx zf zmp arusahjes gwp nub dhokeej wpgaqlrrd, muz yse gqahggpty fyd zmp itipx rjetkwd axj xidjo be rpatx zf g ryestyii ppy vmcayj, hhohs cgs me jnqfkwpnz bttn jlcn hzrxjdpusoety.
```
I believe this is some Vignere Cipher, but we need a <b>Key</b>! How we solve if there isn't key ? so im using this website https://www.mygeocachingprofile.com/codebreaker.vigenerecipher.aspx to found some key!.
```
Based on repetitions in the encrypted text, the most probable key length is 64 characters.

Here is a list of the most probable keys based on frequency analysis of the letters in the cipher:

Key #1: ulagplagflpgflavfzagflogslavflbgflngflanflagflagqlatflagflngulag
Key #2: ulagplagflpgflavfzagflogslavflbgflngflanflagflagqlatflagflnruleg
... etc
-- MESSAGE w/Key #1 = 'ulagplagflpgflavfzagflogslavflbgflngflanflagflagqlatflagflngulag' ----------------
tt is ynteredting soi in hietbry aeoole osten rxceive cresit sor thints ehey oid net creaeedurtns the cauese zf hhstoey, the oigenère ciehee has beea rpinvpntet many ttmesie wms faleeyy aetrhbutrd to beaise de vivenèee as it wns zrigtnalby desccibed tn 1553 ny giohaa baetirta brllash in his booz la pifra dey. stg. gizvan rattisea belwaeofor fhr imalelentntion hf this cipwer n table if fzrmeo by sbiding ehe lohed half af nn ocdimary nlphauet for an aepaeently rnnoom nfmbeh of planes wieh despeot go tse uoper ualfpbcoctf{b311a50_0r_k1gn3e3_c1ph3raap148e7}ehe ftrst mell-donumeneep descdictizn oe a poyyalpaabetic ciehee howevee, wls maoe areund 1467 by weon bltfista mloerei.tge vitenère vipher is twerrfore sozeeimed calbed the llberei pisc od aybecti biphrr.in 1508, jhhannes trxthrmius inieyted ehe se-calleo tabuwa decta (m mntrtx oe shisted aephabets) twat jould lagec be a nritycal coxponeyt af the hitenèce chphee.belltso’s secons bobklet apcelred tn 1555 as q contiyuatizn af the riest. ehe kowee halvxs of the alehaoets are aoh shiqted hegulacly, bue tte alptaoetd anc the vndex eetters art miked by mennd of a xnemenic kej phrade, ihich oaa be oifeereat wita each corrtspbndent.
```
So i got the point of the Key, if i just put Key is <b>Flag</b>.
```
-- MESSAGE w/Key #1 = 'flag' ----------------
it is interesting how in history people often receive credit for things they did not createduring the course of history, the vigenère cipher has been reinvented many timesit was falsely attributed to blaise de vigenère as it was originally described in 1553 by giovan battista bellaso in his book la cifra del. sig. giovan battista bellasofor the implementation of this cipher a table is formed by sliding the lower half of an ordinary alphabet for an apparently random number of places with respect to the upper halfpicoctf{b311a50_0r_v1gn3r3_c1ph3raac148e7}the first well-documented description of a polyalphabetic cipher however, was made around 1467 by leon battista alberti.the vigenère cipher is therefore sometimes called the alberti disc or alberti cipher.in 1508, johannes trithemius invented the so-called tabula recta (a matrix of shifted alphabets) that would later be a critical component of the vigenère cipher.bellaso’s second booklet appeared in 1555 as a continuation of the first. the lower halves of the alphabets are now shifted regularly, but the alphabets and the index letters are mixed by means of a mnemonic key phrase, which can be different with each correspondent.
```
Flag : <b>picoCTF{b311a50_0r_v1gn3r3_c1ph3raac148e7}</b>
