# 5. Hafta Ödevi — Tasarım, API Sözleşmesi ve Sunucu İskeleti

**Teslim:** ders içi bölüm dersin sonuna kadar (11:45) · kalanı Cumartesi 23:59 · Proje reponuza commit edin

## Projenizde şimdiye kadar ne yaptık, bundan sonra ne yapacağız

Bir ay önce projeniz yalnızca aklınızdaki bir fikirdi, şimdi neye dönüştüğüne bakalım:

- **1. hafta:** araçlarınızı kurmak ve iki yapay zeka asistanıyla konuşmalarınızı gerçekleştirmek.
- **2. hafta:** gerçek bir problem bulmak, o problemi yaşayan gerçek insanlar ve ürününüzün yapması gerekenlerin ilk listesini oluşturmak.
- **3. hafta:** projenizi arkadaşlarınıza sundunuz, pazara ve rakiplere baktınız.
- **4. hafta:** proje ekranlara dönüştü. Bir sınıf arkadaşınız onlara tıkladı ve ürününüzü bir başkasının gözünden gördünüz.

Bu haftadan itibaren projeniz yazılıma dönüşüyor. Ürününüz bir iskelet kazanıyor: nelerden oluştuğuna karar
veriyorsunuz, parçalarının birbirine verdiği sözleri (API sözleşmesi) yazıyorsunuz ve gerçek bir sunucu size
ilk kez cevap veriyor. Gelecek hafta bir kullanıcı, e-posta kutusuna gelen bir kodla giriş yapacak. 7.
haftada aynı giriş bir telefonda çalışacak. 8. haftada ürününüz, var oluş nedeni olan işi sunucuda, web'de
ve telefonda yapacak. Ardından gerçek testçiler ve mağazanın incelemesi gelecek; Aralık'ta kendi
uygulamanızı, juri önünde iken bir mağazadan indireceksiniz.

Bu hafta, mühendislerin en çok keyif aldığı haftadır: bir tasarımın koda dönüştüğü an. Bir sözleşmenin
birkaç satırını elle yazacak, sunucunuzun endpoint'lerini `/docs` sayfasında listelediğini görecek ve
bilerek başarısız olan testler yazacaksınız, çünkü bekledikleri kod henüz yok. Gelecek hafta onları tek tek
yeşile döndüreceksiniz.

## Bu hafta: ne kuruyorsunuz ve projedeki yeri ne

Bu hafta, geri kalan her şeyin üzerine kurulacağı parçayı kuruyorsunuz:

- **Tasarım** (`week05/DESIGN.md`): ürününüzün hangi parçalardan oluştuğu ve her parçanın hangi gereksinime
  hizmet ettiği.
- **API sözleşmesi** (`week05/api.md`): sunucunuzun istemcilerine verdiği söz: ne isteyebilecekleri, ne
  alacakları ve bir isteğin başarısız olabileceği her yol.
- **Sunucu iskeleti** (`server/`): sözleşmedeki her endpoint'e şimdiden cevap veren gerçek bir sunucu; şimdilik
  yalnızca "henüz yapılmadı" diyerek de olsa.
- **İlk testler**: giriş test case'leriniz, koda dönüşmüş ve girişi bekliyor.

Neden önemli: 6. haftada bugün listelediğiniz endpoint'lerin arkasına girişi kuracaksınız ve web istemciniz
[]()bu endpoint'leri çağıracak. 7. haftada mobil istemciniz aynı endpoint'leri, hiç değiştirmeden
çağıracak. 8. haftada ürününüzün kendi özelliği aynı sözleşmeye yeni satırlar, aynı tasarıma yeni bileşenler
ekleyecek. Şimdi yazdığınız her test, sonraki haftalarda bir asistan kodunuzu her değiştirdiğinde onu izlemeye
devam edecek. Sözleşmedeki bir hata bugün bulunursa size bir satıra mal olur; 8. haftada bulunursa sunucuya
ve iki istemciye.

### Bu hafta bilmeniz gerekenler

