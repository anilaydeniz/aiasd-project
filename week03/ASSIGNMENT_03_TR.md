# 3. Hafta Ödevi — Sunum, Akran İncelemesi, Teklif Bölüm B

**Teslim:** ders içi bölüm dersin sonuna kadar (11:45) · kalanı Cumartesi 23:59 · Proje reponuza commit edin

> **Dersten önce:** `PITCH_03.md` dosyanız yazılmış ve push edilmiş olmalı. Dersin ilk
> saati onu sunmakla geçer — o sırada yazacak zaman yok. Bilgisayarınızı şarjı dolu
> getirin; sunumu ondan yapacaksınız.
>
> **Bu derste projeniz kesinleşir: başlığı ve içeriği.** Dönemin geri kalanında onun
> üzerinde çalışacaksınız; bu karara bugün, grubunuzla, gereken zamanı ayırın. Derse
> sorgulanmaya hazır bir projeyle gelin, hâlâ aradığınız bir projeyle değil.

Geçen hafta ne yapacağınıza karar verdiniz. Bu hafta üç sınıf arkadaşınız bu karar
hakkında ne düşündüğünü söyler, siz neyi değiştireceğinize karar verirsiniz ve teklifin
ikinci yarısını yazarsınız — neden yapmaya değer olduğunu ve sizi neyin durdurabileceğini
anlatan yarısını.

---

## Bu hafta gelenler

Denetleyiciyi bir kez çalıştırın:

```bash
python .github/check_deliverables.py
```

`week03/PITCH_03.md`, `week03/group_03.json`, `week03/contributors_03.json`,
`week03/screens_03.md` ve `week03/ai_log_03.md` gelir.
`PROPOSAL.md` zaten sizde; Bölüm B (§8–§12) ve Değişiklik günlüğü onun içinde, sizi
bekliyor.

---

## Dersten önce — `week03/PITCH_03.md`

Beş dakikalık sunumunuz, altı slayt, Markdown olarak: dosya sunumun **kendisidir**, her
`---` yeni bir slayttır. VS Code'da açın; **Marp for VS Code** eklentisi onu slayt olarak
gösterir (sağ üstte önizleme düğmesi) ve isterseniz PDF ya da PPTX'e aktarır. Eklenti
olmadan VS Code'un normal Markdown önizlemesi de sunum için yeterlidir.

Altı slayt, her birinin yönergesi dosyanın içinde:

1. ürün tek cümleyle;
2. **sorun en son ne zaman oldu** — size ya da gözünüzün önünde — tarih, yer, kim, onun yerine ne yaptı;
3. **9. haftada test edecek beş gerçek kişi** — ad, nereden tanıdığınız;
4. yaptığı üç şey, yapmadığı bir şey;
5. ana ekran, **elle çizilmiş** (fotoğraf `week03/` içinde) ya da metinle;
6. emin olmadığınız tek şey.

7. slayt sabittir: değerlendirenlerinizin cevaplayacağı üç soru.

**Kendiniz yazın — bu dosyada yapay zekâ yok.** Ne metin, ne yapı. Bu slaytlardaki her
şey sizin hayatınız ve sizin çevreniz hakkında; bir asistan bunu bilemez ve ben grupta ya
da derste herhangi bir slaytı sorabilirim. Haftanın geri kalanı farklı: orada yapay zekâ
her zamanki gibi bir araçtır ve `ai_log_03.md` onu kullanmanızı ister.

2. ve 3. slaytların arkasında iki kural var ve dönem boyunca geçerli: **proje sizin bir
sorununuzu çözer — kendinizin, üniversitedeki arkadaşlarınızın ya da sosyal çevrenizin**
ve **çevrenizdeki gerçek kişiler tarafından kullanılabilir** — Atlas'ta, ailenizde, bir
kulüpte — çünkü 9. haftada o kişiler test edecek ve onlara ihtiyacınız olacak. Sorunun en
son ne zaman olduğunu ya da ürünü kullanacak beş kişiyi
söyleyemiyorsanız sorun slaytta değil projededir: projeyi bu derste değiştirin.

