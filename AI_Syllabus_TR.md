# Ders İzlencesi

**Yazılım Mühendisliği Bölümü · Atlas Üniversitesi** · sürüm 1 · 2026-09-21

*English: [`AI_Syllabus_EN.md`](AI_Syllabus_EN.md)*

| | |
|---|---|
| **Ders Kodu** | 1413002043 |
| **Ders Adı** | AI – Assisted Software Development (Yapay Zekâ Destekli Yazılım Geliştirme) |
| **Yıl ve Dönem** | 2026 – 2027 Güz |
| **Öğretim Üyesi** | Prof. Dr. Vedat COŞKUN |

## Dersin Tanımı

Öğrenciler yapay zekâyı yazılım geliştirme yaşam döngüsü boyunca disiplinli bir mühendislik aracı olarak kullanır. Her öğrenci dönem boyunca tek başına tek bir ürün geliştirir. Ürün bir mobil istemci, bir web istemcisi ve bir sunucudan oluşur; kullanıcılar e-postayla gönderilen bir kodla ya da OTP ile (tek kullanımlık şifre, yalnızca bir kez geçerli olan kısa bir kod) giriş yapar. Ürün ayrıca projenin kendisi hakkındaki soruları yanıtlayan bir sohbet botu içerir ve bu sohbet botu açık ağırlıklı modellerle (ağırlıkları yayımlanmış, dolayısıyla öğrencinin kendi bilgisayarında çalıştırabildiği yapay zekâ modelleri) çalışır. Öğrenci ürünü public bir uygulama mağazasında yayınlar: Google Play, Huawei AppGallery, Samsung Galaxy Store ya da Apple App Store. Uygulama native (platformun kendi dilinde yazılmış) ya da hybrid (bir kez yazılıp iki platform için derlenen) olabilir; bu seçim öğrencinindir.

