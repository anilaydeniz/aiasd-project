# Haftalık İş Akışı

**AI-Assisted Software Development · Atlas Üniversitesi · Güz 2026–2027**

**Sürüm 1 · 20 Eylül 2026** — bu belge dönem içinde yenilenir. Her haftanın dosyalarını
çektiğinizde onlarla birlikte gelir ("çekmek" ya da "pull yapmak", git'e GitHub'daki
en yeni dosyaları bilgisayarınızdaki kopyaya indirmesini söylemek demektir); dolayısıyla
pull yapmayı sürdürdüğünüz sürece deponuzdaki (depo, projenizin git tarafından takip
edilen klasörüdür; hem bilgisayarınızda hem GitHub'da bulunur) kopya günceldir.

> [!IMPORTANT]
> **Bu sürümde ne değişti**
>
> Henüz hiçbir şey değişmedi, çünkü bu ilk sürüm. Belgeyi yenilediğimde bu kutu neyin
> değiştiğini listeler ve değişen başlıkların yanında **`↻ changed in v2`** işareti olur.
> İkisi de ondan sonraki sürümde kaybolur; dolayısıyla işaretli olan her şey sizin için
> yenidir.

Bu belge değişmeyen rutini anlatır. Her haftanın *içeriği* farklıdır, çünkü her haftanın
ödevi o haftanın klasöründe gelir; ama *ritim* hep aynıdır.
Takıldığınızda buraya dönün.

---

## Bir bakışta

| Ne zaman | Ne yaparsınız | Puan |
|------|-------------|--------|
| Dersten önce | `weekNN/ASSIGNMENT_NN_TR.md` dosyasını okuyun | — |
| Ders sırasında (3 saat) | Çalışın ve sık push edin (push, bilgisayarınızda kaydettiğiniz işi GitHub'a gönderir) | — |
| Ders sonunda | Son bir push yapın; hemen ardından anlık görüntü alırım (anlık görüntü, deponuzun o andaki hâlinin birebir kopyasıdır) | 5 |
| Dersten sonra | Kalanı bitirin ve `ai_log_NN.md` dosyasını yazın | — |
| Cumartesi 23:59'a kadar | **Yeniden push edin.** Deponuzun ikinci bir anlık görüntüsünü alırım | 5 |

Her hafta on puan değerindedir ve bu puan iki ana eşit bölünür: **beşi dersin sonunda,
beşi Cumartesi teslim saatinde ölçülür.** İki yarı da GitHub'dan okunur, dolayısıyla
ikisi de push ister (push, bilgisayarınızdaki commit'leri GitHub'daki deponuza gönderen
`git push` komutudur). **1. Hafta tek istisnadır:** beş puan değerindedir, ilk dersin
sonunda hiçbir şey okunmaz ve beşinin tamamı Cumartesi 23:59'da deponuzdan okunur.
Bitmiş ama push edilmemiş iş, hiç yapılmamış işle tamamen aynı puanı alır.

Haftanın notunun yarısının derse bağlı olması bilinçlidir. İşin yeri derstir:
sınıftasınızdır ve hâlâ soru sorabilirsiniz. Diğer yarısı, haftanın işini bitirmeye ve
bir denetleyicinin (her haftanın istediği dosyaları arayan otomatik betik; nasıl
çalıştırılacağını §2 gösterir) göremeyeceği iki şeye dayanır. O iki şeyi §3 anlatır.

**Teslim saati her hafta aynıdır: Cumartesi 23:59.** Hesaplanacak bir şey yoktur, çünkü
Cumartesi gece yarısı deponuzda ne varsa onu notlandırırım. İşin çoğu, soru
sorabileceğiniz laboratuvarda yapılmalıdır; dersten sonraki günler başlamak için değil,
açıkları kapatmak içindir.

---

## Bir kez, bir daha asla

İlk ders başlamadan önce üç şeyin doğru olması gerekir ve hiçbiri dersin içeriğinin bir
parçası değildir: (a) bir GitHub hesabınız vardır, (b) deponuz vardır ve (c) o depoya
push etmesine izin verilen bir bilgisayarınız vardır. Gerekli komutlar
[**Kurulum Kartı**](AI_SETUP_CARD_TR.md)'ndadır. Kartta dört adım vardır ve son adım,
diğer üçünün çalışıp çalışmadığını söyler.

Kart ayrıca en çok karşılaşacağınız hataların ve her birinin gerçekte ne anlama
geldiğinin tablosunu da taşır. Açık tutun; git ve GitHub mekaniği için muhtemelen
ihtiyacınız olan tek sayfa odur.

---

## 1. O haftanın dersinden önce

`weekNN/ASSIGNMENT_NN_TR.md` dosyasını okuyun. Haftanın klasörüyle birlikte gelir ve o
haftanın tam olarak hangi dosyaları istediğini listeler.

Ön okuma varsa gelmeden önce okuyun.

---

## 2. Ders sırasında

### Hangi yarıda çalıştığınızı bilin

Deponuzun kökünden (projenizin en üst klasörü, yani `.github` klasörünü içeren klasör)
çalıştırın:

```bash
python .github/check_deliverables.py
```

İki parça hâlinde yanıt verir:

```
In the lab:     11 of 14 done
By Saturday:     0 of  3 done
```

Yukarıdaki sayılar yalnızca örnektir; gerçek sayılar haftadan haftaya değişir. Önemli
olan, iki satırdan hangisini okuduğunuzdur.

**In the lab**, dersin sonunda okuduğum satırdır ve haftanın notunun yarısı değerindedir.
Bu maddeler, benimle ve aynı yerde takılmış, diyelim, yirmi dokuz kişiyle aynı odadayken
yapmaya değer şeylerdir.

**By Saturday** haftanın geri kalanıdır: yazılar, diyagramlar ve `ai_log_NN.md` (yapay
zekâ asistanıyla yaptığınız işin haftalık günlüğü; §3 açıklar).
Bu, gerçekten yalnız yaptığınız iştir. Hafta içinde kontrolü başarısız kılmaz, çünkü
henüz teslim vakti gelmemiştir; ama notun diğer yarısıdır ve Cumartesi anlık görüntüsü
onu okur.

Kendinizi laboratuvarda `ai_log_NN.md` yazarken bulursanız haftayı tersten yaşıyorsunuz
demektir.

### Çalışın ve sık push edin

Her şeyi sonda tek devasa yığın hâlinde commit etmek yerine iş ilerledikçe commit edin
(commit, git geçmişinde `git commit` ile kaydedilen tek bir adımdır). Her commit'in
mesajı ne yaptığınızı söylemelidir:

```bash
git add .
git commit -m "week01: hello.py reads a name and prints the list"
git push
```

"update", "fix" ya da "asdf" gibi bir mesaj ne olduğu hakkında hiçbir şey söylemez ve
böyle mesajlar size commit hijyeni puanına (§3'te anlatılan commit disiplini puanı) mal
olur.

**10:00'da, 11:00'de ve dersin sonunda (11:45) push edin**; bu, iş hangi durumda olursa olsun her
derste en az üç push demektir. 10:00'da ve 11:00'de sınıf tablosuna (her öğrencinin deposunun
ne durumda olduğunu gösteren, perdeye yansıtılan tablo) bakıp herkesin nerede olduğunu
görürüm; dersin puanını belirleyen push, dersin sonundaki (11:45) push'tur. Push etmek hiçbir şeye mal
olmaz ve push edilmiş yarım bir bölüm, push edilmemiş bitmiş bir bölümden daha değerlidir.

### Kontrolleri kendiniz çalıştırın

Aynı komutu, istediğiniz kadar sık çalıştırın:

```bash
python .github/check_deliverables.py
```

Bunlar tam olarak benim çalıştıracağım kontrollerdir. Çıktı, eksik olanları satır satır
listeler. Bir not değil, yapılacaklar listesidir ve çalıştırmanın maliyeti yoktur.

### Ders bitmeden bir kez daha push edin

Son push dersin sonundadır (11:45). Hemen ardından her depoyu olduğu gibi dondururum (bir anlık görüntü,
yani deponun o andaki hâlinin birebir kopyasını alırım) ve kontrolleri o anlık görüntü
üzerinde çalıştırırım. Push etmediğiniz iş görünmezdir: bilgisayarınızda durur ve
sayılmaz.

Sonuç anonimleştirilmiş bir tablo (kimsenin gerçek adının görünmediği bir tablo) olarak
yansıtılır; satırınızı `student.json` (deponuzda bilgilerinizi, seçtiğiniz takma ad
dâhil, tutan dosya) içindeki takma adınızla bulun. O tablo **5 puan — haftanın yarısı**
değerindedir.

Bir öğrenci bir bilgisayarda, bir GitHub hesabıyla çalışır. Bir sınıf arkadaşınızın
bilgisayarında ya da onun GitHub oturumunda yapılan iş, ders için hiçbir puan getirmez.

**Commit disiplini (haftada 1 puan) her hafta değerlendirilir.** Derste farklı
zamanlarda birkaç push (en az üç) ararım; her birinde yeni iş olmalı. Ders dışında tek oturuşta çalışabilirsiniz; baktığım şey,
çalıştıkça yapılmış, her birinde biraz yeni iş ve ne değiştiğini söyleyen bir mesaj olan
birkaç commit'tir. Bir commit'in bitmiş bir parça olması gerekmez. Üç soru sorarım: iş adım adım mı büyümüş, bir commit'ten
diğerine gerçek bir ilerleme var mı, metin üzerinde çalışılmış mı yoksa bitmiş hâlde mi
yapıştırılmış? Hafta sonunda tek bir commit ya da tek parça hâlinde gelen metin puan
getirmez. Bir haftada şüpheli bir durum görürsem karar vermeden önce önceki haftalarınıza
da bakarım. Ayrıca herhangi bir derste size projeniz hakkında iki dakikalık bir soru
sorabilirim. Her hafta çalıştıkça commit edin; gerisi kendiliğinden hallolur.

### Devam, ve burada olmazsanız ne olur

**Her hafta dizüstü bilgisayarınızı getirin**, şarj aletiyle ve gereken kablosuyla
birlikte. Ders, üç saatlik uygulamalı bir çalışma fırsatıdır.

**Devam zorunludur.** Üniversite dönem boyunca birkaç hafta devamsızlık hakkı tanır ve
bu hak, nedeni ister hastalık, ister iş, ister aile, isterse başka herhangi bir şey
olsun, her şeyi zaten kapsar. Bunun üstünde ikinci bir kategori yoktur ve telafi
prosedürü yoktur.

**Kaçırdığınız ders, notlandıramadığım derstir.** Nedeni ne olursa olsun o 5 puan gider.
Nedenleri birbiriyle tartmam ve bu bilinçli bir karardır: yüzden fazla öğrenciyle,
mazeretleri yargılama süreci kendini en iyi anlatanı yargılama sürecine dönüşür.

Açık kalan, diğer yarıdır. Dersin işini kendi zamanınızda yapın, Cumartesi gece
yarısından önce push edin ve o beş puanı herkes gibi alın. Bir dersi kaçırmak size o
derse mal olur, haftaya değil.

---

## 3. Dersten sonra — Cumartesi 23:59'a kadar

Haftanın kalan işini Cumartesi gece yarısına kadar bitirin. O saatte ikinci bir anlık
görüntü alırım ve teslim anındaki durumunuz diğer 5 puanı belirler.

### `ai_log_NN.md` — atlamayın

Haftada bir dosya yazarsınız ve dosya o haftanın klasöründe durur; yani 1. Hafta'nın
dosyası `week01/ai_log_01.md` olur ve böyle devam eder. Dosya, hafta klasöründeki diğer
belgelerle birlikte gelir ve siz doldurursunuz. Hangi asistanı kullandığınızı, neyi doğru
yaptığını, neyi düzeltmek zorunda kaldığınızı ve ne öğrendiğinizi yazarsınız. **Kendiniz,
kendi cümlelerinizle yazarsınız**: Kanıt bloğu dışında asistan kullanılmaz, dili düzeltmek
için bile. İngilizceniz ya da Türkçeniz notlanmaz; asistanın yazdığı bir günlük, ne kadar
düzgün olursa olsun 2 puanın en çok 1'ini alır.

**Evidence bloğu zorunludur.** Gerçek yazışmayı iddianızın altına, kod bloğunun (üçer
ters tırnaktan oluşan iki satır arasındaki blok) içine yapıştırın: gönderdiğiniz istemi
ve aldığınız yanlış yanıtı. Konuşmanın tamamını yapıştırmayın; hatayı gösteren satırları
yapıştırın, bu da genellikle kısa bir kesittir, diyelim on–on beş satır. Evidence bloğu
boş olan bir iddia hiçbir şey kazandırmaz.

Bu neden zorunlu? Herkes "yapay zekâ hata yaptı, ben düzelttim" yazabilir. Gerçek bir
model çıktısını inandırıcı biçimde uydurmak zordur, çünkü uydurma transkriptler fazla
temiz okunur ve hataları fazlasıyla kolay fark edilir. Ve uzun bir konuşmanın hangi
kısmının kanıt sayılacağını seçmek, değerlendirilen becerinin ta kendisidir.

Konuşmanın tamamını saklamak isterseniz `weekNN/transcript.md` olarak kaydedin. O
dosyaları varsayılan olarak okumam, ama bir günlük girdisi tutarsız olduğunda sizinkini
okurum.

Bu dosya 2 puan değerindedir.

### Kontroller yeşil olana kadar devam edin

```bash
python .github/check_deliverables.py
git add .
git commit -m "week01: llm_notes written up"
git push
```

GitHub'da deponuzun **Actions** sekmesi her push'un sonucunu gösterir: GitHub her push'tan
sonra aynı kontrolleri çalıştırır ve bu otomatik çalıştırmaya CI (sürekli entegrasyon)
denir. Cumartesi durumunuzdaki yeşil tik **2 puan** değerindedir.

### Otomatik olmayan 3 puan

**Tutarlılık ve commit disiplini — 1 puan.** Bu haftanın işi, önceki haftalarda
yazdığınız gereksinimlerden ve tasarımdan gerçekten türüyor mu; commit geçmişiniz son
dakikada gelen tek bir yığın yerine adım adım büyüyen bir çalışma gösteriyor mu? Planınızı
değiştirdiyseniz, değişiklik `PROPOSAL.md` dosyasının değişiklik günlüğüne tarihli bir
satır olarak girdi mi? Fikir değiştirmek normal ve sağlıklıdır, ama değişiklik görünür
olmalıdır. Projenin kendisi (problemi ve ürünü) 3. Hafta dersinin sonunda (11:45) kesinleşir; ondan sonra yalnızca ayrıntıları değişir. Sessizce terk edilen bir gereksinim puana mal olur; `ai_log_NN.md` içinde tek
satırlık bir gerekçeyle bırakılan bir gereksinim hiçbir şeye mal olmaz. Mühendislik
böyle görünür.

**İnsan katkısı — 2 puan.** Bu, bu haftanın işini yalnızca modellerin değil, insanların
da yaptığının kanıtıdır. Kendi payınız `weekNN/ai_log_NN.md` içinde görünür: somut bir
yapay zekâ hatası, yapıştırılmış kanıt ve elle değiştirdiğiniz şey; bu iki puan o günlük
için ödenir. 2. Hafta'dan itibaren her hafta en çok iki sınıf arkadaşınız, ödevin
adlandırdığı rolde (örneğin paydaş, tasarım gözden geçireni ya da testçi olarak) size
yardım edebilir ve onları `weekNN/contributors_NN.json` içine, her biri için ne yaptığını
söyleyen bir cümle ve o işin kanıtıyla birlikte kaydedersiniz; kanıt, onların notları,
hata listeleri ya da günlüğünüzdeki tarihli bir paragraf olabilir. 2. Hafta'da katkıcı
zorunlu değildir: sıfır, bir ya da iki kişi; yalnız çalışmak size hiçbir şeye mal olmaz.
3. Hafta'dan itibaren zorunludur: derste sizi değerlendiren üç kişi, 4. Hafta'dan
itibaren de grubunuzun üç üyesi her hafta dosyada yer almalıdır. Listelediğiniz kişi
gerçek olmalıdır; arkasında hiçbir şey olmayan isimler bir listedir, kanıt değil, ve kanıt
olmadan katkıcı bonusu ödenmez.

**4. Hafta'dan itibaren katkıcılarınız grubunuzdur.** 3. Hafta'da dört kişilik grubunuzu
kendiniz kurarsınız ve o grup dönem boyunca birlikte kalır. Her hafta, ders ile Cumartesi
arasında, dördünüz **bir saat çevrimiçi** buluşursunuz: her kişi o hafta projesinde neyin
değiştiğini anlatır ve diğer üçü ne düşündüğünü söyler. `weekNN/contributors_NN.json`
içindeki üç kaydınız bu üç kişidir; her biri için ne söylediğini, alıntı olarak, ve
bunun üzerine sizin ne yaptığınızı yazarsınız. Orada olmayan biri için o kayıtları kimse
yazamaz.

**Katkıcılar bonus kazanır.** Size yardım eden bir sınıf arkadaşı o haftaki notunuzun
%10'unu kazanır; bu, haftada en fazla üç katkı için geçerlidir. Siz onlara yardım
ettiğinizde de aynısı sizin için geçerlidir. 2. Hafta'da isimler sizin seçiminizdir;
3. Hafta'dan itibaren grubunuzdur. 1. Hafta'da katkıcı yoktur.

Bir LLM (büyük dil modeli; yapay zekâ asistanlarının arkasındaki model türü) bir ödevin
istediği her dosyayı üretebilir. Yapamadığı şey, o dosyaları çevresindeki on haftayla
tutarlı kılmak ya da kendi hatalarını sizin yerinize fark etmektir. Asıl değerlendirilen
budur.

---

## 4. Her hafta geçerli kurallar

**API anahtarını asla koda koymayın.** (API anahtarı, programınızın bir dış hizmeti
kullanmasını sağlayan, parolaya benzer gizli bir dizgidir.) Anahtar `.env` içinde yaşar
(yalnızca kendi bilgisayarınızın okuduğu küçük bir ayar dosyası) ve `.env`,
`.gitignore` içinde listelenir (git'e hangi dosyaların asla commit edilmeyeceğini
söyleyen dosya). Bir anahtar depoya ulaşırsa otomatik tarama
onu yakalar ve **10 puan** kaybedersiniz. Anahtar bir kez push edildiyse silmek yetmez,
çünkü git geçmişinde kalır. O anahtarı iptal edip yenisini almanız gerekir.

**Kodu temiz tutun.** Push etmeden önce `ruff` çalıştırın (Python kodundaki biçem
sorunlarını bulan ve düzelten bir araç):

```bash
ruff check .          # sorunları listele
ruff check . --fix    # otomatik düzeltilebilenleri düzelt
ruff format .         # biçimlendir
```

Yapay zekâ üretimi kod sık sık arkasında kullanılmayan import bırakır (import satırı,
kodun hiç kullanmadığı bir modülü yükleyen satırdır); `ruff` bunları anında yakalar.

**Uygulamanız telefonda çalışmalı.** Tarayıcı pencerenizi ara sıra yaklaşık 390 piksele
(aşağı yukarı bir telefon ekranının genişliği) daraltın. Bir şey kesiliyor ya da yana
kayıyorsa pencere küçükken düzeltin, 10. Hafta'da değil.

**Önceki haftaları bozmayın.** Kontroller birikimlidir: 5. Hafta'da 1–4. Haftalar
yeniden denetlenir. Bir değişiklik eski bir şeyi bozarsa CI (kontrollerin GitHub'daki
otomatik çalıştırması; bkz. §3) size söyler.

---

## Takıldığınızda

**CI kırmızı ve nedenini anlamıyorum.** GitHub'da **Actions** sekmesini açıp başarısız
çalıştırmaya tıklayın. Hangi kontrolün neden başarısız olduğunu satır satır söyler. Aynı
çıktı, `python .github/check_deliverables.py` komutunu yerelde (kendi bilgisayarınızda)
çalıştırdığınızda da gelir.

**Kontroller yerelde geçiyor, GitHub'da geçmiyor.** Olağan neden, push etmediğiniz bir
dosyadır. `git status` çalıştırın (değişmiş ama henüz commit ya da push edilmemiş
dosyaları listeler).

**`ruff` yerelde temiz, CI'da değil.** Bu bir sürüm uyuşmazlığıdır: bilgisayarınız ve CI
farklı `ruff` sürümleri çalıştırıyordur. Elinizde hangisi varsa onu değil, o haftanın
`requirements.txt` dosyasında (haftanın ihtiyaç duyduğu paketlerin, tam sürümleriyle
birlikte listesi) sabitlenmiş sürümü kurun.

**Ollama çalışmıyor / model inmiyor.** (Ollama, bir yapay zekâ modelini kendi
bilgisayarınızda çalıştıran programdır.) Daha küçük bir modele geçin. Hiçbiri
çalışmıyorsa bulut arka ucunu (bir sağlayıcının sunucularında çalışan ve internet
üzerinden ulaştığınız bir model) kullanın ve nedenini `model_notes.md` içine yazın; bu
kabul edilebilir bir sonuçtur. Haftayı buna kaptırmayın.

**Bir şeyi bozdum ve geri alamıyorum.** Panik yapmayın, çünkü git her şeyi hatırlar:

```bash
git log --oneline           # commit geçmişi
git diff                    # şu an ne değişti
git checkout -- file.py     # bir dosyayı son commit'e döndür
```

**Hâlâ takıldınız mı?** Derste sorun ya da bir yapay zekâya sorun. Bir yapay zekâya
sorarsanız söylediğini doğrulayın ve yazışmayı `ai_log_NN.md` içine kaydedin. Bu ders
tam olarak bununla ilgilidir.

---

## Komut özeti

```bash
# çalışırken
python .github/check_deliverables.py     # neyin eksik olduğunu göster
AIASD_WEEK=2 python .github/check_deliverables.py   # istersen yalnızca bir hafta
ruff check . --fix                       # kodu temizle
git add . && git commit -m "weekNN: ..." && git push

# ortam
source .venv/bin/activate                # Windows: .venv\Scripts\activate
streamlit run app.py
```
