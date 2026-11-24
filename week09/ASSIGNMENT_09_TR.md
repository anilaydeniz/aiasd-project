# 9. Hafta Ödevi: Beta Test

## 1. Kurallar ve notlandırma

### 1.1 Kurallar

- **Paylaşılmayan tek bir bilgisayar ve paylaşılmayan tek bir GitHub hesabı kullan.** Derste `student.json`
  içinde listelediğin bir bilgisayarda (8. hafta §4.1), dersten sonra da aynı bilgisayarda çalışmalısın.
  `student.json` içinde listelenmemiş bir bilgisayarda ya da başka bir kişinin Git kimliğiyle yaptığın ders
  çalışması ders için puan getirmeyecek. Derse geç gelirsen ve ders işinin önemli bir kısmı sen gelmeden önce
  yapılmış olursa ders çalışman 0 puan alacak.

- **Her commit'te ait olduğu işleri listele ve asla 'force push' yapma.** Bu haftadan itibaren bir iş için tek
  bir commit yeterli. Commit mesajının ilk satırından sonra her commit, ait olduğu işleri her biri ayrı satırda ve
  `- ` ile başlayarak listelemeli (§5.7). Bir force push, neyi değiştirmiş olursa olsun, sana o haftanın commit
  puanını kaybettirecek.

- **Derste Cumartesi işine geçmeden önce bir issue aç.** Ders işini dersin bitiminden önce tamamlarsan, önce kendi
  repona ders işini tamamladığını söyleyen bir issue açmalısın. Cumartesi işine ancak bundan sonra
  başlayabilirsin; böylece ders işini ve Cumartesi işini birbirinden ayırabilirim.

- **AI log'u hiçbir yapay zeka yardımı olmadan doldur. Bir asistan AI log'da sana herhangi bir şekilde yardım
  ederse AI log'un 0 alacak.** Log'u yazmak, geliştirmek, çevirmek ya da dilini düzeltmek için bir asistan
  kullanma.

**Bu hafta asistanın yardım edebileceği ve edemeyeceği yerler:**

Beta test gerçek kişilerin haftasıdır. Testçilerinin gördükleri ve senin bunlarla ilgili kararların bir asistandan
değil, senden ve onlardan gelmeli.

| İş | Asistan |
|---|---|
| Bir hatanın sebebini bul, kodu yaz ya da düzelt. | Asistan yardım edebilir. Her değişikliği commit etmeden önce kontrol etmelisin. |
| Sohbet botunun sahte modelli testlerini ve Report butonunun kodunu yaz. | Asistan yardım edebilir. |
| Bir sınıf arkadaşının test case'lerini onun uygulamasında çalıştır ve gördüğünü yaz. | Asistan yardım edemez. |
| `beta_runs.json`, `bug_list.json` ve `tested_by_me.json` dosyalarını yaz. | Asistan yardım edemez. |
| Değişiklik isteklerini (change request), gereksinimleri ve test case'leri yaz. | Asistan yardım edemez. |
| `test_report_09.md` dosyasını yaz. | Asistan yardım edemez. |
| `week04/store.json` içinde S4'ü doldur. | Asistan yardım edemez. |
| `ai_log_09.md` dosyasını yaz. | Asistan hiçbir şekilde yardım edemez. Bir asistan sana yardım ederse AI log'un 0 alacak. |

### 1.2 Performansın nasıl notlandırılacak

Dersteki performansın 5 puan üzerinden notlandırılacak. Dersin sonuna kadar push ettiğin son commit'i okuyacağım ve
şunları kontrol edeceğim:

- Derste bulunan her testçi sınıf arkadaşın, test kanalından yüklenmiş uygulamanda test case'lerini çalıştırmış
  olmalı ve sen onların her çalıştırmasını `week09/beta_runs.json` dosyasına yazmış olmalısın (§4.2).
- Başarısız olan her çalıştırma ve testçilerinin bulduğu diğer her sorun `week09/bug_list.json` içinde olmalı
  (§4.3).
- Seni testçi olarak yazan ve derste bulunan her sınıf arkadaşının uygulamasını test etmiş ve her birini
  `week09/tested_by_me.json` dosyasına yazmış olmalısın (§4.4).

İlk madde sana 2 puan, ikincisi 1 puan, üçüncüsü 2 puan kazandıracak.

Cumartesi 23:59'a kadarki performansın 5 puan üzerinden notlandırılacak. 23:59'a kadar GitHub'a ulaşan son
commit'i okuyacağım. Commit'in üzerindeki saat değil, GitHub'ın push saati sayılacak.