| | Nedir |
|---|---|
| **Sunucu ve istemciler** | Sunucu verileri ve kuralları tutar. Web istemcisi ve mobil istemci ekranları gösterir ve her şeyi sunucuya sorar. |
| **Bileşen** | Sisteminizin tek bir işi olan bir parçası: "Sunucu: giriş", "Veritabanı", "Mobil istemci". |
| **Endpoint** | Sunucunun cevap verdiği tek bir şey: bir metot ve bir yol, örneğin `POST /auth/code`. `GET` okur, `POST` gönderir ya da oluşturur, `PUT` ve `PATCH` değiştirir, `DELETE` siler. |
| **İstek, cevap, durum kodu** | İstemcinin gönderdiği, geri dönen ve işin nasıl gittiğini söyleyen bir sayı: 200 çalıştı, 401 giriş yapılmamış, 422 yanlış bir alan, 501 henüz yapılmadı. |
| **JSON** | İki tarafın istek ve cevaplarda kullandığı metin: `{"email": "deniz@example.com"}`. |
| **API sözleşmesi** | Bütün endpoint'ler tek bir tabloda, `api.md`: sunucunun, iki istemcinin ve her testin üzerinde anlaştığı sayfa. |
| **FastAPI, route, uvicorn** | FastAPI sunucunuzun Python kütüphanesidir; route, tek bir endpoint'e cevap veren tek bir fonksiyondur; uvicorn sunucuyu çalıştırır ve `/docs` her route'u listeler. Tek sayfada: `week05/FASTAPI_CARD_TR.md`. |
| **Test, pytest** | Koda dönüşmüş bir test case; `pytest` hepsini çalıştırır. Bir testin adı test case kimliğiyle başlar. Kırmızı başarısız oldu, yeşil geçti demektir. |
| **Taban çizgisi, değişiklik isteği** | Cumartesi'den itibaren gereksinimleriniz ve test case'leriniz sabittir; onları değiştirmek artık yazılı bir değişiklik isteği gerektirir. |
| **Mermaid** | 2. haftadan bildiğiniz metin tabanlı diyagram gösterimi; bu hafta mimarinizi çizer. |

## Ne, ne zaman teslim edilir

| Ne zaman | Ne yaparsınız | Nerede |
|---|---|---|
| **Dersten önce** | Denetleyiciyi bir kez çalıştırın, `week05/requirements.txt` dosyasındakileri kurun, başlangıç testinin geçtiğini görün, `week05/FASTAPI_CARD_TR.md` dosyasını okuyun (10 dakika) | aşağıdaki kutu |
| **Derste, 11:45'e kadar push** | **`api.md` dosyasının giriş satırları, sizin elle yazdığınız, 10:00'da push** · `DESIGN.md` içindeki Components tablosu (en az dört bileşen) · `api.md` dosyasının her satırı için `server/` içinde bir route · test case kimliğiyle adlandırılmış, çalıştırılmış ve doğru nedenle başarısız olan ilk giriş testi · 10:00, 11:00 ve 11:45'te push | §1–§5 |
| **Cumartesi 23:59'a kadar** | `api.md` tamamlanmış · test case kimlikleriyle adlandırılmış en az üç giriş testi · her işlevsel `must` gereksinime bir bileşen hizmet ediyor · Mermaid ile mimari · `ai_log_05.md` · `requirements.json` ve `test_cases.json` dosyalarındaki son değişiklikler: bu dosyalar **taban çizginiz (baseline)** olur | §6–§11 |

`api.md` dosyasının giriş satırları koddan sonra yazılamaz: sunucunuzun route'ları henüz
yokken, 10:00'daki push'unuzdan okunur.

> ## AI log'u (yapay zeka günlüğü) insan yazar. İstisna yok.
>
> `week05/ai_log_05.md` dosyasını **siz**, kendi cümlelerinizle yazarsınız. Evidence bloğunun
> ve asistanın cevabından yaptığınız kalın alıntıların (§10) dışında asistan kullanılmaz: ne
> yazmak için, ne "düzeltmek" için, dil için bile. **Asistana yazdırılmış bir günlük 0 puan alır.**
> Dil notlanmaz; her günlüğü bir insan okur.

> ## `api.md` dosyasının giriş satırlarını, herhangi bir koddan önce, elle yazarsınız.
>
> Bir istemcinin ne gönderdiği, ne geri döndüğü ve girişin başarısız olabileceği her yol bu
> haftanın kararıdır ve bu karar sizindir. Satırları, bir asistandan tek bir satır kod
> istemeden önce, REQ-001'den ve test case'lerinizden yazın. Kod sözleşmeden yazılır,
> tersi değil.

