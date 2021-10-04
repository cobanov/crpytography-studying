# Cryptography

## Python ile Kriptografi Scriptleri

- [SHA256 Password Encryption with SQlite](https://github.com/cobanov/crpytography-studying/blob/master/sha.py)
- [AES CTR](https://github.com/cobanov/crpytography-studying/blob/master/aes-ctr.py)
- [AES GCM](https://github.com/cobanov/crpytography-studying/blob/master/aes-gcm.py)
- [HMAC](https://github.com/cobanov/crpytography-studying/blob/master/hmac.py)

## Sozluk

Sozluk yeni terimler ogrendikce giderek genislemektedir.

Key:

Message:

Cipher:

Plaintext:

Encrypt:

Decrypt:

## Kriptografi Kullanim Alanlari

Kriptografinin genellikle iki parcali dusunulebilir, Ilki guvneli anahtarin (secured key)  iletisime gececek iki kisi tarafiondan paylasilmasi ve bu paylasim saglandiktan sonra bu iki kisinin nasil iletisime gececegi.

- Guvenli baglanti olusturmak (Secure communication)
- Dijital Imzalar (Digital Signatures)
- Anonim haberlesme (Anonymous communication)
- Anonim dijital paralar (Anonymous digital cash)
- Oy vermek ve secimler (Elections)
- Privately Outsourcing Computation: e.g. google'a sorgu gondermek
- Proof of Knowledge

## Kriptografi Tarihi

David Kahn The Code Breakers (1996)

### Simetrik Ciphers

Iletisime gececek iki tarafin sahip oldugu bir key var, fakat bu iletisimi dinlemek isteyen kisi bu key'e sahip degil.

![Untitled](Cryptography%2069fc9591d0f046b0883fdb153d726a46/Untitled.png)

### **Subtition Cipher, Caesar Cipher**

Anahtar kisaca, bir tablodan veya basitce cozulebilecek bir algoritmayla belirlenir, bu harfleri kaydirmak veya sabit bir tablodan sifreleme ile yapilabilir. Kirilma yontemi oldukca basittir:

1. En sik kullanilan harf baslangic noktasi olarak secilir. e.g. %12.7 ingilizcede e harfinin kullanimi, t harfi %9.1, a %8.1
2. Ikili veya uclu harflerin birlikte kullanimina bakilir, 'he', 'an', 'in', 'th' gibi ciftlerin uyumlari incelenir

![Untitled](Cryptography%2069fc9591d0f046b0883fdb153d726a46/Untitled%201.png)

### **Vigener Cipher(16th century, Rome)**

Herhangi bir anahtar belirlendikten sonra, bu anahtar mesaji ortecek kadar tekrarlanir, anahtarin alfabedeki sirasi mesajin harflerindeki alfabe siralarina eklenir, 26 harf icin mod(26)

Kirilmasi yine oldukca basittir, ilk yapilmasi gereken sey, anahtarin uzunlugu icin bir tahminde bulunmak, sonrasinda mesaj bu grup uzunluguna bolunur, her grubun baslangici icin ilk harfe bakilir, anahtarin ilk harfinin mesajda en cok tekrarlanan degeri, E olacak sekilde deneme yapilir. **Kaynak gerekli daha iyi arastirma yapilacak.**

![Untitled](Cryptography%2069fc9591d0f046b0883fdb153d726a46/Untitled%202.png)

### **Rotor Machine**

Hebern Machine, Enigma

Harflar, bir disk uzerinde karsilik gelecek sekilde siralanir, klavyede giris yapildikca disk bir adim doner ve key her giris saglandiginda bir adim kaymis olur, istatistiksel bir sifreleme yontemidir, cozumu gorece daha zor olsa da, gunumuzde oldukca kolaydir. 

![Untitled](Cryptography%2069fc9591d0f046b0883fdb153d726a46/Untitled%203.png)

### **Data Encryption Standard DES**

Ikinci dunya savasindan sonra genellikle kriptografik sistemler, fiziksel motorlu sistemlerden cikip dijital sistemlere donustu, ilk zamanlarda $2^{56}$ keys, 64 bit block size'a sahip sistemelr o gun icin yeterliydi fakat gunumuzde brute force attack ile kolayca gecilebildigi icin, AES (128-bit key), Salsa20 gibi sistemler kullaniliyor.

---

## Ayrik Olasilik

Kaynak:

[High School Mathematics Extensions/Discrete Probability - Wikibooks, open books for an open world](https://en.wikibooks.org/wiki/High_School_Mathematics_Extensions/Discrete_Probability)

**Uniform Distribution:** Uzaydaki her eleman ayni agirliga sahiptir.

**Point Distribution**: Tek bir deger icin olasilik degeri 1 ve geri kalan tum degerler icin olasilik degeri 0 olan dagilimdir.

Union Bound

Random Variable:

Uniform Random Variable:

Randomized Algorithms:

### XOR

Temelde XOR iki bitin toplaminin mod2'sidir. Bir espri olarak kriptograflarin bildigi tek sey her seyi XORlamaktir. XOR kriptografide oldukca sik kullanilmaktadir.

Random dagilan bir y dagilimimiz olsun, ayni zamanda bagimsiz **uniform** dagilan bir x dagilimi olsun. $Z = Y \oplus Z$ ne ile basliyor olursa olsun her zaman uniform bir dagilim ciktisi verir.

### Birthday Paradox

Ornek sayisinin karekoku kadar deneme yapildiginda, yaklasik olarak iki ornegin birbirine esit olabileceginin savunan paradoks. Daha iyi bir aciklama geleceke **TODO**

![Untitled](Cryptography%2069fc9591d0f046b0883fdb153d726a46/Untitled%204.png)

---

## One Time Pad - OTP

$C:=E(K, M) = K \oplus M$

Yukarida goruldugu sekilde basit bir temeli vardir. Sifrelenmek istenen mesaj, ayni (veya daha uzun) uzunluktaki bir anahtarla XOR islemine tabii tutulur ve mesaj basitce sifrelenmis olur. 

D(K, E(K, M) veya $K \oplus (K \oplus M)$ seklinde hizlica cozulebilir.

XOR islemi cok hizli bir sekilde yapilabildigi icin cok hizlidir. Fakat anahtar mesaj uzunlugunda olmasi gerektigi icin anahtarlar cok uzun olacaktir. Arkasindaki fikir oldukca iyidir ama pratik olarak kullanmak bu problemden dolayi zordur. 

## Information Theoretic Security

***Claude Shannon hakkinda daha fazla arastirma yap***

**Temel Fikir:** Ciphertext asla plaintext hakkinda fikir vermemeleridir veya onu aciga cikartacak bilgi icermemeledir.

## Stream Ciphers

## Atak Tipleri

**Rainbow Attack:**

TODO

**Dictionary Attack:**

TODO

## Simetrik / Asimetrik

TODO

## Algoritmalar

### SHA

### AES

Salt:

- 128-bit olmali
- Daha sonrasi icin kaydedilmeli

Key:

256-bit integer, 64 hex digits, 32 byte

base64: binary datanjj 64 ascii karakteriyle kodlanmasidir. 010101 gibi degerler bas64 tabllsundan sirayla degerler alir. 3 adet 8 bitlik ya da 3 baytlik veri, 4 adet 6 bitlik degerle yeniden yazılır.