- Yeşil kontroller sana 2 puan kazandıracak.
- AI log, bütün haftadaki gerçek kullanımını anlatıyorsa, commit'lerinle uyuşuyorsa, cevapları nasıl kontrol
  ettiğini gösteriyorsa ve commit'leri anıyorsa sana 2 puan kazandıracak. Çok genel kalırsa ya da cevapları nasıl
  kontrol ettiğini göstermezse 1 puan kazandıracak. Bir asistan yazdıysa, commit'lerin onunla çelişiyorsa ya da
  boşsa 0 puan alacak.
- Commit disiplini sana 1 puan kazandıracak (§5.7).

Bir biçim hatası için önce bir uyarı vereceğim. Aynı hatayı sonraki bir haftada tekrarlarsan 1 puan
kaybedeceksin.

---

## 2. Döneme genel bakış

<table>
<tr><th width="10%" align="center">Hafta</th><th width="15%" align="center">Tarih</th><th width="70%" align="left">Ne yapıyoruz</th></tr>
<tr><td align="center">1</td><td align="center">22–23 Eylül</td><td>Araçları kurdun, Git ve GitHub'ı öğrendin ve LLM'lere ilk kez baktın.</td></tr>
<tr><td align="center">2</td><td align="center">29–30 Eylül</td><td>Proposal Part A'yı, gereksinimleri ve kullanım senaryolarıyla birlikte SRS'i yazdın.</td></tr>
<tr><td align="center">3</td><td align="center">6–7 Ekim</td><td>Projeni grubunda sundun (pitch), Proposal Part B'yi yazdın ve mağazanı seçtin (S0).</td></tr>
<tr><td align="center">4</td><td align="center">13–14 Ekim</td><td>Tıklanabilir prototipi yaptın ve test case'leri yazdın (S1).</td></tr>
<tr><td align="center">5</td><td align="center">20–21 Ekim</td><td>Tasarımı ve API sözleşmesini yazdın ve sunucuya başladın. Gereksinimlerin baseline'ın oldu.</td></tr>
<tr><td align="center">6</td><td align="center">27–28 Ekim</td><td>Özelliğin sunucuda ve web'de uçtan uca çalıştı (S2).</td></tr>
<tr><td align="center">7</td><td align="center">3–4 Kasım</td><td>Uygulaman telefonda çalıştı.</td></tr>
<tr><td align="center">–</td><td align="center">10–11 Kasım</td><td>Ders yoktu.</td></tr>
<tr><td align="center">8</td><td align="center">17–18 Kasım</td><td>Ürünün sohbet botuna kavuştu, sunucun yeniden başlatmadan sonra verisini korudu ve ilk build'in testçilerine gitti (S3).</td></tr>
<tr><td align="center"><b>9</b></td><td align="center"><b>24–25 Kasım</b></td><td><b>Bu hafta testçilerin uygulamanı beta testte test edecek. Hataları düzelteceksin, sohbet botunun testlerini yazacaksın ve cevaplarına Report butonunu ekleyeceksin (S4).</b></td></tr>
<tr><td align="center">10</td><td align="center">1–2 Aralık</td><td>UAT'yi yapacaksın, dağıtım (deployment) diyagramını çizeceksin ve uygulamanı mağazaya göndereceksin (S5). <i>Erken başla: aşağıdaki listeye bak.</i></td></tr>
<tr><td align="center">11</td><td align="center">8–9 Aralık</td><td>İncelemenin istediği düzeltmeleri yapacaksın, uygulamanı mağazada yayınlayacaksın ve son README'yi yazacaksın (S6). <i>Erken başla: aşağıdaki listeye bak.</i></td></tr>
<tr><td align="center">12</td><td align="center">15–16 Aralık</td><td>Posteri hazırlayacaksın ve savunmanın provasını yapacaksın. <i>Erken başla: aşağıdaki listeye bak.</i></td></tr>
<tr><td align="center">13</td><td align="center">22–23 Aralık</td><td>Uygulaması mağazada yayında olan öğrenciler projelerini sunacak.</td></tr>
<tr><td align="center">14</td><td align="center">29 Aralık</td><td>Diğer öğrenciler projelerini sunacak.</td></tr>
</table>

**Erken başla.** Önümüzdeki haftaların bazı işleri saatler değil günler sürecek, bu nedenle onlara erken başlamanı
rica ederim:

- **10. hafta:** Uygulamanın mağaza sayfasına ihtiyacın olacak: ikonu, ekran görüntüleri, açıklamaları ve gizlilik
  metninin adresi. UAT için pitch'indeki beş kişiye de ihtiyacın olacak. Onlardan bu hafta rica et.
