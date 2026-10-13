# 4. Hafta Ödevi — Tıklanabilir Prototip ve Test Case'ler

**Teslim:** ders içi bölüm dersin sonuna kadar (11:45) · kalanı Cumartesi 23:59 · Proje reponuza commit edin

> ## AI log'u (yapay zeka günlüğü) insan yazar. İstisna yok.
>
> `week04/ai_log_04.md` dosyasını **siz**, kendi cümlelerinizle yazarsınız. Evidence bloğunun ve
> cevabından yaptığınız kalın alıntıların (§9) dışında asistan kullanılmaz: ne yazmak için, ne
> "düzeltmek" için, dil için bile. **Asistana yazdırılmış bir günlük 0 puan alır.** Dil notlanmaz;
> her günlüğü bir insan okur.

> ## Collaborator'ınızın söylediklerini elle yazarsınız. Asistan yok, dil bilgisi için bile.
>
> Bu hafta sınıftan seçtiğiniz bir arkadaşınız, yani **collaborator**'ınız prototipinizi test eder.
> Onun söylediklerine ilişkin kağıt notlarınızı, `walkthrough_04.json` içindeki notları, ondan
> alıntıladığınız cümleyi ve `group_04.json` içindeki kararlarınızı **siz**, kendi cümlelerinizle
> yazarsınız. Bunları hiçbir asistan yazmaz, çevirmez ya da düzeltmez; bir virgül için bile.
> Türkçeniz ya da İngilizceniz notlanmaz; her kaydı bir insan okur.

> **Dersten önce:** `week02/requirements.json` dosyanızı açın ve hangi gereksinimlerinizin
> `must` olduğunu not edin. Sonra **ana akışınıza** karar verin: kullanıcının
> giriş yapmaktan uygulamanızın var olma nedeni olan tek işe kadar izlediği yol. StudyRoom
> için bu yol şöyledir: giriş → bugünün boş odalarını görme → oda ayırma → ayırmayı görme.

Geçen hafta gereksinim kimlikleriniz kalıcı oldu. Bu hafta gereksinimlerinizi ekran olarak
görürsünüz ve başka biri onları test eder. Ana akışınızın tıklanabilir bir prototipini yaparsınız, kabul
ölçütlerinizi test case'lere dönüştürürsünüz ve seçtiğiniz bir sınıf arkadaşınız, yani
collaborator'ınız, bu test case'leri prototipiniz üzerinde yürütür.

Neden şimdi, henüz hiç kod yokken? Kimse bir ürünü görmeden onun bütün gereksinimlerini
yazamaz. Başka biri ekranlarınızda gezinirken orada olmayan bir düğmeyi arar ya da
hiçbir gereksinimin söz etmediği bir mesajı bekler. Bunların her biri eksik ya da belirsiz
bir gereksinimdir ve onu bugün bulmak size bir ekrana mal olur. 8. haftada bulmak ise sunucuyu
ve iki istemciyi birden değiştirmek demektir.

---

## Bu hafta gelenler

Denetleyiciyi bir kez çalıştırın:

```bash
python .github/check_deliverables.py
```