> **Bu hafta tek başınıza çalışırsınız.** Collaborator yok, `group_05.json` yok, katkı
> bonusu yok. Grubunuz 6. haftadan itibaren yeniden toplanır.

> **Dersten önce:** `python .github/check_deliverables.py` komutunu bir kez çalıştırın. Komut
> `week05/` klasörünü ve reponuzun kökünde yeni bir klasör olan `server/` klasörünü getirir.
> Sonra, sanal ortamınız etkinken:
>
> ```bash
> pip install -r week05/requirements.txt
> python -m pytest
> ```
>
> Son satır `1 passed` demelidir. Kurulum başarısız olursa derse hata mesajıyla gelin,
> mesajsız değil. `week05/FASTAPI_CARD_TR.md` dosyasını okuyun: tek sayfa, on dakika.

Neden koddan önce sözleşme? Web istemciniz (6. hafta) ve mobil istemciniz (7. hafta) API
sözleşmesine göre yazılır. Sözleşme koddan sonra yazılırsa, yalnızca asistanın o an ne
yazdıysa onu anlatır ve test case'leriniz artık gereksinimlerinizi test etmez. Önce yazılırsa,
sunucunun, iki istemcinin ve her testin üzerinde anlaştığı tek sayfa olur.

---

## Bu hafta gelenler

Denetleyiciyi bir kez çalıştırın:

```bash
python .github/check_deliverables.py
```

`week05/` içine şunları getirir: bu ödev, `DESIGN.md` ve `api.md` (haftanın iki belgesi,
içlerinde yönergelerle), `ai_log_05.md`, `requirements.txt` (FastAPI ve pytest, tam
sürümleriyle) ve `FASTAPI_CARD_TR.md` (tek sayfa: bir asistanın FastAPI için yazdığı kod
nasıl okunur).

Reponuzun kökünde de `server/` klasörünü getirir: `main.py`, tek endpoint'i `/health` olan bir
sunucu, ve `tests/test_health.py`, geçen tek bir test. Sunucu dönemin geri kalanında
`server/` içinde kalır; 6. ile 8. haftalar onun üzerine kurulur.

Sunucuyu reponuzun kökünden başlatın:

```bash
uvicorn server.main:app --reload
```

Sonra tarayıcınızda http://127.0.0.1:8000/docs adresini açın. FastAPI sunucunuzun her
endpoint'ini orada listeler ve her birini deneyebilirsiniz. Sunucuyu Ctrl+C ile durdurun.

---

## Bu hafta asistan nerede yardım eder, nerede etmez

| Parça | Asistan |
|---|---|
| Bir route'un FastAPI kodu (`api.md` satırı isteme yapıştırılır; bir route, bir commit) | **Yardım eder** |
| Test case'lerinizden birinden bir testin kodu (test case'in söylediğini test edip etmediğini siz kontrol edersiniz) | **Yardım eder**, onay sizde |
| Gereksinimlerinizden bir bileşen önerisi | **Yardım eder**, karar sizde |
| Mimarinizin Mermaid sözdizimi | **Yardım eder** |
| Bir hata mesajını açıklamak | **Yardım eder** |
| `api.md` dosyasının giriş satırları: metot, yol, istek, cevap, hatalar | **Yardım yok**: herhangi bir koddan önce siz yazarsınız |
| Testleri ve sunucuyu çalıştırmak ve ekrana yazdıklarını okumak | **Yardım yok**: kendiniz çalıştırırsınız |
| Değişiklik günlüğü satırları ve Pazar'dan itibaren değişiklik istekleri | **Yardım yok** |
| `ai_log_05.md` (Evidence bloğu ve kalın alıntılar dışında) | **Yardım yok** |

---

## Derste — dersin sonuna (11:45) kadar push edilir