- **10. ve 11. haftalar:** Mağazanın uygulamanı incelemesi birkaç gün sürebilir ve bu süre senin sorumluluğunda.
  Uygulamanı planlandığı gibi 10. haftada gönder, böylece 11. haftada incelemenin istediği düzeltmeleri yapmaya
  vaktin olur. 13. haftadaki sunumun kalan 3 puanı için uygulamanı 5 Aralık Cumartesi 23:59'a kadar göndermiş
  olman da gerekiyor. Google Play'de, üretime (production) başvurabilmen için testçilerinin 14 gün boyunca
  kesintisiz olarak kayıtlı kalması gerekiyor.
- **12. hafta:** Posterin için uygulamanın ekran görüntülerine ve mimari diyagramına ihtiyacın olacak.

---

## 3. Bu hafta

### 3.1 Bu hafta bir bakışta

8. haftadan beri uygulaman mağazanın test kanalında ve testçilerin bu kanala kayıtlı. Bu hafta gerçek kişiler onu
ilk kez kullanacak. Testçi sınıf arkadaşların uygulamanı derste test edecek, sen de seni testçi olarak yazan sınıf
arkadaşlarının uygulamalarını test edeceksin. Bu dersi almayan testçilerin uygulamanı Cumartesi 23:59'a kadar
test edecek.

```text
testçilerin uygulamanı test kanalından yükler (dersten önce)
  ↓    test case'lerini çalıştırırlar ve uygulamayı serbestçe kullanırlar
  ↓    her çalıştırmayı beta_runs.json'a, her sorunu bug_list.json'a yazarsın
  ↓    hataları düzeltirsin (commit mesajında her satırda bir BUG id'si)
  ↓    başarısız çalıştırmalar yeniden çalışır (2. tur)
  ↓    test_report_09.md: beta testin gösterdikleri
```

Bir sınıf arkadaşıyla yapılan her test iki kez kaydedilir: bir kez uygulamanın sahibi tarafından
(`beta_runs.json`) ve bir kez testçi tarafından (`tested_by_me.json`). Yani ikiniz de aynı testi, her biriniz
kendi reponuzda yazmalısınız.

**Derste ne yapıyorsun**

<table>
<tr><th width="15%" align="left">Saat</th><th width="75%" align="left">İşin</th><th width="10%" align="center">§</th></tr>
<tr><td>dersten önce</td><td>Testçilerin uygulamanı test kanalından yüklemiş, sen de test edeceğin uygulamaları yüklemiş olmalısın. Repondaki "9. haftaya hazırlık" issue'su bunu anlatıyor.</td><td align="center">4.2</td></tr>
<tr><td>dersin başı</td><td>Checker'ı çalıştır: <code>week09/</code> klasörünü getirir. Ders dosyalarını commit et ve push et.</td><td align="center">4.1</td></tr>
<tr><td>yaklaşık 11:15'e kadar</td><td>Beta test. Testçi sınıf arkadaşların senin test case'lerini uygulamanda çalıştırır, sen de seni yazan sınıf arkadaşlarının test case'lerini çalıştırırsın. Her turdan hemen sonra çalıştırmaları yazın: uygulamanın sahibi <code>beta_runs.json</code> dosyasına, testçi <code>tested_by_me.json</code> dosyasına.</td><td align="center">4.2, 4.4</td></tr>
<tr><td>yaklaşık 11:15</td><td>Başarısız çalıştırmalardan ve diğer sorunlardan hata listeni yaz.</td><td align="center">4.3</td></tr>
<tr><td>11:45</td><td>Son kez push et.</td><td align="center">4.5</td></tr>
</table>

Dersteki performansın 5 puan, Cumartesi performansın 5 puan üzerinden notlandırılacak. Ayrıntılar §1.2'de.

### 3.2 Bu hafta neler öğreneceksin

Bu hafta şunları öğreneceksin:

- gerçek kişilerle yapılan bir beta testin, senin de bir asistanın da beklemediği sorunları nasıl bulduğunu;
- testçilerin gördüklerini nasıl bir hata listesine çevireceğini ve her hatayı izlenebilir bir commit'le nasıl
  düzelteceğini;
- bir LLM API'sini çağıran kodu, API'yi çağırmadan, sahte bir modelle nasıl test edeceğini.

Şu yeni terimleri de kullanacaksın:

| Terim | Anlamı |
|---|---|
| Beta test | Beta test, neredeyse bitmiş bir ürünün herkese açılmadan önce gerçek kullanıcılar tarafından test edilmesidir. Testçilerin uygulamanı test kanalından yükler ve onu bir kullanıcı gibi kullanır. |
| Beta testçi | Beta testçi, test kanalına kayıtlı olan ve uygulamanı test eden kişidir. Beta testçilerin, S3'te kaydettiğin testçilerdir. |
| Hata (bug) | Hata, ürününün yaptığı ile gereksiniminin ya da test case'inin yapması gerektiğini söylediği arasındaki farktır. Bir çökme, yanlış bir cevap ve testçinin anlayamadığı bir ekran, hepsi birer hatadır. |
| Önem (severity) | Bir hatanın önemi, kullanıcıya ne kadar zarar verdiğini söyler: `high` (kullanıcı ana işini bitiremiyor ya da veri kayboluyor veya açığa çıkıyor), `medium` (kullanıcı işini bitirebiliyor ama zorlanarak), `low` (görünüşle ilgili bir sorun). |
| 2. tur | 2. tur, başarısız olmuş bir test case'inin düzeltmeden sonra yeniden çalıştırılmasıdır. |
| Sahte model (fake model) | Sahte model, testinde LLM API'sinin yerine cevap veren küçük bir fonksiyondur. Test böylece kodunu internetsiz, anahtarsız ve masrafsız kontrol eder. |
| Kapsam (coverage) | Kapsam, sunucunun satırlarından testlerinin çalıştırdığı kısmın oranıdır. `pytest-cov` bunu ölçer. |
| S4 | S4, mağazanın dördüncü adımıdır. S4'te beta testin, S3'te kaydettiğin testçilerle mağazanın test kanalında çalışır. |

### 3.3 Checker bu hafta neler getiriyor

Dersin başında checker'ı çalıştırdığında (§4.1), checker repona yeni `week09/` klasörünü getirecek. Klasörde
şunlar var:

- `ASSIGNMENT_09_EN.md` ve `ASSIGNMENT_09_TR.md`: bu ödevin İngilizcesi ve Türkçesi;
- `beta_runs.json`: testçilerinin uygulamandaki çalıştırmaları (§4.2);
- `bug_list.json`: hata listen (§4.3);
- `tested_by_me.json`: test ettiğin uygulamalar (§4.4);
- `test_report_09.md`: Cumartesi günü dolduracağın test raporunun formu (§5.5);
- `ai_log_09.md`: Cumartesi günü dolduracağın AI log'un formu (§5.6);
- `requirements.txt`: bu haftanın paketleri, aralarında `pytest-cov` var.

Bu haftanın paketlerini bir kez kur:

```bash
pip install -r week09/requirements.txt
```

Checker'ın kendisi de bu hafta yeni kontroller kazanıyor. Beta testin üç dosyasını kontrol edecek. Senin
`tested_by_me.json` dosyanı, uygulamasını test ettiğin her sınıf arkadaşının `beta_runs.json` dosyasıyla ben
karşılaştıracağım. Cumartesi günü sohbet botunun testlerini, Report butonunu, test raporunu ve `week04/store.json`
içindeki S4'ü de kontrol edecek.

---

## 4. Dersteki işin

### 4.1 Ders dosyaları

Dersin başında checker'ı çalıştır. `week09/` klasörünü getirir. Sonra ders dosyalarını commit et ve push et:

```bash
python .github/check_deliverables.py
git add .
git commit -m "week09: course files"
git push
```

Checker bilgisayarının adını ve `git config user.email` çıktını da okur ve bu bilgisayar `student.json` içinde
listelenmemişse sana söyler.

### 4.2 Beta test: `week09/beta_runs.json`

Testçi sınıf arkadaşların, `week04/store.json` dosyasındaki S3'ün `"classmate_testers"` alanına yazdığın sınıf
arkadaşlarındır. Bunlardan derste bulunan her biri uygulamanı test eder, sen de seni yazan her sınıf arkadaşının
uygulamasını test edersin.

- **Uygulama test kanalından gelir.** Testçi, uygulamanı mağazanın test kanalından yüklendiği haliyle, kendi
  telefonunda kullanır. Yalnız senin laptopunda ya da bir emülatörde çalışan bir build beta test değildir.
- **Testçi senin test case'lerini çalıştırır.** Testçi `week04/test_cases.json` içindeki test case'lerinden en az
  üçünü çalıştırır ve bunlardan en az biri login dışında olmalı. Sohbet botunun test case'i iyi bir seçimdir.
