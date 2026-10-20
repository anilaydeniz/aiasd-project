# AIASD · 5. Hafta — Tasarım, API Sözleşmesi ve Sunucu İskeleti

*Atlas Üniversitesi · 2026–27 Güz · Prof. Dr. Vedat Coşkun*
*Bu sayfadan sunulur. Her seferinde bir bölüm kaydırın; her `---` bir slayttır.*

<!-- Eğitmen: tarayıcıyı %150'ye yakınlaştırın ve GitHub başlığını kapatın. Toplam ≈ 2 sa 45 dk:
20 dk anlatım + kısa bir FastAPI gösterimi · 10:00'a kadar bileşenler ve api.md'nin giriş satırları, elle
(push) · 11:00'e kadar route'lar (push) · ilk giriş testi, denetleyici ve 11:45'teki son push ·
hemen ardından dondurma. -->

---

## Bugün

1. Projeniz şimdiye kadar ve sözleşme neden koddan önce gelir
2. Tasarım: ürününüzün bileşenleri, `week05/DESIGN.md`
3. API sözleşmesi: `week05/api.md` dosyasının giriş satırları, **elle**, 10:00'da push
4. On dakikada FastAPI ve `server/` içindeki sunucu iskeleti, 11:00'de push
5. Önce testler: test case kimliğiyle adlandırılmış ilk giriş testi, 11:45'te push
6. Cumartesi'ye kadar: sözleşmenin tamamı, üç test, mimari, taban çizgisi, AI log
7. Haftanın notlandırılması

---

## Projeniz şimdiye kadar ve nereye gidiyor

Bir ay önce projeniz yalnızca aklınızdaki bir fikirdi.

- **1. hafta:** araçlarınız ve yapay zeka asistanlarıyla ilk gerçek konuşmalarınız
- **2. hafta:** gerçek bir problem, onu yaşayan gerçek insanlar, ilk gereksinimler
- **3. hafta:** pitch ve pazar; proje artık kalıcı olarak sizin
- **4. hafta:** ekranlar ve onlara tıklayan bir sınıf arkadaşı
- **Bu hafta proje yazılıma dönüşüyor:** bir iskelet, bir sözleşme, size ilk kez cevap veren bir sunucu
- **Sonra:** e-posta kutunuza gelen kodla giriş (6) · aynı giriş telefonda (7) · ürününüzün kendi özelliği her yerde (8) · gerçek testçiler, mağaza ve Aralık'ta bir mağazadan kurulan uygulamanız

Cumartesi gereksinimleriniz ve test case'leriniz **taban çizginiz (baseline)** olur.

<!-- Eğitmen: bunu bir liste gibi değil, bir hikaye gibi anlatın: her biri dört haftada ne kurdu. İki üç öğrenciye ürünlerinin şu an ne yaptığını sorun. -->

---

## Bu hafta: geri kalan her şeyin üzerine kurulduğu parça

- **Tasarım:** ürününüzün parçaları ve her parçanın hizmet ettiği gereksinim
- **API sözleşmesi:** sunucunuzun istemcilerine verdiği söz
- **Sunucu iskeleti:** her endpoint'e, şimdilik "henüz yapılmadı" diyerek cevap veren gerçek bir sunucu
- **İlk testler:** giriş test case'leriniz kod olarak, girişi bekliyor

Girişi 6. hafta, bugünkü endpoint'lerin arkasına kurarsınız ve web istemcisi onları çağırır. Mobil istemci 7. haftada aynılarını, hiç değiştirmeden çağırır. 8. hafta aynı sözleşmeye satır ekler.

**Sözleşmedeki bir hata bugün bulunursa bir satıra mal olur. 8. haftada bulunursa sunucuya ve iki istemciye.**

---

## Bu hafta asistan nerede yardım eder

| Parça | Asistan |
|---|---|
| Bir route'un FastAPI kodu (`api.md` satırı isteme yapıştırılır; bir route, bir commit) | **Yardım eder** |
| Test case'lerinizden birinden bir testin kodu (test case'le karşılaştırmak sizin işiniz) | **Yardım eder**, onay sizde |
| Gereksinimlerinizden bir bileşen önerisi | **Yardım eder**, karar sizde |
| Mimarinizin Mermaid sözdizimi | **Yardım eder** |
| Bir hata mesajını açıklamak | **Yardım eder** |

---

## … ve nerede hiç yardım etmez