**Dersin sonunda (11:45) projeniz dönem için kesinleşir: başlığı ve içeriği.** Dönem sonuna kadar
aynı başlık, aynı problem ve aynı ürün. Ayrıntıları (özellikler, gereksinimler, kapsam) her
biri Değişiklik günlüğünde bir satırla değişmeye devam edebilir; projenin kendisi
değişemez. Bu, dönemin en önemli kararıdır; ona zaman ayırın: projeyi inceleme turunda
sınayın, sonra grubunuzun cevapları önünüzdeyken §1'i (başlık) ve §3–§4'ü (problem ve
ürün) kesinleştirmek için turdan sonra en az yarım saat ayırın. Grubunuza projenin gerçek
olup olmadığını ve bitirilip bitirilemeyeceğini sorun.
Bugünden sonra yalnızca teknik olarak imkânsız çıkan bir proje değişebilir; o da ancak
benim bir issue'da yazılı onayımla.

---

## Derste — dersin sonuna (11:45) kadar push

### 1. İnceleme turu — dörtlü gruplar, ilk saat

Dört kişilik grubunuzu dersin başında kendiniz kurarsınız. Sınıf dörde bölünmüyorsa artan
öğrenciler bir gruba katılır ve o grup beş kişi olur; üç kişilik grup kurmayın. **Sonra her
üye grubu `week03/group_03.json` dosyasına yazar**: kendi numarası dahil bütün üyelerin
öğrenci numaraları. Her üye tam olarak aynı listeyi yazar. Dersten sonra listeleri
karşılaştırırım; aynı değilse grubun her üyesi ders sonu notundan bir puan kaybeder. Herkes kendi bilgisayarından beş dakika sunar;
diğer üçü dinler, sonra 7. slayttaki üç sorunun her biri için birer cümle **yazar** —
kâğıda ya da bir metin dosyasına — ve sunana verir. Dört tur, yaklaşık 45 dakika. Ne
düşünüyorsanız söyleyin; nazik bir "iyi olmuş" kimseye yardım etmez, kimseye puan
getirmez.

**Bu grup, dönemin geri kalanında sizin grubunuzdur.** 4. Hafta'dan itibaren dördünüz
**her hafta, ders ile Cumartesi arasında, bir saatlik bir çevrimiçi toplantı** yaparsınız
— Teams, Meet, Discord, ne isterseniz — ve her biriniz o hafta projesinde neyin değiştiğini
anlatır; diğer üçü ne düşündüğünü söyler. O andan sonra `weekNN/contributors_NN.json`
içindeki üç kayıt bu toplantıdan gelir: kim ne dedi, alıntıyla, ve siz ne yaptınız.
Toplantıda olmayan biri için kimse o üç kaydı yazamaz; toplantıyı kaçırmak kendiliğinden
görünür. İlkini bu hafta yapabilirsiniz.

### 2. `week03/contributors_03.json` — üç değerlendiren

Üç değerlendireniniz grubunuzun diğer üç üyesidir (beş kişilik grupta dördünden üçü). Rol
`reviewer`, öğrenci numaraları ve her biri için **yazdığı en
yararlı cümle** — özetlenmiş değil, alıntılanmış. Sonra `accepted: true` ya da `false`
ve `why`. Bir öneriyi gerekçeyle reddetmek olur; her şeyi kabul edip neyin değiştiğinin
izi olmaması olmaz. Adını yazdığınız her değerlendiren geçen haftaki gibi katkı bonusu
kazanır.

### 3. `PROPOSAL.md` — Bölüm A gözden geçirilmiş, Değişiklik günlüğü başlamış

Üç cevap önünüzdeyken §1–§7'yi yeniden okuyun ve incelemenin değiştirdiğini değiştirin.
Her değişiklik dosyanın sonundaki Değişiklik günlüğüne **tarihli bir satır**: ne değişti,
hangi bölümde, neden — "2026-10-08 — §4: grup sohbeti çıkarıldı; iki değerlendiren
WhatsApp'ın yanında kimsenin kullanmayacağını söyledi". Teklif değişebilir; sessizce
değişemez.