- **Sonra testçi uygulamayı birkaç dakika serbestçe kullanır**: bir kullanıcı gibi, test case'lerin olmadan.
- **Sen izlersin ve yardım etmezsin.** Ekranlarını açıklama. Testçi ne yapacağını bilemiyorsa, bu bir bulgudur.

Mağazan uygulamanı ya da hesabını senin değiştiremeyeceğin bir nedenle test kanalına kabul etmediyse, örneğin mağazanın kuralları gereği reddettiyse, testçilerin uygulamanın APK'sini kendi telefonlarına yükleyebilir. Bunun için mağazanın ret mesajının ekran görüntüsünü, kişisel bilgilerini kapatarak `week04/` içine kaydetmelisin. `beta_runs.json` içinde cihazın sonuna "(APK)" yaz, S4'ün `track` alanına da "APK" ve reddin nedenini yaz. Geç yapılmış ya da hiç yapılmamış bir adım, örneğin zamanında yüklenmemiş bir build ya da kaydedilmemiş testçiler, bu nedenlerden sayılmaz.

Her turdan hemen sonra her çalıştırmayı `week09/beta_runs.json` dosyasına elle yaz. Biçim, 7. haftanın
`mobile_runs.json` dosyasıyla aynı:

```json
{ "tc": "TC-012-01", "tester": "123456789", "device": "Samsung A52, Android 14", "round": 1,
  "result": "fail", "note": "The chat screen showed an empty bubble when the server answered 503." }
```

- `tc`, test case'in id'sidir. Testçinin uygulamayı serbestçe kullanırken bulduğu bir sorun için `"free"` yaz.
- `tester`, testçinin 9 haneli öğrenci numarasıdır. Bu dersi almayan bir testçi için `"outside: "` ve ardından
  adını ve soyadının ilk harfini yaz, örneğin `"outside: Ayşe Y."`. Asla bir e-posta adresi yazma.
- `device`, testçinin telefonunu adlandırır.
- `round`, beta test için 1, bir düzeltmeden sonraki yeniden çalıştırma için 2'dir (§5.2).
- `result`, `pass`, `fail` ya da `blocked` olur. `note`, testçinin ne gördüğünü tam bir cümleyle söylemeli. Bir
  `fail` ya da `blocked` çalıştırmanın notu olmalı.

### 4.3 Hata listesi: `week09/bug_list.json`

Beta testten hemen sonra hata listeni yaz. Her `fail` ve her `blocked` çalıştırma ve testçinin bulduğu diğer her
sorun, daha önceki bir girdiyle aynı sorun değilse, bir girdidir:

```json
{ "id": "BUG-01", "found_by": ["123456789"], "tc": "TC-012-01", "severity": "high",
  "what": "The chat screen shows an empty bubble when the server answers 503.",
  "status": "open", "fix_commit": "", "why": "" }
```

- `id`, `BUG-` ve bir numaradır: `BUG-01`, `BUG-02` ve böyle devam eder. Bir id asla anlamını değiştirmez.
- `found_by`, hatayı bulan testçileri `beta_runs.json` dosyasındaki gibi listeler.
- `tc`, test case'in id'si ya da `"free"` olur.
- `severity`, `high`, `medium` ya da `low` olur (§3.2). Buna sen karar verirsin.
- `what`, neyin yanlış olduğunu, uygulamanı hiç görmemiş biri anlayacak şekilde tam bir cümleyle söyler.
- `status` derste `open` olur. Cumartesi günü `fixed` ya da `not fixed` olur (§5.2).

### 4.4 Test ettiğin uygulamalar: `week09/tested_by_me.json`

Sen de bir beta testçisin. Seni testçi olarak yazan ve derste bulunan her sınıf arkadaşının uygulamasını §4.2'de
anlatıldığı şekilde test et. Her turdan hemen sonra bunu kendi `week09/tested_by_me.json` dosyana yaz:

```json
{ "owner": "234567891", "device": "Xiaomi Redmi Note 12, Android 14", "tcs": ["TC-001-01", "TC-004-01", "TC-009-01"],
  "free_use": true, "problems": 2, "note": "The list did not refresh after I added a record." }
```

- `owner`, uygulamanın sahibinin 9 haneli öğrenci numarasıdır.
- `tcs`, çalıştırdığın test case'leri listeler. Uygulamayı serbestçe de kullandıysan `free_use` `true` olur.
- `problems`, gördüğün sorunların sayısıdır. `note`, en önemlisini tam bir cümleyle söyler ya da `"no problem"`
  olur.

Hiçbir sınıf arkadaşın seni testçi olarak yazmadıysa dosyanın başındaki `"nobody_listed_me"` alanını `true` yap.

