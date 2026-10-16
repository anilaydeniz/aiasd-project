# AIASD · 4. Hafta — Tıklanabilir Prototip ve Test Case'ler

*Atlas Üniversitesi · Güz 2026–27 · Prof. Dr. Vedat Coşkun*
*Bu sayfadan sunulur. Her seferinde bir bölüm kaydırın; her `---` bir slayttır.*

<!-- Eğitmen: tarayıcıyı %150'ye yakınlaştırın ve GitHub başlığını kapatın. Toplam ≈ 3 saat:
25 dk anlatım · 10:30 civarına kadar yapım (10:00'da push) · 11:30 civarına kadar walk-through,
prototip başına 12 dk (11:00'de push) · dosyalar, denetleyici ve 11:45'teki son push · hemen ardından dondurma. -->

---

## Bugün

1. Neden prototip, neden şimdi
2. Prototip: `week04/prototype/` içinde düz HTML ekranlar
3. Kabul ölçütünden test case'e
4. Yapım zamanı: prototip ve `test_cases.json`
5. Walk-through: collaborator'ınız test case'lerinizi prototipiniz üzerinde yürütür
6. Cumartesi'ye kadar: düzeltme, yeniden yürütme, güncelleme, S1, yapay zeka günlüğü
7. Bu hafta nasıl notlanır

---

## Bu hafta asistan nerede yardım eder

| Parça | Asistan |
|---|---|
| Her ekranın HTML ve CSS'i (REQ satırları isteme yapıştırılır; bir ekran, bir commit) | **Yardım eder** |
| Kabul ölçütlerinizden test case taslağı (her birini kendi ölçütüyle siz karşılaştırırsınız) | **Yardım eder**, onay sizde |
| Ölçütlerinizden önerilen uydurma veriler | **Yardım eder**, onay sizde |
| Bir `fail` sonrası prototipi düzeltmek | **Yardım eder** |

---

## … ve nerede hiç yardım etmez

| Parça | Asistan |
|---|---|
| Ana akışınız ve istemden önce yazılan ölçütler | **Yardım yok**: siz karar verirsiniz |
| Collaborator'ınızın söyledikleri: notlarınız, `walkthrough_04.json`, alıntıladığınız cümle, `accepted` ve `why` | **Hiç yardım yok, dil bilgisi ve çeviri dahil**: elle |
| Değişiklik günlüğü satırları, her `fail` için kararınız, bir belgenin değişip değişmeyeceği | **Yardım yok** |
| `ai_log_04.md`, Evidence bloğu ve kalın alıntılar dışında | **Yardım yok** |
| `store.json`, geliştirici hesabı, ekran görüntüsü | **Yardım yok** |

<!-- Eğitmen: "Yardım yok" satırlarını yüksek sesle okuyun. Yeni olan ikinci satır: collaborator'ın söyledikleri elle yazılır, dil bilgisi ve çeviri de dahil. -->

---

## Neden prototip, neden şimdi

Kimse bir ürünü görmeden onun bütün gereksinimlerini yazamaz.

Başka biri ekranlarınızda gezinirken orada olmayan bir düğmeyi arar ya da hiçbir gereksinimin söz etmediği bir mesajı bekler. Bunların her biri eksik ya da belirsiz bir gereksinimdir.

**Bugün bulunursa size bir ekrana mal olur. 8. haftada bulunursa bir sunucu değişikliğine ve iki istemciye mal olur.**

Gereksinimleriniz bu yüzden 5. haftanın sonuna kadar açık kalır: bu hafta size neyin eksik olduğunu gösterir.

---

## Prototip — `week04/prototype/`

- **Her ekran için bir HTML dosyası.** İlki `index.html`'dir. Çift tıklayınca açılır: sunucu yok, framework yok, derleme adımı yok.
- **Her ekrana tıklayarak ulaşılır.** Bağlantıları `href="rooms.html"` biçiminde yazın: tam ad, küçük harf, tırnak içinde.
- **Her ekran gereksinimlerini söyler:** `<!-- serves: REQ-002, REQ-006 -->`
- **Uydurma veriler sabittir**, böylece collaborator'ınız adımları izleyebilir. Giriş kodu her zaman **1234**'tür. Kendi değerleriniz `prototype/README.md` dosyasına yazılır.
- **Üç başlangıç ekranı** denetleyiciyle gelir: herkesin ortak girişi (REQ-001). Ana akışınız `home.html`'den başlar.
- **Sunucu yok, hafıza yok:** bir rezervasyondan sonra bir sonraki ekran, aynı sabit veriyi o rezervasyon zaten içinde olacak şekilde gösterir.

**Dersin sonuna (11:45) kadar en az beş ekran. Cumartesi'ye kadar akışın tamamı, en az yedi.**

---

## Asistanınızla yapın — önce ölçütler

`AI_Doc5` §1: bir ekran istemeden önce, karşılaması gereken REQ satırlarını kabul ölçütleriyle birlikte yapıştırın. Sonra cevabı bunlarla karşılaştırın.

Asistanların eklemeyi sevdikleri ve bozdukları:

| Asistanın eklediği | Bozduğu |
|---|---|
| şifre alanı, "Google ile giriş" | REQ-001: e-postayla kod, şifre yok |
| 480 px genişliğinde bir yerleşim | REQ-006: 390 px, yatay kaydırma yok |
| bir şey ters gittiğinde hiçbir mesaj | yanlış kodun test case'i |

**Ne istediğinizi söyleyin:** düz HTML ve CSS, her ekran için ayrı bir dosya, ortak `style.css`, framework yok. Bir seferde tek ekran ve **her ekran için bir commit**.

**Uydurma veriler:** asistan ölçütlerinizden önersin (boş bir saat ve dolu bir saat, doğru bir kod ve yanlış bir kod, boş bir liste, sınır değerleri). Siz onaylar, `prototype/README.md` dosyasına yazarsınız. Orada veri yoksa collaborator'ınızın sonucu `blocked` olur.

Bu konuşmalardan birini saklayın. Bu haftanın yapay zeka günlüğü odur.

---

<h1 align="center">AI LOG KESİNLİKLE<br>İNSAN TARAFINDAN YAZILIR.</h1>

<h1 align="center">SİZ YAZARSINIZ.<br>ASİSTAN DEĞİL.</h1>

<p align="center"><b>Evidence bloğunun ve kalın alıntıların dışında asistan yok.<br>Ne yazmak için. Ne düzeltmek için. Dil için bile.</b></p>

<h1 align="center">Asistana yazdırılmış günlük 0 puan alır.</h1>

<!-- Hoca: bir kez yüksek sesle okuyun ve geçmeden önce birkaç saniye ekranda bırakın. -->

---

## AI log: iki tür söz

Sizin sözleriniz: düz yazı. Her kelime, her virgül, dil bilgisi de. Siz yazarsınız.

Asistanın sözleri: kalın. Yalnızca asistandan gelmesi gereken yerde: cevabında işaret ettiğiniz bir ifade ya da tek cümle.

Günlüğünüzde böyle görünür:

> İlk cevap şu cümleyle bitti: **Tüm gereksinimler karşılandı**. Ama bir şifre alanı vardı ve REQ-001 şifre yok diyor. Bu ölçütü istemden önce yazmıştım.

1. Kalın bir ifade Evidence bloğunda da harfi harfine bulunmalı.
2. Bir ifade ya da tek cümle; asla paragraf değil. Cevabın tamamı Evidence bloğunda `AI:` altına, sizin isteminiz `ME:` altına gider.
3. Kalın yazı asistan içindir, başka hiçbir şey için değil: vurgu, başlık ya da etiket için kalın yok.
4. Geri kalanını siz yazarsınız: ne cümleleri, ne dil bilgisini, ne çeviriyi, ne de bir asistanın "cilasını".

<!-- Hoca: örneği gösterin. Kalın olan asistan, geri kalanı öğrenci. Günlüğü okuyan bunu tek bakışta görmeli. -->

---

## Kabul ölçütünden test case'e

| | |
|---|---|
| **REQ-002** | Bir öğrenci bir odada boş olan 30 ile 120 dakika arası bir dilimi ayırır. |
| **Kabul ölçütü** | Boş bir dilim için yapılan ayırma kaydedilir ve dolu görünür; dolu bir dilim için yapılan ayırma bir mesajla reddedilir. |
| **TC-002-01** | *Ön koşul:* giriş yapılmış. *Adımlar:* Odalar'ı açın; Oda 3, bugün, 16:00–17:30; Ayır'a dokunun. *Beklenen:* "Ayrıldı: Oda 3, 16:00–17:30"; dilim dolu görünür. |
| **TC-002-02** | *Ön koşul:* Oda 3, 14:00–15:00 dolu. *Adımlar:* Oda 3, bugün, 14:00–15:00; Ayır'a dokunun. *Beklenen:* "Bu dilim dolu"; hiçbir şey ayrılmaz. |

Kimlik, hangi gereksinimi test ettiğini söyler. **TC-002-01** ve **TC-002-02** ikisi de **REQ-002**'yi test eder ve bir kimliğin anlamı hiçbir zaman değişmez.

---

## İyi bir test case

- **Tek bir gereksinim.** `req` alanı onu söyler.
- **Gerçek değerlerle adımlar:** "bir oda ve bir saat" değil, "Oda 3, 16:00–17:30".
- **Test edenin görebileceği bir beklenen sonuç:** "çalışır" değil, "'Bu dilim dolu' mesajı".
- **Ters giden yol da:** yanlış bir kod, boş bir alan, dolu bir dilim. Cumartesi'ye kadar en az üç gereksinimin böyle bir test case'i olur.

ZAYIF: *"Ayırma çalışıyor. Adımlar: bir oda ayır. Beklenen: başarılı."*

GÜÇLÜ: önceki slayttaki iki satır.

---

## Asistanla test case

Asistanınız test case'leri kabul ölçütlerinizden taslak olarak yazabilir. Sonra her birini kendi ölçütüyle karşılaştırın.

**Ölçütün söylediğini mi test ediyor, yoksa asistanın uydurduğu bir şeyi mi?**

Hiçbir gereksinimin anlatmadığı bir davranışı test eden bir test case iki şeyden biridir:

- **eksik bir gereksinim**: yeni bir kimlik ve bir Değişiklik günlüğü satırıyla ekleyin;
- **silinecek bir test case**.

Her `must` gereksinimin **dersin sonuna (11:45) kadar** en az bir test case'i olur, çünkü collaborator'ınız onları bugün yürütür.

---

## Önceki belgeler hala açık

`requirements.json`, `SRS.md` içindeki use case'ler, `screens_03.md`, `PROPOSAL.md`: hiçbiri donmuş değil. Ekranları kurmak onların ilk gerçek sınavı ve açıklarını gösterecek. **Açığı fark etmek ve değişikliği kaydetmek işin kendisi.**

Kimliklerin anlamı değişmez: yeni kimlik ya da `"dropped": true`. **Her değişiklik: kimlikleri anan tarihli bir Değişiklik günlüğü satırı.** Karar yalnızca sizin, asistan yok.

---

## Bir belgenin değişmesi gerektiğinin belirtileri

- bir ekranın `serves:` yorumunu yazamıyorsunuz → bir gereksinim eksik ya da ekran gereksiz
- akış tamamlandı, bir `must`'ın ekranı yok → akışta boşluk ya da aslında `must` değil
- bir ölçüt test edenin görebileceği bir sonuca dönüşmüyor → ölçüt belirsiz
- uydurma veri, ölçütün hiç söz etmediği bir değer istiyor → ölçütün sınırı yok
- prototip gereksinimin dediğini yapıyor ama `fail` → yanlış olan prototip değil, gereksinim

---

## Yapım zamanı — 10:30 civarına kadar

1. Denetleyiciyi çalıştırın: `week04/` gelir.
2. Üç başlangıç ekranının köşeli parantezli kısımlarını değiştirin.
3. Ana akışınızı `home.html`'den itibaren kurun: `week03/screens_03.md` dosyasındaki ekranlar, tek tek, önce ölçütleri vererek.
4. `test_cases.json` dosyasını yazın: her `must` için en az bir test case.
5. Her ekranı 390 px genişlikte açın: F12, sonra telefon simgesi.

**10:00'da push**, iş hangi durumdaysa.

<!-- Dolaşın. 10:00'da panoya bakın: kimde henüz week04/ yok. 10:25'te beş dakika kaldığını söyleyin. -->

---

## Walk-through — collaborator'ınızla

**Collaborator'ınız**, kendi dersinizden, herhangi bir gruptan seçtiğiniz tek bir sınıf arkadaşınızdır. Walk-through başlamadan önce kim olduğunu aranızda kararlaştırın. Her prototipe yaklaşık **on iki dakika** düşer.

**Sahip**, prototipi kendi bilgisayarında 390 px genişlikte açar, `prototype/README.md` içindeki uydurma verileri gösterir ve bilgisayarı verir. Bundan sonra sahip **yalnızca izler, açıklama yapmaz, yardım etmez**, her yürütmeyi kağıda not eder ve tur biter bitmez dosyaya yazar.

**Collaborator**, adımları yüksek sesle okur, tam olarak söylediklerini yapar ve ne gördüğünü söyler. Sahibin test case'lerinden **en az dördünü**, en az ikisi ana akıştan olmak üzere yürütür.

<!-- 12 dakikada bir zil. 11:00'de push, ya da kendi turunuz biter bitmez. -->

---

<h1 align="center">COLLABORATOR'INIZIN SÖYLEDİKLERİNİ<br>ELLE YAZARSINIZ.</h1>

<p align="center"><b>Kağıt notlarınız. <code>walkthrough_04.json</code> içindeki notlar. Alıntıladığınız cümle. Kararlarınız.<br>Asistan yok. Yazmak için yok. Çevirmek için yok. Dil bilgisi için bile yok.</b></p>

<h1 align="center">GERİ DÖNÜŞ COLLABORATOR'INIZDAN GELİR,<br>BAŞKA KİMSEDEN DEĞİL.</h1>

<p align="center">Türkçeniz ya da İngilizceniz notlanmaz. Her kaydı bir insan okur.</p>

<!-- Eğitmen: bir kez yüksek sesle okuyun ve geçmeden önce birkaç saniye ekranda bırakın. -->

---

## Pass, fail, blocked

| Sonuç | Anlamı | Not |
|---|---|---|
| `pass` | collaborator "expected" alanında yazanı gördü | birkaç kelime |
| `fail` | görmedi | onun yerine ne gördüğü |
| `blocked` | prototip üzerinde kontrol edilemez; örneğin "kod bir dakika içinde gelir" | nedeni; 5. haftadan itibaren gerçek sistem üzerinde kontrol edilir |

Henüz var olmayan bir ekran `fail`'dir.

**Bir `fail` yüzünden kimse puan kaybetmez.** Puanlar, test case'leri dürüstçe yürütmek ve her `fail` için ne yaptığınız içindir.

---

## Hiçbir test case'in kapsamadığına kulak verin

*"Ayırmayı iptal etmenin bir yolunu aradım."*

Bunu hiçbir test case kapsamaz, çünkü hiçbir gereksinim bunu istemez. Walk-through tam olarak bunun içindir.

Bir nota yazın. Cumartesi'ye kadar karar verirsiniz: ya yeni bir kimlik ve bir Değişiklik günlüğü satırıyla gereksinim olur ya da neden olmadığını yazarsınız.

---

## Walk-through'dan sonra — dersin sonuna (11:45) kadar

**`week04/group_04.json`**: tek bir kayıt, collaborator'ınız, rol `collaborator`, öğrenci numarası (sizinki değil) ve **bulduğu ya da söylediği en yararlı şey, alıntı olarak**, onun sözleriyle, sizin yazdığınız. Sizi geri yazması gerekmez.

`accepted` ve `why`, neyi değiştirdiğinizi bildiğiniz Cumartesi'ye kadar bekleyebilir.

```bash
python .github/check_deliverables.py
git add .
git commit -m "week04: prototype, test cases, walk-through"
git push
```

Son push **dersin sonunda (11:45)**. Hemen ardından bütün repoları dondururum.

---

## Cumartesi'ye kadar — düzeltin, yeniden yürütün, güncelleyin

- **Her `fail`'i düzeltin.** Genellikle prototip değişir; bazen yanlış olan test case ya da gereksinimdir.
- **Collaborator'ınızla çevrim içi ikinci tur.** Ekranınızı paylaşın; collaborator'ınız `fail` olan her test case'in adımlarını okur, siz tam olarak söylediğini tıklarsınız: `walkthrough_04.json` içinde `"round": 2`, sizin yazdığınız. Collaborator'ınız grubunuzdaysa grup toplantınız bunun için doğal yerdir; değilse ikinizin seçeceği herhangi bir görüşme olur.
- **`requirements.json` ve `test_cases.json` dosyalarını güncelleyin.** Her değişiklik, Değişiklik günlüğünde kimlikleri anan tarihli bir satır alır:

`2026-10-14 — REQ-011 eklendi: collaborator'ım ayırmayı iptal etmenin bir yolunu aradı ve bulamadı; TC-011-01 yazıldı.`

---

## Cumartesi'ye kadar — akışın tamamı

Her işlevsel `must` gereksinimin ona hizmet eden bir ekranı vardır. **En az yedi ekran.** Renkler ve yazı tipleri önemli değildir; önemli olan akıştır.

**5. haftanın sonu: `requirements.json` + `test_cases.json` = taban çizginiz (baseline).** Ondan sonra bir değişiklik, bir değişiklik isteğiyle (change request) yapılır.

5. haftadan itibaren test case'leriniz otomatik testlere dönüşür ve her testin adı kendi kimliğini taşır: `test_TC_002_02_busy_slot_is_refused`.

---

## S1 — geliştirici hesabınızı bugün açın

Kimlik kontrolü **bir günden bir haftaya kadar** sürer ve sonraki hiçbir adım o olmadan başlayamaz.

| Mağaza | Ücret | Ne kadar sürer |
|---|---|---|
| Google Play | ≈ 25 $, bir kez | birkaç gün |
| Huawei AppGallery | ücretsiz | 1–2 iş günü |
| Samsung Galaxy Store | ücretsiz | birkaç gün |
| Apple App Store | ≈ 99 $, her yıl | ödemeden sonra bir iki gün |

**Google Play:** yeni bir kişisel hesap, Play Console uygulamasıyla bir kez **gerçek bir Android telefonda** onay verir; emülatör kabul edilmez. Android telefonunuz yok mu? Bir arkadaşınızınkini bir dakikalığına ödünç alın.

---

## `week04/store.json` — ve verileriniz

Mağazayı, başvuru tarihinizi, geliştirici adınızı ve durumu doldurun: bu hafta `applied` yeterlidir.

Geliştirici konsolunuzun ya da başvurunuzun **ekran görüntüsünü** `week04/` içine kaydedin. Kaydetmeden önce **adresinizi, kimlik numaranızı ve kart bilgilerinizi kapatın**.

**Reponun hiçbir yerinde şifre, kart numarası ya da kimlik numarası olmaz.**

Ücret konusunda karar sizindir. Huawei AppGallery ve Samsung Galaxy Store ücretsizdir.

---

## Cumartesi'ye kadar — yapay zeka günlüğü, `week04/ai_log_04.md`

**Önce kabul ölçütü.** Asistanınızın yaptığı bir ekranı seçin.

1. İstemden **önce** yazdığınız REQ satırları ve test case kimlikleri.
2. Cevabın her birine göre ölçülmesi: neyi karşıladı, neyi bozdu, ne ekledi.
3. Neyi değiştirdiğiniz: istemi, ekranı elle ya da `requirements.json`'ı.
4. Yapıştırılmış konuşma, `ME:` ve `AI:` altında.

**Günlüğü kendiniz yazın: AI log'u bir insan yazar.** Sizin sözleriniz düz, asistanın sözleri kalın ve yalnızca ondan gelmesi gereken yerde. Evidence bloğunun ve bu kalın alıntıların dışında, dil için bile asistan yok. Asistana yazdırılmış bir günlük 0 puan alır.

---

## 4. Hafta nasıl notlanır — 10 puan

| | Puan | Ne |
|---|---|---|
| Ders sonu (11:45) | 5 | prototip, test case'ler, walk-through, collaborator'ınızdan alıntılanmış bir bulgu |
| Cumartesi denetleyicisi | 2 | ikinci tur, güncellemeler, yedi ekran, S1, yapay zeka günlüğü |
| İnsan katılımı | 2 | yapay zeka günlüğü; collaborator'ınızın söylediklerinin sizin elle yazdığınız kaydı; gerçek bulgular, gerçek kararlar |
| Commit düzeni | 1 | derste birkaç push (en az 3); çalıştıkça birkaç commit |

Adını yazdığınız collaborator haftalık notunuzun %10'unu kazanır; sizi yazan sınıf arkadaşınız için yürüttüğünüz testler için siz de. S1 mağaza bonusuna da sayılır.

---

## Gelecek hafta: tasarım ve ilk gerçek kod

**5. hafta:** tasarım ve API sözleşmesi (sunucunuzun neye ve nasıl cevap verdiğinin listesi), sunucu iskeleti ve uçtan uca çalışan e-posta kodu ile giriş.

5. haftanın sonunda gereksinimleriniz ve test case'leriniz **taban çizginiz (baseline)** olur.

---

## Toparlama — ilk şablondan kalanlar

26 Eylül'den önce açılmış bir repoda şunlar duruyor. Artık hiçbir şey onları okumuyor; içlerine kendi dosyanızı koymadıysanız hepsini silin.

- `requirements/` → artık `weekNN/requirements.txt`
- `docs/` → artık kökte `AI_Doc1`–`AI_Doc4` ve `AI_Doc2_media`
- `SETUP_CARD_EN.md`, `SKELETON.md`, `WEEKLY_WORKFLOW_STUDENT_EN.md` → artık başında `AI_` ile
- `CURRENT_WEEK.txt` → checker dersin kopyasını ağdan okuyor; sizdeki etkisiz

```
git rm -r --ignore-unmatch requirements docs CURRENT_WEEK.txt \
  SETUP_CARD_EN.md SKELETON.md WEEKLY_WORKFLOW_STUDENT_EN.md
git commit -m "ilk şablondan kalanları kaldır"
```

---

## Sınıfla ilgili iki kural

**Bir öğrenci, bir bilgisayar, bir GitHub hesabı.** Bir arkadaşınızın bilgisayarında ya da onun oturumunda yapılan iş ders için puan kazanmaz. Walk-through'da collaborator'ınız sizin bilgisayarınızı kullanır; reponuza yazılan her şeyi siz yazarsınız.

**Yoklama sisteminde kayıtlı değilseniz gelmemiş sayılırsınız.** Ders slotunun beş puanı o zaman gider, ne push edilmiş olursa olsun.

---

## Şimdi

Denetleyiciyi çalıştırın. `week04/prototype/` gelir.

**Köşeli parantezli kısımları değiştirin, sonra ana akışınızı `home.html`'den itibaren kurun.**

<!-- Saati başlatın. 10:30 civarına kadar yapım, 11:30 civarına kadar walk-through, 11:45'e kadar dosyalar ve push. 11:45'ten hemen sonra dondurma: push.md blok 3. -->