| Parça | Asistan |
|---|---|
| `api.md` dosyasının giriş satırları: metot, yol, istek, cevap, hatalar | **Yardım yok**: herhangi bir koddan önce siz yazarsınız |
| Testleri ve sunucuyu çalıştırmak ve ekrana yazdıklarını okumak | **Yardım yok**: kendiniz çalıştırırsınız |
| Değişiklik günlüğü satırları ve Pazar'dan itibaren değişiklik istekleri | **Yardım yok** |
| `ai_log_05.md` (Evidence bloğu ve kalın alıntılar dışında) | **Yardım yok** |

<!-- Eğitmen: "Yardım yok" satırlarını yüksek sesle okuyun. Yeni olan ilk satırdır: giriş satırları, herhangi bir koddan önce elle yazılır. -->

---

<h1 align="center">api.md DOSYASININ GİRİŞ SATIRLARINI<br>ELLE YAZARSINIZ.</h1>

<h1 align="center">HERHANGİ BİR KODDAN ÖNCE.</h1>

<p align="center"><b>İstemcinin ne gönderdiği. Ne geri döndüğü. Başarısız olabileceği her yol.<br>Hiçbir asistan onları yazmaz, düzeltmez ya da tamamlamaz.</b></p>

<p align="center">Sunucunuzun route'ları henüz yokken, 10:00'daki push'unuzdan okunurlar.</p>

---

<h1 align="center">AI LOG'U<br>İNSAN YAZAR.</h1>

<p align="center"><b>Evidence bloğunun ve kalın alıntıların dışında asistan yok.<br>Ne yazmak için, ne düzeltmek için, dil için bile.</b></p>

<h1 align="center">Asistana yazdırılmış bir günlük 0 alır.</h1>

---

## Bu hafta tek başınıza çalışırsınız

- Collaborator yok, `group_05.json` yok, katkı bonusu yok. Grubunuz 6. haftadan itibaren yeniden toplanır.
- **Bir öğrenci, bir bilgisayar, bir GitHub hesabı.** Kendi bilgisayarınızdan, kendi hesabınızla commit edin.
- Bir gün gerçekten başka bir bilgisayardan commit etmeniz gerekirse, bunu o haftanın AI log'unda, günü ve nedeniyle birlikte söyleyin.

---

## Sözleşme neden koddan önce

Web istemciniz (6. hafta) ve mobil istemciniz (7. hafta) API sözleşmesine göre yazılır.

**Koddan sonra yazılırsa**, sözleşme yalnızca asistanın o an ne yazdıysa onu anlatır ve test case'leriniz artık gereksinimlerinizi test etmez.

**Önce yazılırsa**, sunucunun, iki istemcinin ve her testin üzerinde anlaştığı tek sayfa olur.

---

## Tasarım — `week05/DESIGN.md`

**Bileşen**, sisteminizin tek bir işi olan bir parçasıdır. **Derste: en az dört.**

| Bileşen | Ne yapar | REQ |
|---|---|---|
| Sunucu: giriş | Bir e-posta adresine 4 haneli bir kod gönderir, kodu kontrol eder ve bir token verir | REQ-001 |
| Sunucu: rezervasyonlar | 30 ile 120 dakika arası boş bir dilim için rezervasyonu kaydeder, dolu bir dilimi reddeder | REQ-002, REQ-003 |
| Veritabanı | Kullanıcıları, odaları ve rezervasyonları tutar | REQ-002, REQ-004 |
| Web istemcisi | Prototipin ekranları, tarayıcıda, 390 px genişlikte | REQ-006 |
| Mobil istemci | Aynı ekranlar bir telefonda | REQ-006 |

---

## Bileşenler: kurallar

- Her bileşene, kodunuzda vereceğiniz adı verin: "Sunucu: rezervasyonlar" `server/bookings.py` olur.
- Ne yaptığına dair tek cümle. Üç kez "ve" diyorsanız, bunlar iki bileşendir.
- REQ kimlikleri `requirements.json` içinde bulunur. Hiçbir gereksinime hizmet etmeyen bir bileşenin var olmak için bir nedeni olmalıdır.
- Asistan önerebilir; **karar sizindir**.

ZAYIF: `| Backend | Her şeyi yapar | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005 |`

---

## Endpoint'ler, istekler, cevaplar

**Endpoint**, sunucunuzun cevap verdiği tek bir şeydir: bir metot ve bir yol, `POST /auth/code`.