`week04/prototype/` (üç başlangıç ekranı, `style.css` ve kuralları anlatan bir
`README.md`), `week04/test_cases.json`, `week04/walkthrough_04.json`,
`week04/group_04.json` (bu hafta collaborator'ınızı içerir), `week04/store.json` ve
`week04/ai_log_04.md` gelir.

---

## Bu hafta asistan nerede yardım eder, nerede etmez

| Parça | Asistan |
|---|---|
| Her ekranın HTML ve CSS'i (REQ satırları isteme yapıştırılır; bir ekran, bir commit) | **Yardım eder** |
| Kabul ölçütlerinizden test case taslağı (her birini kendi ölçütüyle siz karşılaştırırsınız) | **Yardım eder**, onay sizde |
| Ölçütlerinizden önerilen uydurma veriler | **Yardım eder**, onay sizde |
| Bir `fail` sonrası prototipi düzeltmek | **Yardım eder** |
| Ana akışınızı seçmek ve istemden önce ölçütleri yazmak: ekran hangi gereksinimleri karşılamalı | **Yardım yok**: siz karar verirsiniz |
| Collaborator'ınızın söyledikleri: kağıt notlarınız, `walkthrough_04.json` içindeki notlar, alıntıladığınız cümle, `group_04.json` içinde `accepted` ve `why` | **Hiç yardım yok, dil bilgisi ve çeviri de dahil**: kendi elinizle yazarsınız |
| Değişiklik günlüğü satırları ve her `fail` için kararınız | **Yardım yok** |
| `ai_log_04.md` (Evidence bloğu ve kalın alıntılar dışında) | **Yardım yok** |
| `store.json`, geliştirici hesabı, ekran görüntüsü | **Yardım yok** |

---

## Derste — dersin sonuna (11:45) kadar push edilir

Ders üç bölümdür. Yaklaşık 25 dakika anlatım; sonra 10:30 civarına kadar yaparsınız
(10:00'da, iş hangi durumdaysa push); sonra 11:30 civarına kadar collaborator'ınızla walk-through
(11:00'de push; 11:00 sizin turunuza denk gelirse turunuz biter bitmez); son on beş dakika da dosyalarınız, denetleyici ve dersin sonundaki (11:45) push için.

### 1. Prototip — `week04/prototype/`

Prototip, uygulamanın daha hiçbir parçası yapılmadan nasıl kullanılacağını gösterir.
Sunucu yoktur ve veriler uydurmadır; gerçek olan akıştır: hangi ekranın hangisinden sonra
geldiği, her ekranın ne istediği ve bir şey ters gittiğinde kullanıcının ne gördüğü.

- **Her ekran için bir HTML dosyası**, hepsi `week04/prototype/` içinde. İlk ekran
  `index.html`'dir. Çift tıklayınca açılır: sunucu yok, framework yok, derleme adımı yok.
- **Her ekrana `index.html`'den tıklayarak ulaşılır** ve her bağlantı var olan bir ekrana
  gider.
- **Her ekranın üst kısmında, hizmet ettiği gereksinimleri söyleyen bir yorum vardır**:
  `<!-- serves: REQ-002, REQ-006 -->`. Bir ekran, var olma nedeni olan gereksinime böyle
  bağlanır. Telefon ekranı gereksiniminiz REQ-006 değilse, başlangıç ekranlarındaki ve
  TC-006-01'deki REQ-006'yı onun kimliğiyle değiştirin.
- **Bağlantılar dosyanın tam adını küçük harfle ve tırnak içinde kullanır**:
  `href="rooms.html"`. Denetleyici yalnızca böyle yazılmış bağlantıları izler.
- **Uydurma veriler sabittir**, böylece collaborator'ınız bir test case'i adım adım
  izleyebilir: `code.html` içinde doğru kod her zaman 1234'tür. Kendi uydurma
  değerlerinizi `prototype/README.md` dosyasına yazın (StudyRoom için: "Oda 3, 14:00 ile
  15:00 arasında dolu").
- **Uydurma verileri kabul ölçütlerinizden seçin.** Bir test case, ihtiyaç duyduğu
  değerler varsa yürütülebilir: boş bir saat ve dolu bir saat, doğru bir kod ve yanlış bir
  kod, boş bir liste ve kayıtlı bir liste, sınır değerleri (30 ve 120 dakika).
  Asistanınızdan bunları ölçütlerinize göre önermesini isteyin, kendiniz onaylayın,
  `prototype/README.md` içindeki "Invented data" bölümüne yazın ve her ekranda aynı
  değerleri kullanın. Veriyi orada bulamayan collaborator test case'i yürütemez ve sonuç
  `blocked` olur. Gerçek ad ya da e-posta adresi kullanmayın.
- **Sunucu olmadığı için bir ekran hiçbir şeyi hatırlamaz.** Kullanıcı bir saat
  ayırttıktan sonra bir sonraki ekran, aynı sabit veriyi o rezervasyon zaten içinde olacak
  şekilde gösterir.
- Üç başlangıç ekranı (`index.html`, `code.html`, `home.html`) herkesin ortak girişidir
  (REQ-001). Köşeli parantezli kısımlarını değiştirin, sonra ana akışınızı `home.html`'den
  itibaren kurun: `week03/screens_03.md` dosyasında listelediğiniz ekranlar, her satır için
  bir HTML dosyası.

**Dersin sonuna (11:45) kadar en az beş ekran**: üç başlangıç ekranı ve en az iki ekran da sizin.
Akışın geri kalanı Cumartesi'ye kadar tamamlanır.

**Prototipi asistanınızla yapın, ama önce ölçütlerinizi verin** (`AI_Doc5` §1). Bir ekran
istemeden önce, o ekranın karşılaması gereken REQ satırlarını kabul ölçütleriyle birlikte
isteme yapıştırın. Sonra cevabı bunlarla karşılaştırın. Asistanlar hiçbir gereksinimin
istemediği şeyler eklemeyi sever: bir giriş ekranında şifre alanı ve "Google ile giriş"
düğmesi (ikisi de REQ-001'e aykırı), 480 px genişliğinde bir yerleşim (REQ-006'ya aykırı),
bir şey ters gittiğinde hiçbir mesaj göstermeyen bir ekran. Bu konuşmalardan birini
saklayın; bu haftanın yapay zeka günlüğü odur.

**Ekranları asistanınız yazar; ne yapacaklarına siz karar verirsiniz.** Akış, uydurma
veriler ve her ekranın kontrolü sizindir. Asistana düz HTML ve CSS kullanmasını, her ekran
için ayrı bir dosya yazmasını, ortak `style.css` dosyasını kullanmasını ve framework
kullanmamasını söyleyin: React ile ya da içeriğini değiştiren tek bir sayfayla cevap veren
bir asistan, denetleyicinin izleyemeyeceği bir şey verir. Bir seferde tek ekran isteyin,
tarayıcıda açın, ölçütlerinizle karşılaştırın ve bir sonrakini istemeden önce commit edin:
bir ekran, bir commit.

### 2. Test case'ler — `week04/test_cases.json`

Test case, herkesin izleyebileceği adımlara ve herkesin kontrol edebileceği bir sonuca
dönüştürülmüş tek bir kabul ölçütüdür. StudyRoom'un bir gereksinimi iki test case'e şöyle
dönüşür:

| | |
|---|---|
| **REQ-002** | Bir öğrenci bir odada boş olan 30 ile 120 dakika arası bir zaman dilimini ayırır. |
| **Kabul ölçütü** | Boş bir dilim için yapılan ayırma kaydedilir ve dolu görünür; dolu bir dilim için yapılan ayırma bir mesajla reddedilir. |
| **TC-002-01** | *Ön koşul:* giriş yapılmış. *Adımlar:* Odalar'ı açın; Oda 3, bugün, 16:00–17:30'u seçin; Ayır'a dokunun. *Beklenen:* "Ayrıldı: Oda 3, 16:00–17:30" görünür ve dilim dolu gösterilir. |
| **TC-002-02** | *Ön koşul:* Oda 3, 14:00 ile 15:00 arasında dolu. *Adımlar:* Oda 3, bugün, 14:00–15:00'ı seçin; Ayır'a dokunun. *Beklenen:* "Bu dilim dolu" mesajı görünür ve hiçbir şey ayrılmaz. |

Kurallar:

- **Her `must` gereksinimin en az bir test case'i vardır.** Bunları derste yazın, çünkü
  collaborator'ınız dersin sonundan (11:45) önce onları yürütür.
- **Kimlik, hangi gereksinimi test ettiğini söyler**: TC-002-01 ve TC-002-02 ikisi de
  REQ-002'yi test eder. REQ kimliklerinde olduğu gibi, bir test case kimliğinin anlamı
  hiçbir zaman değişmez.
- **Adımlar gerçek değerler kullanır** ("bir oda ve bir saat" değil, "Oda 3, 16:00–17:30")
  ve **beklenen sonuç, test edenin görebileceği bir şeydir** ("çalışır" değil, "'Bu dilim
  dolu' mesajı").
- **Cumartesi'ye kadar en az üç gereksinimin, bir şey ters gittiğinde ne olacağını test
  eden bir test case'i de olur**: yanlış bir kod, boş bir alan, zaten dolu bir dilim.
  Dosyadaki TC-001-02 bunların ilkidir.

Asistanınız test case'leri kabul ölçütlerinizden taslak olarak yazabilir. Her birini kendi
ölçütüyle karşılaştırın: ölçütün söylediğini mi test ediyor, yoksa asistanın uydurduğu
bir şeyi mi? Hiçbir gereksinimin anlatmadığı bir davranışı test eden bir test case ya
eksik bir gereksinimdir (yeni bir kimlikle `requirements.json`'a ekleyin ve Değişiklik
günlüğüne bir satır yazın) ya da silinmesi gereken bir test case'tir.

ZAYIF: *"TC-002-01 — Ayırma çalışıyor. Adımlar: bir oda ayır. Beklenen: başarılı."*
GÜÇLÜ: yukarıdaki tablodaki iki satır.

### 3. Walk-through — collaborator'ınızla

**Collaborator'ınız**, kendi dersinizden, herhangi bir gruptan seçtiğiniz tek bir sınıf
arkadaşınızdır. Walk-through başlamadan önce kim olduğunu aranızda kararlaştırın. İki arkadaş
çoğu zaman birbirini seçer ve sırayla test eder, ama bu zorunlu değildir. Her prototipe
yaklaşık on iki dakika düşer.

- **Prototipin sahibi** (siz) prototipi kendi bilgisayarında 390 px genişlikte açar (F12,
  sonra telefon simgesi), collaborator'ınıza `prototype/README.md` içindeki uydurma verileri
  gösterir ve bilgisayarı ona verir. Bundan sonra sahip yalnızca izler; açıklama yapmaz,
  yardım etmez. Sahip her yürütmeyi, collaborator'ın en yararlı cümlesiyle birlikte kağıda
  not eder ve tur biter bitmez `walkthrough_04.json` dosyasına yazar.
- **Collaborator'ınız** bir test case'in adımlarını yüksek sesle okur, tam olarak
  söylediklerini yapar ve ne gördüğünü söyler. Test case'lerinizden **en az dördünü**
  yürütür ve bunlardan en az ikisi girişe değil, ana akışa aittir.
- **Her yürütmenin tek bir sonucu vardır.** `pass`: collaborator "expected" alanında yazanı
  gördü. `fail`: görmedi; not, onun yerine ne gördüğünü söyler. `blocked`: prototip
  üzerinde kontrol edilemez; örneğin "kod bir dakika içinde gelir" gerçek sunucu ister ve
  5. haftadan itibaren gerçek sistem üzerinde kontrol edilir. Henüz var olmayan bir
  ekran `fail`'dir.

Prototip sizin özel reponuzda olduğu için collaborator sizin bilgisayarınızda çalışır.
Buna izin vardır: reponuza yazan yine sizsiniz.

**Collaborator'ınızın söylediklerini elle yazarsınız.** Kağıt notlarınız, `walkthrough_04.json`
içindeki notlar, alıntıladığınız cümle ve kararlarınız sizin tarafınızdan, kendi cümlelerinizle
yazılır. Hiçbir asistan bunları yazmaz, çevirmez ya da düzeltmez: dil bilgisi için de, Türkçe
ya da İngilizce için de, bir virgül için bile. Collaborator'ınızın söylediğini söylediği gibi
yazın. Türkçeniz ya da İngilizceniz notlanmaz; her kaydı bir insan okur.

**Geri dönüş collaborator'ınızdan gelir, başka kimseden değil.** `walkthrough_04.json`
içindeki her yürütmenin `tester` alanındaki öğrenci numarası onundur ve aynı numara
`group_04.json` içindedir.

**Bir `fail` yüzünden kimse puan kaybetmez.** Puanlar, test case'leri dürüstçe yürütmek ve
her `fail` için ne yaptığınız içindir. Öteki tür bulguya da kulak verin: "Ayırmayı iptal
etmenin bir yolunu aradım." Bunu hiçbir test case kapsamaz, çünkü hiçbir gereksinim bunu
istemez. Bir nota yazın; Cumartesi'ye kadar gereksinim olup olmayacağına siz karar
verirsiniz.

### 4. `week04/group_04.json` — collaborator'ınız

Dosya 3. Hafta'daki adını korur, ama bu hafta **tek bir kayıt** içerir: collaborator'ınız,
rol `collaborator`, 9 haneli öğrenci numarasıyla (sizinki değil). Onun için **bulduğu ya da
söylediği en yararlı şey, tam bir cümle olarak alıntılanmış**, onun sözleriyle, sizin yazdığınız.
`accepted` ve `why` alanları, neyi değiştirdiğinizi bildiğiniz Cumartesi'ye kadar bekleyebilir.
Collaborator'ınızın sizi geri yazması gerekmez ve yazmazsa puan kesilmez. Adını yazdığınız
collaborator katkı bonusu kazanır.

### 5. Push

```bash
python .github/check_deliverables.py
git add .
git commit -m "week04: prototype, test cases, walk-through"
git push
```

10:00'da, 11:00'de ve dersin sonunda, **11:45**'te push edin. Hemen ardından bütün
repoları dondururum. Push edilmemiş olan yoktur.

---

## Cumartesi 23:59'a kadar

### 6. Düzeltin, yeniden yürütün, güncelleyin

- **Her `fail`'i düzeltin.** Genellikle prototip değişir. Bazen yanlış olan test case ya da
  gereksinimdir: o zaman onu değiştirin ve nedenini Değişiklik günlüğüne yazın.
- **Collaborator'ınızla çevrim içi ikinci tur.** `fail` olan her test case, düzeltmeden sonra
  yeniden yürütülür: düzeltilmiş prototipi ekran paylaşımıyla açarsınız, collaborator'ınız
  `fail` olan her test case'in adımlarını yüksek sesle okur ve siz tam olarak söylediğini
  tıklarsınız. Collaborator'ınız grubunuzdaysa grup toplantınız bunun için doğal yerdir; değilse
  ikinizin seçeceği herhangi bir görüşme olur. Bu yürütmeleri `walkthrough_04.json` dosyasına
  `"round": 2` ile, kendi elinizle yazarak ekleyin. Bunun yerine çıkardığınız (`"dropped": true`,
  Değişiklik günlüğünde bir satırla) bir test case'in ikinci tura ihtiyacı yoktur.
- **`requirements.json` ve `test_cases.json` dosyalarını** walk-through'un gösterdiklerine
  göre güncelleyin: eksik olan bir gereksinim (yeni bir kimlikle), belirsiz olan bir kabul
  ölçütü, eksik olan bir test case. Her değişiklik, `PROPOSAL.md`'nin Değişiklik
  günlüğünde kimlikleri anan **tarihli bir satır** alır:
  "2026-10-14 — REQ-011 eklendi: collaborator'ım ayırmayı iptal etmenin bir yolunu aradı ve
  bulamadı; TC-011-01 yazıldı."

İki dosya bir hafta daha değişebilir. 5. haftanın sonunda **taban çizginiz (baseline)**
olurlar. Ondan sonra her değişiklik bir değişiklik isteği (change request) gerektirir:
değişikliği ve etkilediği her dosyayı söyleyen kısa, yazılı bir istek.

### 7. Ekran akışının tamamı

Her işlevsel `must` gereksinimin ona hizmet eden en az bir ekranı vardır ve her ekran
gereksinimlerini `serves:` yorumunda söyler. Toplamda **en az yedi ekran** gerekir.
Renkler ve yazı tipleri önemli değildir; önemli olan akıştır.

### 8. S1 — geliştirici hesabınız, `week04/store.json`

Teklifinizin §12'sinde adını verdiğiniz mağazada geliştirici hesabınızı açın ve bunu
**dersin olduğu gün** yapın: kimlik kontrolü bir günden bir haftaya kadar sürer ve sonraki
hiçbir adım o olmadan başlayamaz. 3. haftada başvurduysanız `store.json` dosyasına o tarihi ve
hesabınızın şu anki durumunu yazın.

| Mağaza | Ücret | Ne istiyor | Kontrol ne kadar sürer |
|---|---|---|---|
| Google Play | yaklaşık 25 $, bir kez | bir Google hesabı ve ödeme profilinizle uyuşan bir kimlik belgesi. Yeni bir kişisel hesap ayrıca bir kez, Play Console uygulamasıyla, gerçek bir Android telefonda (Android 10 ya da sonrası; emülatör kabul edilmez) onay verir. Android telefonunuz yok mu? Bir arkadaşınızınkini bir dakikalığına ödünç alın. | birkaç gün |
| Huawei AppGallery | ücretsiz | bir Huawei ID, kimlik kartı ya da pasaport ve bir banka belgesi | 1–2 iş günü |
| Samsung Galaxy Store | ücretsiz | bir Samsung hesabı ve Seller Portal kaydı | birkaç gün |
| Apple App Store | her yıl yaklaşık 99 $ | iki adımlı doğrulamalı bir Apple ID, bir kimlik kontrolü ve ödeme | genellikle ödemeden sonra bir iki gün |

`store.json` dosyasını doldurun: mağaza, başvuru tarihiniz, geliştirici adınız ve durum (bu
hafta için `applied` yeterlidir). Geliştirici konsolunuzun ya da başvurunuzun ekran
görüntüsünü, adresiniz, kimlik numaranız ve kart bilgileriniz kapatılmış olarak `week04/`
içine kaydedin ve dosya adını `evidence` alanına yazın. **Reponun hiçbir yerine şifre, kart numarası ya da kimlik numarası
yazmayın.** Ücret ödeyip ödememek sizin kararınızdır: Huawei AppGallery ve Samsung Galaxy Store
ücretsizdir.

### 9. Önce kabul ölçütü — `week04/ai_log_04.md`

Asistanınızın yaptığı bir ekranı seçin. İstemden önce, o ekranın karşılaması gereken REQ
satırlarını ve üzerinde yürütülecek test case'leri yazmıştınız. Bunları, cevabın her
birine göre ölçülmüş halini ve neyi değiştirdiğinizi gösterin. Yönergeler ve bir
zayıf/güçlü örnek dosyanın içindedir. **AI log'u bir insan yazar: siz.** Evidence bloğunun ve aşağıdaki kalın alıntıların dışında asistan kullanılmaz; ne yazmak için, ne düzeltmek için, dil için bile. **Asistana yazdırılmış bir günlük 0 puan alır.**

İki tür söz var ve okuyan hangisinin hangisi olduğunu görmeli. Sizin sözleriniz düz yazıdır: her kelime, dil bilgisi de. Asistanın sözleri kalındır ve yalnızca asistandan gelmesi gereken yerde: cevabında işaret ettiğiniz bir ifade ya da tek cümle (ne iddia etti, ne ekledi); örneğin: cevap şu cümleyle bitti: **Tüm gereksinimler karşılandı**. Her kalın ifade Evidence bloğunda da harfi harfine bulunmalı. Kalın yazı başka hiçbir şey için kullanılmaz: vurgu, başlık ya da etiket için değil. Evidence bloğunda isteminiz `ME:` altına, cevap hiç dokunulmadan `AI:` altına yazılır.

### 10. Yeniden push, denetimler yeşil

Çalıştıkça yapılan, her birinde biraz yeni iş ve ne değiştiğini söyleyen bir mesaj olan commit'ler; bir commit'in bitmiş bir parça olması gerekmez. Denetleyicinin
istediklerinin hepsi aşağıdadır.

---

## Teslim listesi

**Derste, dersin sonuna (11:45) kadar**
- [ ] `week04/prototype/` — `index.html` dahil en az beş ekran, hepsine tıklayarak ulaşılıyor, köşeli parantezli kısım kalmamış
- [ ] `week04/test_cases.json` — her `must` gereksinim için en az bir test case
- [ ] `week04/walkthrough_04.json` — collaborator'ınız test case'lerinizden en az dördünü, en az ikisi ana akıştan olmak üzere yürüttü; her `fail` ve `blocked` için bir not; sizin yazdığınız, elle
- [ ] `week04/group_04.json` — collaborator'ınız (tek kayıt), ondan alıntılanmış bir bulgu; sizin yazdığınız, elle

**Cumartesi'ye kadar**
- [ ] `fail` olan her test case ikinci turda yeniden yürütüldü ya da Değişiklik günlüğünde bir satırla çıkarıldı
- [ ] `requirements.json` ve `test_cases.json` güncellendi; kimlikleri anan bir Değişiklik günlüğü satırı
- [ ] En az yedi ekran; her işlevsel `must` gereksinimin bir ekranı var; her ekranın `serves:` yorumu var
- [ ] En az üç gereksinimin, bir şey ters gittiğinde ne olacağını test eden bir test case'i var
- [ ] `group_04.json` — collaborator'ınızın bulgusu için `accepted` ve `why` kararı verildi; sizin yazdığınız, elle
- [ ] `week04/store.json` — S1 dolduruldu, ekran görüntüsü kaydedildi
- [ ] `week04/ai_log_04.md` — ölçütleriniz, cevabın onlara göre ölçülmesi, konuşma yapıştırılmış; sizin yazdığınız, asistanın değil (asistana yazdırılan 0 alır)
- [ ] GitHub'da denetimler yeşil; 1–3. haftalar hala geçiyor

---

## Bu hafta yok

Henüz sunucu kodu ve tasarım belgesi yok (ikisi de 5. haftada). Prototip için framework
yok: React, Flutter ve diğerleri gerçek istemcilerle gelir. Gerçek e-posta gönderilmez;
kod 1234'tür.

---

## Bu hafta nasıl notlanır

**Dersin sonu — 5 puan.** Prototip, test case'ler, collaborator'ınızla yapılmış walk-through ve
ondan alıntılanmış bir bulgu; reponuzun dersin sonundaki (11:45) halinden okunur.

**Cumartesi 23:59 — 5 puan.** Son halinizde denetimlerin yeşil olması: **2**. İnsan
katılımı: **2**; yani kanıtıyla birlikte, sizin yazdığınız `ai_log_04.md` (asistana yazdırılmış günlük **0** alır), collaborator'ınızın söylediklerinin sizin elle yazdığınız kaydı ve arkasında gerçek kararlar olan
gerçek bulgular. Commit düzeni: **1**; yani derste farklı zamanlarda birkaç push (en az üç) ve
çalıştıkça yapılan birkaç commit; her birinde biraz yeni iş olsun.

**S1**, 3. haftadaki S0 gibi mağaza bonusunun notlanan adımlarından biridir.

**Katkı bonusu.** Adını yazdığınız collaborator haftalık notunuzun %10'unu kazanır;
siz de sizi yazan sınıf arkadaşınız için yürüttüğünüz test case'ler için aynısını kazanırsınız.

**Bir öğrenci, bir bilgisayar, bir GitHub hesabı.** Bir arkadaşınızın bilgisayarında ya da
onun oturumunda yapılan iş ders için puan kazanmaz. Walk-through tek istisnadır: collaborator'ınız
sizin bilgisayarınızı kullanır, sonuçları siz yazarsınız.