Ders, üretimi değil değerlendirmeyi notlandırır: asistanın ne ürettiğini değil, öğrencinin onu ne kadar iyi tanımladığını, denetlediğini, düzelttiğini ve hesabını verdiğini notlar. Her haftanın işi, öğrencinin ders şablonundan (GitHub'ın öğrenci için kopyaladığı hazır bir repo) oluşturduğu kendi GitHub reposuna push edilir ve her push'ta otomatik olarak denetlenir.

## Dersin Hedefleri

Dersi tamamlayan öğrenci:

1. **Proje önerisi hazırlar.** Öğrenci kendi yaşadığı gerçek bir problemden yola çıkar; problemi ve çözümü anlatan, paydaşları adlandıran ve kullanım senaryolarını veren Bölüm A'yı, pazarı ve rakipleri inceleyen, ticari potansiyeli değerlendiren ve teknik riskleri sıralayan Bölüm B'yi yazar ve öneriyi beş dakikada pitch eder (2–3. Hafta).
2. **Gereksinim mühendisliği yapar.** Öğrenci fonksiyonel ve fonksiyonel olmayan gereksinimleri bir SRS (Software Requirements Specification, sistemin ne yapması gerektiğini listeleyen belge) olarak yönetir. Her gereksinim REQ-NNN biçiminde bir kimlik taşır, izlenebilirdir, verildikten sonra anlamını korur ve prototip incelemesinden sonra taban çizgisine (baseline) girer; öğrenci sonraki her değişikliği tarihli bir değişiklik günlüğüyle görünür kılar; kabul ölçütlerinden test case'ler yazılır ve prototip üzerinde yürütülür (2–5. Hafta).
3. **Tasarlar ve prototipler.** Öğrenci mimariyi, veri modelini, sistem bağlam diyagramını ve dağıtım diyagramını repoda Mermaid ile (GitHub'ın markdown dosyasının içinde çizdiği, metin tabanlı bir diyagram gösterimi) çizer, tıklanabilir bir prototip kurar ve onu akran incelemesinden sonra revize eder (4–5. Hafta).
4. **Full-stack uygulama geliştirir.** Öğrenci e-posta kodu ya da OTP ile giriş yapılan bir sunucu, bir web istemcisi ve bir mobil istemci geliştirir; aynı özellik üç katmanda birden çalışır (5. ve 8. Hafta).
5. **Mobil uygulama geliştirir.** Öğrenci mobil istemciyi Flutter, React Native–Expo, Kotlin ya da Swift ile geliştirir; istemci telefonda çalışır ve mağazaya hazırdır (7–8. Hafta).
6. **Açık ağırlıklı modellerle sohbet botu kurar.** Öğrenci, Ollama (açık ağırlıklı modelleri yerelde çalıştıran bir program) üzerinde Qwen modeli ve BGE-M3 gömmeleriyle (metnin, benzer parçaların bulunmasını sağlayan sayısal gösterimleri) projenin kendi belgeleri üzerinden getirme destekli bir sohbet botu (önce bir belge kümesindeki ilgili parçaları bulan, sonra onlardan yanıt veren sohbet botu) kurar, chat endpoint'ini yazar ve istemcilere entegre eder (6–7. Hafta).
7. **Yapay zekâ asistanlarını mühendislik aracı olarak kullanır.** Öğrenci asistana istem yazar, çıktısını doğrular ve düzeltir, hatalarını kanıtla haftalık yapay zekâ günlüğünde belgeler ve asistanı kendi işinin düşman gözden geçireni olarak kullanır. Ders üretileni değil değerlendirmeyi notlar (her hafta).
8. **Sürüm kontrolü ve sürekli entegrasyon uygular.** Öğrenci günlük küçük commit'ler yapar, GitHub'da otomatik kontrollerin çalışmasını sağlar, kod kalitesini ruff ile (Python kodundaki stil ve hata sorunlarını bildiren bir araç) korur ve parola gibi gizli anahtarları repo dışında tutar (her hafta; CI, yani sürekli entegrasyon, 7. Hafta'dan).
9. **Formal test süreçleri yürütür.** Öğrenci birim ve entegrasyon testleri yazar, kayıtlı testçilerle beta test yapar, hata listesi tutar, test raporu yazar ve gerçek kullanıcılarla Kullanıcı Kabul Testi (gerçek kullanıcıların ürünü deneyip ihtiyaçlarını karşılayıp karşılamadığını söylediği bir oturum) yürütür (7. ve 9–10. Hafta).
10. **Uygulamayı mağazada yayınlar.** Öğrenci S0–S6 izini izler: mağazayı seçer, geliştirici hesabı açar, uygulama kaydını oluşturur, test kanalına bir build yükler, testçi kaydeder, uygulamayı incelemeye gönderir, inceleme düzeltmelerini uygular ve yayınlar (3–11. Hafta).
11. **İnceler ve iş birliği yapar.** Öğrenci sabit dörtlü grupta haftalık incelemeye katılır, geri bildirimi alıntı olarak, kabul/ret kararı ve gerekçesiyle kaydeder ve sınıf arkadaşlarının işine paydaş, gözden geçiren ya da testçi olarak katkı verir (3. Hafta'dan).
12. **Ürünü savunur.** Öğrenci uygulamayı sınav görevlisinin önünde mağazadan kurar, koddaki ve belgelerdeki kararları gerekçelendirir ve poster ile sunum hazırlar (12–14. Hafta).

## Ders Materyali

Ders şablonu ve haftalık ödevler github.com/vedatcoskun-course/aiasd-template adresindedir. Her haftanın `ASSIGNMENT_NN` dosyası orada İngilizce ve Türkçe olarak bulunur; `AI_SETUP_CARD`, `AI_WEEKLY_WORKFLOW_STUDENT` ve `AI_SKELETON` köktedir.

1. Hafta'nın ön okuması Vaswani vd., "Attention Is All You Need" (2017) makalesi ve dört ders belgesidir: AI Technical Background; Development Environment and Tools; Working with AI Tools; ve Yazılım Geliştirmede Yapay Zekâyı Doğru Kullanmak (`AI_Doc5`; haftalık yapay zekâ günlüğünün istediği sekiz tekniği anlatır ve sınav kapsamındadır). 2. Hafta için öğrenciler iki tam SDLC belge seti (bir sınav salonu tahsis sistemi; simülatörlü bir asansör denetleyicisi) ile Platforms and Stores el kitabını okur.

Araçlar: Python 3.12, Git/GitHub, VS Code, Streamlit, açık ağırlıklı bir modelle Ollama, öğrencinin seçtiği iki sohbet asistanı (ücretsiz katman) ve bir mobil çatı (Flutter / React Native–Expo / Kotlin / Swift). Öğrenciler her hafta kendi dizüstü bilgisayarlarını getirir.

## Notlandırma

| Kalem | Puan | Açıklama |
|---|---|---|
| Haftalık Projeler | 60 | 12 hafta × 10 puan, 60'a ölçeklenir. Her hafta 5 puan dersin sonunda, 5 puan Cumartesi 23:59'da repodan okunur (1. Hafta 5 puandır ve tamamı Cumartesi okunur). Otomatik kontroller derste 5, Cumartesi 2 puan verir; öğretim üyesi yapay zekâ günlüğü (2) ve commit disiplini (1; her hafta değerlendirilir: derste farklı zamanlarda birkaç push (en az üç), her birinde yeni iş, ders dışında iş ilerledikçe yapılmış, her birinde biraz yeni iş olan birkaç commit (bir commit'in bitmiş bir parça olması gerekmez); şüpheli bir durumda önceki haftalara da bakılır) puanlarını verir. Kaçırılan ders için telafi yoktur. |
| Mağaza Bonusu | 15 | Yayın bonusu. Mağaza izi S0–S6 (öğrenci mağazayı seçer, geliştirici hesabı açar, uygulama kaydını oluşturur, test kanalına build yükler, testçi kaydeder, uygulamayı gönderir ve uygulama canlıya çıkar) her adımın teslim haftasında adım adım notlandırılır. O hafta yardım eden sınıf arkadaşları (katkıcılar) öğrencinin notundan pay kazanır. |
| Sunum | 15 | 13–14. Haftalarda proje savunması. Öğrenci uygulamayı sınav yapanın önünde mağazadan yükler ve koddaki ve belgelerdeki kararlar hakkındaki soruları yanıtlar. Uygulama geliştirme makinesinden değil, mağaza build'inden çalıştırılır. |
| Final Sınavı | 40 | Üniversitenin sınav döneminde yazılı final sınavı. SDLC belgelerini, yapay zekâ günlüğü pratiğini ve on iki haftanın teknik içeriğini kapsar. |

## Sınıf İçi Kurallar

- En az %70 devam zorunludur. Devamsızlığın her türlü nedeni kalan %30'luk hakkın içine sığmak zorundadır. Bu yüzden lütfen başından itibaren tüm derslere katılmaya çalışın; böylece acil durumlar için kendinize esneklik bırakırsınız.
- Ders sırasında konuşmaları en aza indirin. Uzun ya da dersi bozan tartışmalara izin verilmez. Bu kuralı ihlal eden öğrenciden yer değiştirmesi ya da salondan ayrılması istenir.
- Ders sırasında telefon görüşmesi, kısa mesaj, anlık mesaj, e-posta ve genel web gezintisine izin verilmez. Bilgisayarlar yalnızca dersin materyalini izlemek için kullanılabilir.
- Ders sırasında ses ya da görüntü kaydı kesinlikle yasaktır.
- Her türlü kopya ve akademik sahtekârlık, ilgili yasal kurallara göre işlem görür.

## Ders Planı

| Hafta | Tarih | Konu |
|---|---|---|
| 1 | 22/09 · 23/09 | Temeller: öğrenciler araçları kurar, Git/GitHub'ı öğrenir ve LLM'ler (büyük dil modelleri) ile transformer'larla ilk kez tanışır |
| 2 | 29/09 · 30/09 | Teklif Bölüm A ve Gereksinimler (SRS): öğrenciler problemi ve çözümü anlatır, paydaşları adlandırır ve kullanım senaryolarını yazar |
| 3 | 06/10 · 07/10 | Dörtlü gruplarda pitch ve inceleme; öğrencilerin pazarı ve rakipleri incelediği, ticari potansiyeli değerlendirdiği ve riskleri sıraladığı Teklif Bölüm B; mağaza seçilir (S0); bundan sonra bir gereksinim id'sinin anlamı değişmez |
| 4 | 13/10 · 14/10 | Tıklanabilir prototip ve test case'ler: öğrenciler kabul ölçütlerinden test case'ler yazar, bunları prototip üzerinde yürütür ve gereksinimleri günceller; geliştirici hesabı açılır (S1) |
| 5 | 20/10 · 21/10 | Tasarım ve API sözleşmesi; geliştirme sunucu iskeleti ve e-posta kodu / OTP ile girişle başlar; gereksinimler ve test case'ler taban çizgisi (baseline) olur |
| 6 | 27/10 · 28/10 | Sohbet botu I, motor: öğrenciler Ollama + Qwen'i çalıştırır, BGE-M3 gömmelerini oluşturur ve chat endpoint'ini yazar; uygulama kaydı oluşturulur (S2) |
| 7 | 03/11 · 04/11 | Sohbet botu II: sohbet botu web ve mobil istemcilere girer; testler; CI |
| 8 | 10/11 · 11/11 | Projenin kendi çekirdek özelliği üç katmanda birden çalışır; ilk build test kanalına çıkar (S3) |
| 9 | 17/11 · 18/11 | Beta testi: testçiler kaydedilir, öğrenciler hata listesi tutar ve test raporu yazar (S4) |
| 10 | 24/11 · 25/11 | UAT ve gönderim: öğrenciler UAT raporunu ve dağıtım diyagramını yazar, uygulama incelemeye gönderilir (S5) |
| 11 | 01/12 · 02/12 | Yayın ve sağlamlaştırma: öğrenciler inceleme düzeltmelerini uygular, uygulama mağazada canlıya çıkar ve son README yazılır (S6) |
| 12 | 08/12 · 09/12 | Kapanış: poster ve savunma provası |
| 13 | 15/12 · 16/12 | **Proje savunması (sunumlar)** |
| 14 | 22/12 · 23/12 | **Proje savunması (sunumlar)** |
| | | **Final Sınavı** |

*Not: haftalık plan sınıfın ilerlemesine göre değiştirilebilir.*