Yaklaşık yirmi dakika anlatım ve kısa bir FastAPI gösterimi; sonra bileşenler ve `api.md`
dosyasının giriş satırları (**10:00**'da push); sonra sunucunuzun route'ları (**11:00**'de
push); sonra ilk giriş testi, denetleyici ve dersin sonundaki push
(**11:45**).

### 1. Tasarım — `week05/DESIGN.md`

**Ne zaman:** derste en az dört bileşen, 11:45'e kadar push; Cumartesi'ye kadar her işlevsel
`must` gereksinime bir bileşen hizmet eder ve mimari çizilmiş olur (§8).

Bileşen, sisteminizin tek bir işi olan bir parçasıdır. Tablo her bileşenin adını verir, ne
yaptığını tek cümleyle söyler ve hizmet ettiği gereksinimleri listeler. StudyRoom için:

| Bileşen | Ne yapar | REQ |
|---|---|---|
| Sunucu: giriş | Bir e-posta adresine 4 haneli bir kod gönderir, kodu kontrol eder ve bir token verir | REQ-001 |
| Sunucu: rezervasyonlar | 30 ile 120 dakika arası boş bir dilim için rezervasyonu kaydeder, dolu bir dilimi reddeder | REQ-002, REQ-003 |
| Veritabanı | Kullanıcıları, odaları ve rezervasyonları tutar | REQ-002, REQ-004 |
| Web istemcisi | Prototipin ekranları, tarayıcıda, 390 px genişlikte | REQ-006 |
| Mobil istemci | Aynı ekranlar bir telefonda | REQ-006 |

Kurallar:

- **Her bileşene, kodunuzda vereceğiniz adı verin.** "Sunucu: rezervasyonlar" 8. haftada
  `server/bookings.py` olur.
- **Ne yaptığına dair tek cümle.** Üç kez "ve" demeniz gerekiyorsa, bunlar iki bileşendir.
- **REQ kimlikleri `week02/requirements.json` içinde bulunur.** Hiçbir gereksinime hizmet
  etmeyen bir bileşenin var olmak için bir nedeni olmalıdır; nedeni yoksa tabloda yeri yoktur.
- İlk satır, yani giriş, herkes için aynıdır ve dosyada zaten vardır. Onu koruyun ve
  ifadelerini kendinize göre düzenleyin.

Asistanınız gereksinimlerinizden bileşenler önerebilir. Karar sizindir: ürününüzün hangi
parçalara ihtiyacı olduğunu siz bilirsiniz, asistan bilmez.

ZAYIF: *"| Backend | Her şeyi yapar | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005 |"*
GÜÇLÜ: yukarıdaki tablo.

### 2. API sözleşmesi — giriş satırları, elle

**Ne zaman:** derste elle yazılır ve 10:00'da push edilir; `api.md` dosyasının geri kalanı
Cumartesi'ye kadar (§6).

**Endpoint**, sunucunuzun cevap verdiği tek bir şeydir: `POST /auth/code` gibi bir metot ve
bir yol (path). İstemci bir **istek** (request) gönderir ve bir **cevap** (response) alır; cevapla
birlikte bir **durum kodu** (status code), yani işin nasıl gittiğini söyleyen bir sayı gelir:

| Kod | Anlamı |
|---|---|
| 200 | Çalıştı; cevap burada |
| 201 | Çalıştı ve yeni bir şey oluşturuldu |
| 400 | İstek hatalı |
| 401 | Giriş yapmamışsınız ya da kodunuz veya token'ınız yanlış |
| 404 | Böyle bir şey yok |
| 409 | Zaten var olanla çakışıyor (dolu bir dilim) |
| 422 | Bir alan eksik ya da biçimi yanlış (e-posta adresi değil) |
| 429 | Çok fazla istek: bekleyin |
| 501 | Henüz yapılmadı |

Her projede giriş aynı şekilde yapılır (REQ-001): kullanıcı bir e-posta adresi verir, 4
haneli bir kod alır ve bu kodla giriş yapar. Bu yüzden giriş için **en az iki endpoint**
gerekir: biri kod ister, diğeri kodla giriş yapar. İki satırı da REQ-001'den ve TC-001-01 ile
TC-001-02 test case'lerinizden kendiniz yazın: ne girdiği, ne geri döndüğü ve başarısız
olabileceği her yol, her biri kendi durum koduyla. StudyRoom'un ilk satırı şöyledir:

| Metot | Yol | İstek | Cevap | Hatalar | REQ |
|---|---|---|---|---|---|
| POST | /auth/code | {"email": "deniz@example.com"} | 200 {"sent": true} | 422 e-posta adresi değil · 429 bir dakikadan daha kısa süre önce kod istendi | REQ-001 |

İkinci satırı, yani kodla girişi, siz yazarsınız. Test case'lerinizin neye ihtiyaç duyduğunu
kendinize sorun: kod doğruysa istemci ne alır, yanlışsa ya da çok eskiyse ne
alır?

**Bu satırları elle yazın ve herhangi bir koddan önce, 10:00'da push edin.** Hiçbir asistan
onları yazmaz, düzeltmez ya da tamamlamaz. Bunlar için 10:00'daki push okunur.

### 3. Sunucu iskeleti — `server/main.py`

**Ne zaman:** derste; 11:00'de ve 11:45'te push.

`api.md` dosyasının her satırı için sunucunuz bir **route** alır: aynı metodu ve aynı yolu
olan bir fonksiyon. İşi daha sonra yapılacak bir route, kendi haftası gelene kadar **501** ile cevap verir:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="StudyRoom")