`requirements.json` bu hafta da değişebilir — ekleyin, çıkarın (id kalır, `"dropped":
true`), yeniden yazın. **Cumartesiden itibaren bir id'nin anlamı hiç değişmez**; listenin
kendisi 5. Hafta sonuna kadar açık kalır ve prototip incelemesinden sonra taban çizginiz
(baseline) olur.

### 4. `week03/screens_03.md` — ana akışınızın ekranları

Ana akışınız, kullanıcının giriş yapmaktan uygulamanızın var olma nedeni olan tek işe kadar
izlediği yoldur. Ekranlarını sırayla yazın: giriş dahil en az beş. Her ekran için kullanıcının
orada ne yaptığını birkaç kelimeyle yazın ve ekranın hizmet ettiği gereksinimleri adlandırın.
StudyRoom için: Giriş · Bugünün odaları · Dilim ayırma · Ayırmalarım · Check-in.

Proje burada somutlaşır. Beş ekranı ve arkalarındaki gereksinimleri söyleyemiyorsanız proje
henüz hazır değildir; bunu bugün, grubunuz yanınızdayken öğrenmek daha iyidir. 4. haftada her
satır, tıklanabilir prototipinizin bir ekranı olur.

**Ekranlardan sonra vaktiniz kalırsa** grubunuzla şunları yapın:

- birbirinizin `must` gereksinimlerinin kabul ölçütlerini okuyun ve test edenin kontrol
  edemeyeceği her birini işaretleyin (aşağıda 8. madde);
- haftalık bir saatlik çevrim içi toplantınızın gününü ve aracını kararlaştırın;
- ben sınıftayken Bölüm B'ye, özellikle §8'e ve §12'deki mağaza seçimine başlayın.

### 5. Push

```bash
python .github/check_deliverables.py
git add .
git commit -m "week03: pitch, review, proposal revised, main flow"
git push
```

İnceleme turundan sonra ve dersin sonunda, **11:45**'te bir kez daha push edin — her zamanki 10:00 / 11:00 / ders sonu (11:45). Hemen ardından her repoyu donduruyorum. Push edilmeyen yoktur.

---

## Cumartesi 23:59'a kadar

### 6. `PROPOSAL.md` — Bölüm B, §8–§12

Neden yapmaya değer olduğunu söyleyen yarı. Her bölümün dosya içinde NEDEN'i, NE'si ve
zayıf/güçlü örneği var; StudyRoom örnekleri devam ediyor.

- **§8 Pazar ve hedef kullanıcılar** — kim, kaç kişi, nereden biliyorsunuz. 3. slayttaki
  beş test kullanıcınız bu bölümün ilk satırı.
- **§9 Rakipler** — sorunu bugün çözen üç şey; kâğıt liste de sayılır.
- **§10 Karşılaştırma ve üstünlüğünüz** — küçük bir tablo, kullanıcının ölçütleri, tek cümle.
- **§11 Ticari potansiyel** — kendini nasıl finanse eder; "ticari niyet yok, değeri X"
  gerekçelendirirseniz dürüst bir cevaptır.
- **§12 Teknik riskler** — 11. haftaya kadar sizi durdurması en olası üç şey, her biri
  için plan ve yedek. **Seçtiğiniz mağaza (S0)** burada adıyla, ücretiyle, inceleme ya da
  test süresiyle yazılır: karar vermeden `AI_PLATFORMS_AND_STORES_TR.md` dosyasını okuyun.
  Seçiminiz kesinse geliştirici hesabınızı bu hafta açabilirsiniz (S1, 4. haftada
  notlanır), çünkü kimlik kontrolü bir günden bir haftaya kadar sürer.

### 7. Yapay zekâyı düşman gözüyle okutun — `week03/ai_log_03.md`

Bu hafta asistan, hayır demek isteyen yatırımcıyı oynar. Bölüm B'nizi verin ve en güçlü
üç itirazı isteyin. Sonra **birini teklifte cevaplayın** ve **birinin yanlış olduğunu
gösterin** — kanıtla: bir sayı, bir kaynak, kontrol ettiğiniz bir şey. Yazışmayı
yapıştırın. "Yararlı geri bildirim verdi" diyen bir günlük puan getirmez.