Uygulama sahibinin `beta_runs.json` dosyası ile senin `tested_by_me.json` dosyan aynı testi anlatmalı. İkisini ben
karşılaştıracağım.

### 4.5 Push et ve sonucu GitHub'da kontrol et

Checker'ı çalıştır, commit et ve push et. Ders notu, dersin sonuna kadar push ettiğin son commit'i okur. Derste
kaçırdığın bir sınıf arkadaşı testi sonradan telafi edilemez.

---

## 5. Cumartesi 23:59'a kadarki işin

### 5.1 Bu dersi almayan testçiler

Bu dersi almayan testçilerin uygulamanı Cumartesi 23:59'a kadar aynı şekilde test eder: test case'lerinden en az
üçünü çalıştırırlar, sonra uygulamayı serbestçe kullanırlar. Her çalıştırmalarını `beta_runs.json` dosyasına
`"outside: "` ve adlarıyla (§4.2), her sorunu `bug_list.json` dosyasına yazarsın.

Bu dersi almayan bir testçinin reposu olmadığı için kaydın ikinci tarafı bir ekran görüntüsüdür. Bu testçilerin
her biri için `week09/` içine bir ekran görüntüsü kaydet: ya sana gördüklerini anlatan mesajının ya da mağazanın
konsolundaki geri bildiriminin. Kaydetmeden önce e-posta adresini ve telefon numarasını kapat. Dosyanın adını, o
testçinin her çalıştırmasının `evidence` alanına yaz, örneğin `"evidence": "outside_ayse.png"`.

### 5.2 Hataları düzelt

`bug_list.json` içindeki her girdinin Cumartesi'ye kadar bir kararı olmalı:

- **Düzelt.** `status` alanını `fixed` yap ve düzeltmenin commit'ini `fix_commit` alanına yaz. Commit mesajı,
  listesinde hatayı anmalı (§5.7), örneğin `- BUG-03: the chat screen shows the 503 message`. Sonra başarısız test
  case'i yeniden çalışmalı: `beta_runs.json` dosyasına `"round": 2` olan yeni bir çalıştırma yaz. 2. turu kendin
  çalıştırabilirsin.
- **Düzeltme.** `status` alanını `not fixed` yap ve nedenini `why` alanına tam bir cümleyle yaz. Bir `high` hata,
  ancak gereksinimlerinin dışındaysa düzeltilmeden kalabilir; o durumda onu planından hangi değişiklik isteğinin
  çıkardığını yazmalısın.

Bir düzeltme bir gereksinimi, bir test case'ini, bir ekranı ya da bir `api.md` satırını değiştiriyorsa,
değişikliği her hafta olduğu gibi `PROPOSAL.md` Change log'una yaz.

### 5.3 Sohbet botunun testleri, sahte bir modelle

8. haftada sohbet botunun test case'i `"run": "manual"` idi. Bu hafta davranışı sunucuda da, internetsiz ve
anahtarsız olarak test ediliyor: test, LLM API'sine yapılan çağrının yerine sahte bir model koyar.

- Aşağıdaki test case'leri `week04/test_cases.json` dosyasına `"run": "server"` ile, her birini sohbet botunun
  gereksinimiyle adlandırarak ekle. Test case eklemek bir değişiklik isteğidir: bunlar için `PROPOSAL.md` Change
  log'una bir `CR-` satırı yaz.
  - sohbet botu, giriş yapmış bir kullanıcıya cevap verir;
  - token olmadan cevap 401 olur;
  - günlük sınırdan sonra cevap 429 olur;
  - LLM API'si hata verdiğinde ya da zamanında cevap vermediğinde cevap 503 olur ve sunucu çökmez.
- Her biri için `server/tests/` içinde, id'siyle adlandırılmış bir test yaz, örneğin
  `test_TC_012_03_after_the_daily_limit_the_answer_is_429`.
- Her testte, sunucunun LLM API'sini çağıran fonksiyonunu sahte bir fonksiyonla değiştir. Örneğin pytest'in
  `monkeypatch`'i ile:

```python
from fastapi.testclient import TestClient

from server.course_login import auth_header_for_tests
from server.main import app

client = TestClient(app)


def test_TC_012_02_the_chatbot_answers(monkeypatch):
    monkeypatch.setattr("server.chat.ask_model", lambda messages: "Your next booking is on Monday.")
    headers = auth_header_for_tests(client, "chat02@example.edu.tr")
    r = client.post("/chat", json={"message": "When is my next booking?"}, headers=headers)
    assert r.status_code == 200
    assert r.json()["answer"] == "Your next booking is on Monday."
```

  `server.chat` ve `ask_model` adları, `answer` alanı ve e-posta adresi birer örnektir: kendi sunucunun modülünü,
  fonksiyonunu ve alanlarını kullan ve her testte farklı bir adres kullan. Sunucun API'yi uzun bir fonksiyonun
  ortasında çağırıyorsa önce bu çağrıyı ayrı bir fonksiyona taşı.