class CodeRequest(BaseModel):
    email: str


@app.post("/auth/code")
def ask_for_code(body: CodeRequest) -> dict:
    """REQ-001: sends a 4-digit code to the e-mail address. Built in Week 6."""
    raise HTTPException(status_code=501, detail="Not built yet: Week 6")
```

Kurallar:

- **`api.md` dosyasının her satırının bir route'u, her route'un da bir satırı vardır**; metot
  ve yol aynıdır. Denetleyici ikisini iki yönde de karşılaştırır.
- **Route'lar `server/main.py` içinde bulunur**, ya da FastAPI'nin `APIRouter`'ı ile `server/`
  içindeki başka dosyalarda. Testler `server/tests/` içinde bulunur.
- **Her route'un, gereksinimini söyleyen bir ilk satırı vardır**, yukarıdaki gibi.
- **Bir route, bir commit.** Asistanınızdan bir seferde tek route isteyin ve `api.md`
  satırını isteme yapıştırın. Kabul etmeden önce cevabın tamamını okuyun ve istemediğiniz
  şeyi reddedin. Asistanlar "yardım etmeyi" sever: kodu her zaman 1234 olan tamamlanmış bir
  giriş, bir şifre alanı, planlamadığınız bir veritabanı. Bu hafta route'lar yalnızca 501 ile cevap verir.
- Sunucuyu yeniden başlatmanız gerekmez: `--reload` ile her kaydı algılar. `/docs` sayfasını
  açın ve `api.md` dosyasının her satırının orada olduğunu kontrol edin.

### 4. İlk giriş testi — `server/tests/test_login.py`

**Ne zaman:** derste en az bir test, çalıştırılmış ve doğru nedenle başarısız, 11:45'e kadar
push; Cumartesi'ye kadar en az üç test (§7).

Test, koda dönüştürülmüş bir test case'tir. Adı, alt çizgiyle yazılmış test case kimliğiyle
başlar; böylece herkes onun hangi test case'i kontrol ettiğini bulabilir:

```python
from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


def test_TC_001_01_a_code_is_sent_to_a_valid_email():
    response = client.post("/auth/code", json={"email": "deniz@example.com"})
    assert response.status_code == 200
    assert response.json() == {"sent": True}