### 8. Kabul ölçütlerinizi 4. Hafta'ya hazırlayın

4. Hafta'da `requirements.json` içindeki her kabul ölçütü bir test case'e dönüşür ve
grubunuzun üyeleri bu test case'leri tıklanabilir prototipiniz üzerinde yürütür. "Kullanıcılar
memnun kalır" gibi kimsenin kontrol edemeyeceği bir ölçüt test case'e dönüşemez. Bu hafta
ölçütlerinizi yeniden okuyun ve bir testçinin ne görmesi gerektiğini söylemeyenleri yeniden
yazın. Bu hafta notlanmaz; gelecek hafta başlangıç noktası budur.

### 9. Yeniden push, kontroller yeşil

Çalıştıkça yapılan, her birinde biraz yeni iş ve ne değiştiğini söyleyen bir mesaj olan commit'ler; bir commit'in bitmiş bir parça olması gerekmez. Denetleyicinin istediği
her şey aşağıda.

---

## Teslim listesi

**Dersten önce**
- [ ] `week03/PITCH_03.md` — altı slayt dolu, sizin yazdığınız, push edilmiş

**Derste, dersin sonuna (11:45) kadar**
- [ ] `week03/group_03.json` — grubunuzun bütün üyelerinin numaraları, onlarınkiyle aynı liste
- [ ] `week03/contributors_03.json` — grubunuzdan üç değerlendiren, her birinden alıntı bir cümle, accepted/why
- [ ] `PROPOSAL.md` §1–§7 incelemenin değiştirdiği yerlerde gözden geçirilmiş
- [ ] `PROPOSAL.md` Değişiklik günlüğü — en az bir tarihli satır
- [ ] `week03/screens_03.md` — ana akışın en az beş ekranı, her birinde kullanıcının orada ne yaptığı ve REQ kimlikleri
- [ ] Projenizin başlığı ve içeriği kesin: bu push'tan sonra yalnızca ayrıntıları değişebilir

**Cumartesiye kadar**
- [ ] `PROPOSAL.md` §8–§12 dolu; §12 mağazayı, ücretini ve inceleme süresini adlandırıyor
- [ ] `week03/ai_log_03.md` — üç itiraz, biri teklifte cevaplanmış, birinin yanlışlığı gösterilmiş, yazışma yapıştırılmış
- [ ] `requirements.json` güncel — bundan sonra bir id'nin anlamı değişmez
- [ ] GitHub'da kontroller yeşil; 1. ve 2. hafta hâlâ geçiyor

---

## Bu hafta değil

Kod yok, prototip henüz yok (4. hafta), tasarım belgeleri henüz yok (5. hafta), ortam
kurulumu yok. §12'de mağazayı adlandırmak yeter; geliştirici hesabını (S1) açmak bu hafta
isteğe bağlıdır ve 4. haftada notlanır.

---

## Bu hafta nasıl notlanıyor

**Ders sonu — 5 puan.** Sunum push edilmiş ve tam, grup yazılmış, üç değerlendiren gerçek
cümlelerle, Değişiklik günlüğü başlamış, ana akışın ekranları yazılmış — reponuzun dersin sonundaki (11:45) halinden okunur. Üyeleri aynı listeyi yazmayan bir grubun her üyesi bir puan kaybeder.

**Cumartesi 23:59 — 5 puan.** Son durumda kontroller yeşil: **2**. İnsan katkısı: **2** —
kanıtıyla `ai_log_03.md` ve arkasında gerçek cümleler, gerçek kararlar olan incelemeler.
Commit disiplini: **1** — derste farklı zamanlarda birkaç push (en az üç) ve çalıştıkça yapılan birkaç commit; her birinde biraz yeni iş olsun.

**Katkı bonusu.** Adını yazdığınız her değerlendiren haftalık notunuzun %10'unu kazanır;
siz de verdiğiniz incelemeler için aynısını kazanırsınız. 4. Hafta'dan itibaren isimler grubunuzdur.

**Bir öğrenci, bir bilgisayar, bir GitHub hesabı.** Arkadaşınızın bilgisayarında ya da
onun oturumunda yapılan iş ders için puan getirmez.