- Testler asla gerçek LLM API'sini çağırmamalı ve anahtarın olmadığı GitHub'da yeşil kalmalı.

Sonra sunucunun kapsamını bir kez ölç:

```bash
pytest --cov=server --cov-report=term
```

Toplam yüzdeyi test raporuna yaz (§5.5). Yüzdenin kendisi notlandırılmayacak.

### 5.4 Report butonu

Bir model yanlış ya da saldırgan bir cevap yazabilir. Google Play'in yapay zeka ile üretilen içerik politikası,
yapay zeka sohbet botu temel bir özellik olan uygulamalardan, kullanıcının saldırgan içeriği uygulamadan çıkmadan
bildirebilmesini istiyor. Mağazan hangisi olursa olsun, sohbet botunun her cevabı bu hafta bir **Report** butonu
alıyor.

- **Bunu bir değişiklik isteği olarak ekle.** Bunun için `week02/requirements.json` dosyasına sıradaki boş id ile
  bir gereksinim, `week04/test_cases.json` dosyasına test case'ini ve `week05/api.md` dosyasına route'unun
  satırını ekle. Üçünü Change log'un tek bir `CR-` satırında an.
- **Route.** Örneğin `POST /chat/report`, cevabı ve kullanıcının kısa gerekçesini alır. Giriş gerektirir (token
  olmadan 401) ve sunucun bildirimi, diğer kayıtlarını tuttuğu gibi, kendi verisinde tutar.
- **Ekran.** `mobile/` içindeki sohbet ekranında her "AI answer"ın yanındaki Report butonu, cevabı bu route'a
  gönderir ve ekran kullanıcıya bildirimin alındığını söyler.
- **Test.** Route için `server/tests/` içinde, test case'iyle adlandırılmış bir test yaz.

### 5.5 Test raporu: `week09/test_report_09.md`

Test raporunu kendin doldur. Şu kısımları var:

1. **Testçiler.** Testçi sınıf arkadaşlarının öğrenci numaraları ve diğer testçilerinin adları. Kimin derste,
   kimin Cumartesi'ye kadar test ettiğini yaz.