```

Bütün testleri reponuzun kökünden çalıştırın:

```bash
python -m pytest
```

Bugün bu test **başarısız olur** ve olmalıdır: route 501 ile cevap verir, çünkü giriş 6.
haftada yapılır. Neden başarısız olduğunu okuyun. `assert 501 == 200` satırı doğru nedendir.
`assert 404 == 200`, route'un eksik olduğu ya da yolunun `api.md`'dekinden farklı olduğu
anlamına gelir; `ImportError`, testin sunucunuzu bulamadığı anlamına gelir. Bunları düzeltin,
çünkü yanlış nedenle başarısız olan bir test hiçbir şeyi test etmez. Kod var olmadan önce
geçen bir test de hiçbir şeyi test etmez (`AI_Doc5` §2).

Asistanınız testi test case'inizden yazabilir. Onu test case'le karşılaştırın: aynı değerler,
aynı beklenen sonuç. Başarısız bir testi beklenen değeri değiştirerek "düzelten" bir asistan,
testi işe yaramaz hale getirmiştir.

### 5. Push

```bash
python .github/check_deliverables.py
git add .
git commit -m "week05: login rows of the API contract"
git push
```

**10:00**'da, **11:00**'de ve dersin sonunda, **11:45**'te push edin; her seferinde yeni işle
ve o saatten en fazla on beş dakika farkla. 10:00'daki push giriş satırlarınızı taşır.
11:45'ten hemen sonra bütün repoları dondururum. Push edilmemiş olan yoktur.

---

## Cumartesi 23:59'a kadar

### 6. API sözleşmesinin tamamı — `week05/api.md`

Sunucunuzun her endpoint'inin bir satırı, her satırın da bir route'u vardır. Şimdilik bunlar
giriş ve `/health`. Bir giriş genellikle bir endpoint daha gerektirir: istemcinin, token bir
`Authorization` başlığındayken, kimin giriş yaptığını öğrenmek için çağırdığı endpoint.
Sizinkinin buna ihtiyacı olup olmadığına karar verin.

Bir gereksinime hizmet eden her endpoint için: istek, 2xx koduyla cevap ve 4xx koduyla her
hata. Diğer özelliklerinizin endpoint'leri kendi haftalarını bekleyebilir; şimdi birini
eklerseniz route'u da onunla birlikte gelir.

### 7. Giriş testleri — `server/tests/test_login.py`

Her biri `week04/test_cases.json` içindeki bir test case kimliğiyle adlandırılmış en az **üç**
test: kod gönderilir, yanlış bir kod reddedilir, eski bir kod reddedilir, çok erken istenen
ikinci bir kod reddedilir. Bir test henüz var olmayan bir test case'e ihtiyaç duyarsa
(örneğin 429 kuralı), o test case'i Cumartesi'den önce, bir Değişiklik günlüğü satırıyla
`test_cases.json` dosyasına ekleyin: Cumartesi'den sonra bu bir değişiklik isteği olur (§9).

Hepsi 6. haftaya kadar, doğru nedenle başarısız olur. Plan budur: 6. haftada girişi, testler
tek tek geçene kadar yaparsınız. Testleri herhangi bir giriş kodundan önce commit edin: commit
geçmişiniz hangisinin önce geldiğini gösterir.

### 8. Tasarımın tamamı — `week05/DESIGN.md`

- Her işlevsel `must` gereksinime en az bir bileşen hizmet eder.
- **Mermaid diyagramı olarak mimari**, aynı dosyada: bileşenleriniz ve her "konuşur" ilişkisi
  için bir ok. GitHub onu çizer.

### 9. Taban çizgisi (baseline)

**Cumartesi 23:59**'da `week02/requirements.json` ve `week04/test_cases.json` **taban
çizginiz** olur. Son değişikliklerinizi bundan önce, her birini kendi Değişiklik günlüğü satırıyla yapın.

Pazar'dan itibaren bu iki dosyadan birindeki her değişiklik bir **değişiklik isteği (change
request)** olur: `PROPOSAL.md` içinde, `CR-` ve bir numarayla başlayan, değişikliği ve
kimlikleri anan ve etkilediği her dosyayı listeleyen bir Değişiklik günlüğü satırı:

"2026-10-28 — CR-01: REQ-004 artık 15 dakikalık dilimlere izin veriyor; etkilediği dosyalar: requirements.json,
test_cases.json (TC-004-02), week05/api.md, server/bookings.py."

### 10. Çalıştırarak doğrulayın — `week05/ai_log_05.md`

Asistanınızın yazdığı bir route'u ya da bir testi seçin. **Çalıştırmadan önce**, ne
beklediğinizi test case kimliğiyle birlikte yazın. Sonra kendiniz çalıştırın: `python -m pytest`
ya da sunucu ve `/docs`. Komutu ve çıktısını, son satıra, yani testleri sayan satıra kadar,
Evidence bloğuna `TERMINAL:` altına yapıştırın. Sonra asistanın kodundan değiştirdiğiniz ya da
reddettiğiniz bir satırı ve nedenini yazın. Yönergeler ve bir zayıf/güçlü örnek dosyanın içindedir.

**AI log'u bir insan yazar: siz.** Evidence bloğunun ve kalın alıntıların dışında asistan
kullanılmaz; ne yazmak için, ne düzeltmek için, dil için bile. **Asistana yazdırılmış bir
günlük 0 puan alır.** Sizin sözleriniz düz yazıdır; asistanın sözleri, onlara işaret ettiğiniz
yerde, kalındır ve 4. haftadaki gibi Evidence bloğunda da bulunur.

### 11. Yeniden push, denetimler yeşil

Çalıştıkça yapılan, her birinde biraz yeni iş ve ne değiştiğini söyleyen bir mesaj olan
commit'ler; ders dışında, en az iki ayrı oturumda. Denetleyicinin istediklerinin hepsi
aşağıdadır.

---

## Teslim listesi

**Derste, 11:45'e kadar push**
- [ ] `week05/api.md` — en az iki giriş satırı (REQ-001); sizin yazdığınız, elle, 10:00'da push edilmiş
- [ ] `week05/DESIGN.md` — en az dört bileşen, her biri ne yaptığı ve hizmet ettiği REQ kimlikleriyle
- [ ] `server/` — `api.md` dosyasının her satırı için aynı metot ve yolla bir route; sunucu başlıyor ve `/docs` açılıyor
- [ ] `server/tests/test_login.py` — bir test case kimliğiyle adlandırılmış, çalıştırılmış ve doğru nedenle başarısız olan en az bir test

**Cumartesi 23:59'a kadar**
- [ ] `week05/api.md` — her route'un bir satırı var; bir gereksinime hizmet eden her endpoint için istek, cevap ve hatalar
- [ ] `server/tests/test_login.py` — `test_cases.json` içindeki test case kimlikleriyle adlandırılmış en az üç test
- [ ] `week05/DESIGN.md` — her işlevsel `must` gereksinime hizmet ediliyor; Mermaid ile mimari
- [ ] `requirements.json` ve `test_cases.json` — son değişiklikler yapıldı, her biri kendi Değişiklik günlüğü satırıyla: taban çizgisi
- [ ] `week05/ai_log_05.md` — çalıştırmadan önceki beklentiniz, komut ve çıktısı yapıştırılmış, değiştirilen ya da reddedilen bir satır; sizin yazdığınız, asistanın değil (asistana yazdırılan 0 alır)
- [ ] GitHub'da denetimler yeşil; 1–4. haftalar hala geçiyor

---

## Bu hafta yok

Henüz giriş yok: route'lar 501 ile cevap verir ve kod gönderilmez (6. hafta). E-posta yok, veritabanı yok,
web ya da mobil istemci yok (6. ve 7. haftalar). Grup çalışması ve katkı bonusu yok. Mağaza
adımı yok: S2 6. haftada.

---

## Bu hafta nasıl notlanır

**Dersin sonu — 5 puan.** Bileşenler, `api.md` dosyasının giriş satırları, her satır için bir
route ve ilk giriş testi; reponuzun dersin sonundaki
(11:45) halinden okunur.

**Cumartesi 23:59 — 5 puan.** Son halinizde denetimlerin yeşil olması: **2**. İnsan katılımı:
**2**; yani gerçek çıktısı yapıştırılmış, sizin yazdığınız `ai_log_05.md` (asistana yazdırılmış
günlük **0** alır) ve koddan önce elle yazdığınız giriş satırları.
Commit düzeni: **1**; yani üç kontrol noktasının her birinde (10:00, 11:00, 11:45; en fazla on
beş dakika farkla) yeni iş içeren bir push ve ders dışında, ayrı oturumlarda en az iki
commit.

**Bir öğrenci, bir bilgisayar, bir GitHub hesabı.** Kendi bilgisayarınızdan, kendi hesabınızla
commit edin. Bir arkadaşınızın bilgisayarında ya da onun oturumunda yapılan iş ders için puan
kazanmaz. Bir gün gerçekten başka bir bilgisayardan commit etmeniz gerekirse, bunu o haftanın
yapay zeka günlüğünde, günü ve nedeniyle birlikte söyleyin.