| Kod | Anlamı |
|---|---|
| 200 / 201 | Çalıştı / yeni bir şey oluşturuldu |
| 401 | Giriş yapılmamış ya da kod veya token yanlış |
| 404 | Böyle bir şey yok |
| 409 | Var olanla çakışıyor (dolu bir dilim) |
| 422 | Bir alan eksik ya da biçimi yanlış |
| 429 | Çok fazla istek: bekleyin |
| 501 | Henüz yapılmadı |

---

## Giriş: en az iki endpoint

Her projede giriş aynı şekilde yapılır (REQ-001). **İkinci satır, yani kodla giriş, sizindir.** Kod doğru mu? Yanlış mı? Çok mu eski? TC-001-01 ve TC-001-02 test case'leriniz size söyler.

| Metot | Yol | İstek | Cevap | Hatalar | REQ |
|---|---|---|---|---|---|
| POST | /auth/code | {"email": "deniz@example.com"} | 200 {"sent": true} | 422 e-posta değil · 429 bir dakika içinde yeniden istendi | REQ-001 |
| ? | ? | ? | ? | ? | REQ-001 |

---

## Şimdi — 10:00'a kadar

1. `week05/DESIGN.md`: en az dört bileşen.
2. `week05/api.md`: giriş satırları, **elle**, REQ-001'den ve test case'lerinizden.
3. Denetleyici, commit, **10:00'da push**.

<!-- Saati başlatın. Sıraların arasında dolaşın ve ekrandaki api.md satırlarına bakın: satırlar yazılırken hiçbir asistan penceresi açık olmasın. -->

---

## On dakikada FastAPI

```python
from fastapi import FastAPI

app = FastAPI(title="StudyRoom")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
```

```bash
uvicorn server.main:app --reload
```

http://127.0.0.1:8000/docs adresini açın. Asistan ne derse desin, **orada olmayan bir route yoktur**.

`week05/FASTAPI_CARD_TR.md`: aynısı, tek sayfada.

<!-- Gösterim: başlangıç sunucusunu çalıştırın, /docs'u açın, /health üzerinde "Try it out" deyin, sonra aşağıdaki /auth/code route'unu canlı ekleyin ve --reload ile /docs'ta belirdiğini gösterin. -->

---

## Sunucu iskeleti — her satır için bir route

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

İşi daha sonra yapılacak bir route, kendi haftası gelene kadar **501** ile cevap verir.

---

## İskelet: kurallar

- **`api.md` dosyasının her satırının bir route'u, her route'un da bir satırı vardır**: aynı metot, aynı yol. Denetleyici ikisini iki yönde de karşılaştırır.
- Route'lar `server/main.py` içinde, ya da `APIRouter` ile `server/` içindeki başka dosyalarda bulunur.
- Her route'un ilk satırı gereksinimini söyler.
- **Bir route, bir commit.** `api.md` satırı isteme yapıştırılır; cevabın tamamını okuyun; istemediğinizi reddedin.

Asistan "yardım edecektir": kodu her zaman 1234 olan tamamlanmış bir giriş, bir şifre alanı, planlamadığınız bir veritabanı. **Bu hafta route'lar yalnızca 501 ile cevap verir.**

---

## Şimdi — 11:00'e kadar

1. `api.md` dosyasının her satırı için `server/` içinde 501 ile cevap veren bir route.
2. `/docs` her satırı gösterir.
3. Denetleyici, commit, **11:00'de push**.

---

## Önce testler

Test, koda dönüştürülmüş bir test case'tir. Adı test case kimliğiyle başlar.

```python
from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)


def test_TC_001_01_a_code_is_sent_to_a_valid_email():
    response = client.post("/auth/code", json={"email": "deniz@example.com"})
    assert response.status_code == 200
    assert response.json() == {"sent": True}
```

```bash
python -m pytest
```

---

## Kırmızı, doğru nedenle

Bugün test **başarısız olur**. Olmalıdır: giriş 6. haftada yapılır.

| Hata ne diyor | Anlamı |
|---|---|
| `assert 501 == 200` | **Doğru neden**: route var, işi yok |
| `assert 404 == 200` | Route eksik ya da yolu `api.md`'dekinden farklı |
| `ImportError` | Test sunucunuzu bulamıyor |

Yanlış nedenle başarısız olan bir test hiçbir şeyi test etmez. **Kod var olmadan önce geçen bir test de hiçbir şeyi test etmez.**