2. **Neler test edildi.** Build (S4'teki sürüm), çalışan test case'ler ve serbest kullanım.
3. **Sayılar.** Kaç çalıştırma, kaç `pass`, `fail` ve `blocked`, öneme göre kaç hata ve bunlardan kaçının
   düzeltildiği.
4. **En önemli üç bulgu.** Her biri için testçilerin ne gördüğü ve senin bununla ilgili ne yaptığın.
5. **Seni şaşırtan.** Hiç beklemediğin sorun ve bunu neden beklemediğini düşündüğün.
6. **Sohbet botunun testleri.** Sunucunun kapsamı (§5.3).

### 5.6 AI log: `week09/ai_log_09.md`

Biçim 8. haftayla aynı. Log, bütün hafta boyunca, bütün işinde yapay zeka asistanlarını nasıl kullandığını
anlatmalı. Onu commit'lerinle karşılaştıracağım. Log'u Cumartesi günü kendin doldur:

1. **Asistanlarım.** Kullandığın her asistan, modeli ve ücretsiz mi ücretli mi olduğu, paketiyle birlikte.
2. **Bu haftaki her asistan kullanımı.** Haftanın sırasıyla her gerçek kullanım için bir satır: neyi sorduğun,
   cevabı nasıl kontrol ettiğin, onunla ne yaptığın ve commit.
3. **Bu hafta asistanlarla nasıl çalıştım.** Birkaç cümleyle bütün haftadaki çalışma biçimin.
4. **Asistansız yaptıklarım.** İşin hangi kısmını kendin yaptığın.
5. **Gelecek hafta.** Gelecek hafta farklı yapacağın bir şey.
6. **Bu dersten önce ve şimdi.** Bu kısım notlandırılmayacak, bu nedenle dürüstçe yazmanı rica ederim.

2 puan için her satır, cevabı nasıl kontrol ettiğini somut olarak söylemeli ve tutulan her sonuç kendi commit'ini
anmalı. Bir kodlama ajanı (coding agent) bir commit yaptıysa, satır hangi commit'i yaptığını ve onu nasıl kontrol
ettiğini de söylemeli. **AI log'u hiçbir yapay zeka yardımı olmadan yazmalısın. Bir asistan log'da sana herhangi
bir şekilde yardım ederse AI log'un 0 alacak.**

### 5.7 Commit'ler ve yeşil kontroller

Haftanın commit puanı şunları istiyor. Her commit'teki iş listesi bu hafta yeni olduğu için, listesi olmayan bir commit için bu hafta puan kırılmayacak, yalnız bir uyarı alacaksın. 10. haftadan itibaren böyle bir commit, commit puanına mal olacak.

- **Her commit ait olduğu işleri listeler.** Mesajın ilk satırından sonra bir boş satır bırak ve commit'in ait
  olduğu işleri her biri ayrı satırda ve `- ` ile başlayarak listele. Hatayı, gereksinimi, test case'i ya da bu
  ödevin bölümünü an. Örneğin:

  ```text
  week09: show the 503 message in the chat screen

  - BUG-03: the empty bubble on 503
  - TC-012-04: the screen part of the 503 test case
  ```

  `- fix` ya da `- update` gibi bir satır sayılmaz. Yalnız `git commit` yazarsan (`-m` olmadan), Git birkaç satır
  yazabileceğin bir editör açar.
- **Liste commit'le uyuşur.** Satırlar, commit'in değiştirdiği dosyaları anlatmalı.
- **Bir iş için tek bir commit yeterli.** İstediğin kadar sık commit edebilirsin.
- **Asla force push yapma.** Bir force push sana o haftanın commit puanını kaybettirecek.
- **Bir kodlama ajanının commit'i, ancak AI log'un onu anlatıyorsa sayılır.** Log'un satırı commit'i anmalı ve onu
  nasıl kontrol ettiğini söylemeli. Aksi halde commit sayılmaz.

**Öneri (puan kaybettirmez):** bir commit `mobile/` içine en fazla bir yeni ekran ve `server/` içine en fazla bir
yeni route eklemeli. Küçük commit'leri kontrol etmek daha kolaydır ve checker seni uyarmaya devam eder.

On ders testi ve `"run": "server"` olan her test case'in testleri GitHub'da yeşil kalmalı.
`.github/workflows/check.yml` ya da `.github/check_deliverables.py` dosyasını asla değiştirme. Git, uygulamanın
build klasörlerini tutmamalı (7. hafta §12).

### 5.8 `week04/store.json` içinde S4

S4'ü kendin doldur:

```json
  "S4": {
    "date": "2026-11-28",
    "track": "closed testing",
    "version": "1.0.1 (2)",
    "testers_in_lecture": ["123456789", "234567891", "345678912"],
    "testers_outside": ["Ayşe Y.", "Mehmet D."],
    "bugs": 7,
    "fixed": 5
  }
```

- `version`, testçilerinin test ettiği build'dir. Düzeltmelerle yeni bir build yüklersen onun sürümünü de yaz,
  örneğin `"1.0.1 (2), fixes in 1.0.2 (3)"`.
- Testçiler, S3'teki testçilerle aynı kişiler olmalı. Testçilerinin e-posta adresleri asla repona girmemeli.

### 5.9 Belgelerin: bir kontrol listesi

Cumartesi günkü son push'undan önce belgelerinin ürününü şimdiki haliyle anlattığını kontrol et:

- `PROPOSAL.md` içindeki Change log'da haftanın her değişikliği için bir satır ve her değişiklik isteği için bir
  `CR-` satırı var: sohbet botunun yeni test case'leri, Report butonu ve bir gereksinimi ya da bir test case'ini
  değiştiren her düzeltme.
- `week02/requirements.json` içindeki her gereksinim `week02/SRS.md` içindeki bir kullanım senaryosuna ait ve
  Report butonunun kullanım senaryosu, kullanım senaryosu diyagramında var.
- `week04/test_cases.json` içindeki her test case var olan bir gereksinimi anıyor ve adımları, düzeltmelerden
  sonra ekranlarının şimdiki haliyle uyuşuyor.
- Sunucunun her route'unun, `POST /chat/report` de dahil, `week05/api.md` içinde bir satırı var.
- `web/` ve `mobile/` içindeki her ekran, `serves:` satırında var olan bir gereksinimi anıyor.
- `bug_list.json` içindeki `fixed` olan her `BUG-` id'si var olan bir commit'i anıyor.

Checker id'ler arasındaki bağlantıların bir kısmını kontrol eder. Metinleri yalnız sen kontrol edebilirsin.
