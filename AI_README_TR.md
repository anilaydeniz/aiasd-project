# AIASD Projesi — Öğrenci Deposu

**AI-Assisted Software Development · Atlas Üniversitesi · Güz 2026–2027**
**Prof. Dr. Vedat Coşkun**

*English: [`AI_README_EN.md`](AI_README_EN.md)*

---

## Bu depo nasıl kullanılır

Bu, 12 haftalık dersin tamamı için kişisel proje deponuzdur (depo, projenizin git
tarafından izlenen klasörüdür; hem bilgisayarınızda hem GitHub'da durur). Onu 1. Hafta'da
ders şablonundan (GitHub'ın sizin için kopyaladığı hazır bir depo) oluşturursunuz ve her
hafta ona commit edersiniz (commit, dosyalarınızın git tarafından kaydedilen bir anlık
görüntüsüdür).

Her hafta kendi ödeviyle, kendi klasöründe gelir ve ödev, tam olarak ne yapacağınızı ve
ne teslim edeceğinizi söyler. [`AI_SKELETON_TR.md`](AI_SKELETON_TR.md) dönemin tamamını
iki sayfada anlatır: her haftanın ne öğrettiğini, neyi push edeceğinizi (push etmek,
commit'lerinizi bilgisayarınızdan GitHub'a göndermektir) ve ne zaman edeceğinizi söyler.
Dönem boyunca tek bir ürün yaparsınız ve o ürün sizindir: bir mobil istemci, bir web
istemcisi ve bir sunucu. Onu seçtiğiniz bir public mağazada yayınlarsınız ve dönem
sonunda, o mağazadan yüklediğiniz uygulama üzerinden savunursunuz.

Çoğu hafta ayrıca bir yapay zekâ günlüğü ister (o hafta bir yapay zekâ asistanını nasıl
kullandığınızın yazılı kaydı). Günlük, o haftanın klasörünün içindeki
`weekNN/ai_log_NN.md` dosyasıdır.

### Şu an burada ne var, ne yok

Şu anda bu depoda dönem boyunca burada kalan dosyalar ve `week01/` var. `week02/` klasörü
yok ve olmamalı, çünkü **her haftanın klasörünü, o haftanın ödevi söylediğinde siz
oluşturursunuz.** Dosyayı doğru yere koymak işin parçasıdır. Yanlış yere koyduğunuzda
denetleyici (her haftanın gerektirdiği dosyaları arayan otomatik betik; aşağıdaki
"Otomatik kontroller" bölümüne bakın) aradığı tam yolu adıyla söyler.

Aşağıdaki dosyalar köktedir ve dönem boyunca orada kalır:

| | |
|---|---|
| `app.py` | Bu dosya uygulamanızdır. Şimdilik boştur ve hafta hafta büyüyerek ürünün tamamı olur |
| `week01/ASSIGNMENT_01_EN.md`, `_TR.md` | Bu dosyalar bu haftanın ne istediğini iki dilde söyler. Haftanın klasörüyle birlikte gelirler ve görevlerin yazılı olduğu tek yerdirler |
| `week01/ai_log_01.md` | Bu dosya bu haftanın yapay zekâ günlüğüdür ve bu haftanın klasöründe durur. Her haftanın bir tane vardır ve haftayla birlikte gelir |
| `student.json` | Bu dosya kim olduğunuzu söyler. 1. Hafta'da bir kez doldurun |
| `requirements.txt`, `weekNN/requirements.txt` | Bu dosyalar bağımlılıkları (uygulamanızın ihtiyaç duyduğu Python paketlerini) listeler. Hafta hafta gelirler |
| `.github/` | Bu klasör her push'ta çalışan kontrolleri tutar |
| `CURRENT_WEEK.txt` | Bu dosya denetleyicinin yönettiği bir kayıttır. Düzenlemeyin. Denetleyiciyi ilk çalıştırdığınızda yanında `CURRENT_WEEK_CACHE.txt` adlı bir dosya belirir. O dosya denetleyicinin çevrimdışı önbelleğidir (hafta numarasının kaydedilmiş bir kopyası), git onu izlemez ve yok sayabilirsiniz |

Birkaç hafta size bir iskelet verir (sıfırdan başlamayasınız diye kısmen yazılmış
dosyalar içeren bir başlangıç klasörü). Bu olduğunda ödev tek bir komutla açılır ve o
komutu, o klasörde bir şey oluşturmadan **önce** çalıştırırsınız:

```bash
git remote add template https://github.com/vedatcoskun-course/aiasd-template.git
git fetch template
git checkout template/main -- week06
```

İlk satır bütün dönemde yalnızca bir kez gerekir. Bu komutları o klasöre zaten dosya
yazdıktan sonra çalıştırırsanız, komutlar dosyalarınızın üzerine yazar. O yüzden ya önce
çalıştırın ya da hiç çalıştırmayın.

**Buradan başlayın:** [`AI_SETUP_CARD_TR.md`](AI_SETUP_CARD_TR.md) / [`AI_SETUP_CARD_EN.md`](AI_SETUP_CARD_EN.md)
dönem boyunca çalıştıracağınız her komutu, sık karşılaşılan hataların ne anlama
geldiğinin açıklamasıyla birlikte tek sayfada tutar. Dört kurulum adımını 1. Hafta'dan
önce yapın.

**Yeni misiniz?** Haftalık rutinin tamamı
[`AI_WEEKLY_WORKFLOW_STUDENT_TR.md`](AI_WEEKLY_WORKFLOW_STUDENT_TR.md) /
[`AI_WEEKLY_WORKFLOW_STUDENT_EN.md`](AI_WEEKLY_WORKFLOW_STUDENT_EN.md) dosyasında adım
adım yazılıdır. Her dersten önce, ders sırasında ve sonra ne yapacağınızı, puanların nasıl
bölündüğünü ve takıldığınızda ne deneyeceğinizi söyler.

**1. Hafta'dan önce okuyun.** Üç ön okuma ve makale köktedir. Ön okumalar `AI_Doc2` AI
Technical Background, `AI_Doc3` Development Environment and Tools ve `AI_Doc4` Working
with AI Tools'dur. Makale ise `AI_Doc1`, Transformer makalesidir (bugünkü yapay zekâ
asistanlarının arkasındaki araştırma makalesi). Ders, bu dört belgenin yirmi dakikalık
özetidir. Sonraki okumalar aynı biçimde, sırayla numaralanmış olarak gelir. `AI_Doc5`
Yazılım Geliştirmede Yapay Zekâyı Doğru Kullanmak, haftalık yapay zekâ günlüğünüzün
istediği sekiz tekniği anlatır. 4. Hafta'dan itibaren her hafta bir teknik zorunludur ve
bu belge final sınavında çıkar.

İki şube de aynı dosyaları alır. Ödevler, kurulum kartı ve iş akışı `_EN` ve `_TR` ile
işaretlenmiş olarak iki dilde gelir. Kendi dilinizdekini okuyun, diğerini yok sayın.
Okumalar (`AI_DocN`) İngilizcedir. Denetleyicinin aradığı klasör ve dosya adları
(`week01/`, `hello.py`, `student.json`) herkes için aynıdır.

---

## Uygulamayı çalıştırma

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Bağımlılıklar hafta hafta gelir; böylece 1. Hafta'da gigabaytlarca paket indirmezsiniz.
Kökteki `requirements.txt` asgaridir. Ağır bir haftanın kendi `weekNN/requirements.txt`
dosyası olur ve o haftanın ödevi ne zaman kurulacağını söyler:

```bash
pip install -r weekNN/requirements.txt
```

---

## Kim olduğunuz — `student.json`

Bu dosyayı 1. Hafta'da, depo kökünde doldurun:

```json
{
  "student_id": "20210042",
  "first_name": "Ayşe",
  "last_name": "Yılmaz",
  "nickname": "kaplumbaga",
  "section": "tr"
}
```

**section** alanınız, İngilizce şubedeyseniz `en`, Türkçe şubedeyseniz `tr` olur. Bunu
yanlış yazarsanız denetleyici sizi diğer şubenin haftasına göre sınar; o yüzden push
etmeden önce kontrol edin.

**nickname** alanınız, her ders sonunda yansıtılan sınıf panosunda görünen addır; böylece
kendi satırınızı bir bakışta bulursunuz. Harf, rakam, `-` ve `_` içerebilir ve 2–20
karakter uzunluğunda olmalıdır. İstediğinizi seçin, ama Aralık'ta hâlâ tanıyacağınız bir
şey seçin.

Ders sürerken bu depoyu **private** tutun, çünkü öğrenci numaranızı ve adınızı taşır.

---

## Otomatik kontroller

Her push, hocanızın çalıştırdığı kontrollerin aynısını çalıştırır. GitHub'da commit'inizin
yanında yeşil tik ya da kırmızı çarpı görürsünüz ve tam olarak hangi kontrolün başarısız
olduğunu görebilirsiniz.

**Açmanız gereken bir şey yok.** Denetleyici her çalıştığında derse hangi haftada
olduğunu sorar; bu yüzden gördüğünüz her zaman size karşı çalıştırılan şeydir. Depo
kökündeki `CURRENT_WEEK_CACHE.txt` dosyası yalnızca o hafta numarasının önbelleğidir.
Kendini günceller ve ona hiçbir zaman dokunmanız gerekmez.

Çıktı iki parça hâlinde gelir, çünkü haftanın iki teslim anı vardır:

```
In the lab:     11 of 13 done
By Saturday:     2 of  8 done
```

**In the lab**, ders sonu anlık görüntüsünün okuduğu kısımdır (anlık görüntü, deponuzun
o andaki hâlinin birebir kopyasıdır). Haftanın on puanının beşi bu kısımdandır. **By
Saturday** gerisidir, yani yazılar, diyagramlar ve `ai_log_NN.md`. İkinci gruptakiler
hafta açıkken çalıştırmayı başarısız kılmaz, çünkü henüz teslim vakti gelmemiştir.
Birinci gruptaki hiçbir şey evde yapmanız gereken bir şey değildir. (1. Hafta
istisnadır: ilk dersin sonunda hiçbir şey okunmaz ve beş puanının tamamı Cumartesi
okunur.)

Haftalar birikimli denetlenir; yani 3. Hafta, 1 ve 2. Haftaları da yeniden denetler.
Sonraki bir değişiklik eskiyi bozarsa bunu Aralık'ta değil CI'dan (GitHub'ın her push'ta
çalıştırdığı otomatik kontroller) duymak istersiniz.

Tek bir haftaya bakmak için, örneğin 2. Hafta'nın hâlâ geçtiğini doğrulamak için şunu
çalıştırın:

```bash
AIASD_WEEK=2 python .github/check_deliverables.py
```

Push etmeden önce kontrolleri yerelde (kendi bilgisayarınızda) çalıştırın:

```bash
python .github/check_deliverables.py
```

Kırmızı çarpı bir not değildir. Hâlâ eksik olanların listesidir ve o listeyi teslimden
sonra değil Salı günü görmek çok daha iyidir.

**Gizli anahtar taraması her push'ta, her hafta çalışır.** Gizli anahtar taraması
dosyalarınızda şifre ve anahtar arar. Bir API anahtarı (bir programın sizin adınıza bir
hizmeti kullanmasını sağlayan gizli bir dize) depoya ulaşırsa kontrol gürültüyle başarısız
olur. Anahtarı kaldırın, hemen yenileyin (yani eski anahtarı iptal edip yenisini
oluşturun) ve commit edilmiş bir anahtarın otomatik 10 puan kesinti olduğunu unutmayın.

---

## Depo kuralları

- **Her derste birkaç kez push edin** (en az üç), her seferinde yeni işle; ders dışında da **çalıştıkça birkaç kez commit edin**; her birinde biraz yeni iş olsun, bitmiş bir parça olması gerekmez. Cumartesi gecesi tek bir push yapıp başka bir şey yapmazsanız, bu size commit disiplini puanına mal olur.
- O haftanın `ai_log_NN.md` dosyasını doldurun. Her haftanın bir tane vardır ve onu bir insan okur.
- `.venv/`, `__pycache__/` ya da API anahtarlarını **commit etmeyin**.
- Commit'ten önce `ruff check .` çalıştırın (`ruff`, Python kodundaki yaygın hataları bildiren bir araçtır). Yapay zekânın geride bırakma eğilimindeki kullanılmayan import'ları yakalar.
- Gizli değerler için `.env` (gizli değerleri tutan küçük bir dosya) kullanın ve onu `.gitignore` içinde (git'in asla commit etmemesi gereken dosyaların listesi) tutun.
- Uygulamanız dizüstünde olduğu kadar telefonda da çalışmalı. Tarayıcı pencerenizi ara sıra ~390px'e daraltın. Bir şey kesiliyor ya da yana kayıyorsa sayfa küçükken düzeltin, 10. Hafta'da değil.