Başarısız bir testi beklenen değeri değiştirerek "düzelten" bir asistan, testi işe yaramaz hale getirmiştir.

---

## Şimdi — 11:45'e kadar

1. `server/tests/test_login.py`: test case kimliğiyle adlandırılmış en az bir test.
2. Çalıştırın. Neden başarısız olduğunu okuyun.
3. Denetleyici, commit, **11:45'te push**.

---

## Bu haftadan itibaren commit düzeni

**Derste:** her kontrol noktasında, **10:00, 11:00 ve 11:45**'te, her birinden en fazla on beş dakika farkla, yeni iş içeren bir push.

**Ders dışında:** ayrı oturumlarda, yeni iş içeren en az iki commit.

Sonda tek bir commit puan getirmez.

---

## Cumartesi 23:59'a kadar

- `api.md`: her route'un bir satırı var; istek, 2xx koduyla cevap ve 4xx koduyla her hata.
- **En az üç giriş testi**, her biri `test_cases.json` içindeki bir test case kimliğiyle adlandırılmış. 6. haftaya kadar doğru nedenle başarısız olurlar. Onları herhangi bir giriş kodundan önce commit edin.
- `DESIGN.md`: her işlevsel `must` gereksinime hizmet ediliyor; **Mermaid diyagramı olarak mimari**.
- `ai_log_05.md`: çalıştırarak doğrulama.
- `requirements.json` ve `test_cases.json` dosyalarındaki son değişiklikler: **taban çizgisi**.

---

## Taban çizgisi ve değişiklik istekleri

**Cumartesi 23:59:** `requirements.json` ve `test_cases.json` taban çizginiz olur.

**Pazar'dan itibaren**, ikisinden birindeki bir değişiklik bir **değişiklik isteğidir** (change request): `CR-` ve bir numarayla başlayan ve etkilediği her dosyayı sayan bir Değişiklik günlüğü satırı.

> 2026-10-28 — CR-01: REQ-004 artık 15 dakikalık dilimlere izin veriyor; etkilenenler: requirements.json, test_cases.json (TC-004-02), week05/api.md, server/bookings.py.

Henüz var olmayan bir test case'e mi ihtiyacınız var? Cumartesi'den **önce** ekleyin.

---

## AI log — çalıştırarak doğrulama

Asistanın yazdığı bir route ya da bir test seçin.

1. **Çalıştırmadan önce**, ne beklediğinizi test case kimliğiyle yazın.
2. Kendiniz çalıştırın: `python -m pytest`, ya da sunucu ve `/docs`.
3. Komutu ve çıktısını, testleri sayan satıra kadar, `TERMINAL:` altına yapıştırın.
4. Asistanın kodundan değiştirdiğiniz ya da reddettiğiniz bir satır ve nedeni.

Sizin sözleriniz düz, asistanın sözleri kalın. **Asistana yazdırılmış bir günlük 0 alır.**

---

## 5. haftanın notlandırılması — 10 puan

| | Puan | Ne |
|---|---|---|
| Dersin sonu (11:45) | 5 | bileşenler, `api.md` dosyasının giriş satırları, her satır için bir route, ilk giriş testi |
| Cumartesi denetleyicisi | 2 | sözleşmenin tamamı, üç test, tamamlanmış tasarım, AI log |
| İnsan katılımı | 2 | gerçek çıktıyla, sizin yazdığınız AI log; koddan önce elle yazılmış giriş satırları |
| Commit düzeni | 1 | her kontrol noktasında bir push (10:00, 11:00, 11:45); ders dışında, ayrı oturumlarda iki commit |

Bu hafta katkı bonusu yok.

---

## Gelecek hafta: giriş çalışır

**6. hafta:** e-posta koduyla giriş, uçtan uca. Derste kod bir dosyaya yazılır; **Cumartesi'ye kadar gerçek e-postayla gelir**. Web istemcisi giriş ekranını alır. 5. haftanın testleri tek tek yeşile döner. S2: mağazanızda uygulama kaydı.

**6. haftadan önce:** sunucunun e-posta gönderebileceği bir hesap. Gmail için: iki adımlı doğrulama açık, sonra bir uygulama şifresi. Asla repoya değil: `.env` dosyasına girer.

<!-- Eğitmen: "Cumartesi 23:59'a kadar" slaytından itibaren olanlar, 11:45'teki push'tan önceki son on beş dakika içindir. 11:45'ten hemen sonra dondurun. -->
