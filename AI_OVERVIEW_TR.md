# Projeye genel bakış (overview): parçaları, nasıl uyuşmaları gerektiği ve birlikte ne değişir

*English: [`AI_OVERVIEW_EN.md`](AI_OVERVIEW_EN.md)*

Projeniz tek bir dosya değil. Birkaç parçadan oluşur ve hepsi aynı gereksinimlerden (requirements) söz
eder. Bundan sonra her hafta yeni parçalar eklenir; eski parçalar da doğru kalmalıdır. Bu sayfa parçaları
listeler, nasıl uyuşmaları gerektiğini ve birini değiştirdiğinizde başka neyi değiştirmeniz gerektiğini
söyler.

## 1. Parçalar

| # | Parça | Dosya | İçinde ne var |
|---|---|---|---|
| 1 | Teklif (proposal) | `week02/PROPOSAL.md` | problem, ürün, teknolojiler, başarı ölçütleri (success criteria), pazar (market), riskler (risks), mağazanız (§12); sonunda **Change log** (değişiklik günlüğü) |
| 2 | Gereksinimler (requirements) | `week02/requirements.json` | her gereksinim: id, açıklama (`description`), işlevsel mi (`functional`), öncelik (`priority`), kabul ölçütü (`acceptance`) |
| 3 | Kullanım senaryoları (use cases) | `week02/SRS.md` | aktörler (actors); her kullanım senaryosu ve hizmet ettiği gereksinimler; kullanım senaryosu diyagramı (use case diagram) |
| 4 | Ekranlar (screens) | `week03/screens_03.md`, `week04/prototype/` | ana akışın (main flow) ekranları; her ekran gereksinimlerini anar (`<!-- serves: REQ-… -->`) |
| 5 | Test case'ler | `week04/test_cases.json` | her kabul ölçütü (acceptance criterion), adımlar (`steps`) ve beklenen sonuç (`expected`) olarak, `"run"` ile (server, web ya da manual) |
| 6 | Tasarım (design) | `week05/DESIGN.md` | bileşenler (components) ve her birinin hizmet ettiği gereksinimler; Mermaid ile mimari (architecture) |
| 7 | API sözleşmesi (API contract) | `week05/api.md` | istemci (client) ile sunucu (server) arasındaki her istek; sütunlar: Method, Path, Request (istek), Response (cevap), Errors (hatalar), REQ |
| 8 | Sunucu (server) | `server/`, `server/tests/` | `api.md`'nin route'ları; test case id'siyle adlandırılmış testler (`test_TC_002_02_…`) |
| 9 | Web istemcisi (web client) | `web/` | prototipin ekranları, artık sunucuyu çağıran gerçek sayfalar (`serves: REQ-…`) |
| 10 | Mağaza yolu (store path) | `week04/store.json` | mağazanız (store) ve S1–S6 adımları |

Sonraki parçalar da aynı zincire (chain) katılır: 7. haftada mobil istemci (mobile client), 8. haftada
sohbet botu (chatbot), 9.–10. haftalarda test raporu (test report) ve UAT raporu (UAT report).

## 2. Parçalar nasıl uyuşmalı

- **Kaynak (source) `requirements.json` dosyasıdır.** Diğer her parça onu izler. Bir gereksinimi asla
  yalnızca koda uysun diye değiştirmeyin.
- **Her yerde bir id, bir anlam.** REQ-004 her dosyada aynı şeyi anlatır. TC-004-02, REQ-004'ü test eder
  ve `"req"` alanı bunu söyler. Düşürülen bir gereksinim (dropped requirement) id'sini korur ve
  `"dropped": true` alır; ondan sonra başka hiçbir parça onu kullanmaz.
- **Aynı bilgiler, aynı sayılar.** REQ-002 "30 ile 120 dakika" diyorsa UC2, rezervasyon ekranı,
  TC-002-02, `api.md`'deki 422, route ve testi de 30 ile 120 der. Öncelik de yazıldığı her yerde aynıdır.
- **Her işlevsel (functional) `must` gereksinimin zinciri tamdır:** kullanım senaryosu → ekran → test
  case → `api.md` satırları → route → test → sayfa (7. haftadan itibaren telefon da). Bu, 6. hafta
  ödevindeki zincirdir.
- **Kopya yok.** SRS §4 ve §5'te tek satır durur: "The requirements are in `week02/requirements.json`."
- **REQ-001 dersin girişidir (course login).** REQ-001 ve TC-001 test case'leri tam olarak şunu söyler:
  4 haneli kod, 10 dakika geçerli, bir kez kullanılır; yeni kod ancak 60 saniye sonra; arka arkaya 3 yanlış
  kod adresi 15 dakika kilitler; şifre yok.
- **Kod, belgelerin söylediğini yapar.** Route `api.md`'yi izler; test, test case'inin beklediğini
  kontrol eder.
- **Tek mağaza.** `store.json`'daki mağaza, PROPOSAL §12'dekiyle aynıdır.

## 3. Bir parçayı değiştirdiğinizde onunla ne değişir

Önce belgeyi, sonra kodu değiştirin. Nasıl kaydedilir:

- `requirements.json` ya da `test_cases.json` → bir **change request** (değişiklik talebi): `CR-` ve
  sıradaki numarayla başlayan, id'leri anan ve etkilediği her dosyayı listeleyen bir Change log satırı.
- başka bir belge (`SRS.md`, ekranlar, `DESIGN.md`, `api.md`, `store.json`) → **tarihli bir Change log
  satırı** (dated line).
- kod → yalnızca commit.

| Şunu değiştirirseniz … | şunları da kontrol edip değiştirin … | Kayıt |
|---|---|---|
| bir gereksinim (anlamı, bir sayı, önceliği) | kullanım senaryosu, ekranlar ve sayfalar, test case'ler, `api.md` satırları, `DESIGN.md` bileşeni, route'lar, testler | CR |
| bir gereksinimi düşürmek (drop) | test case'lerini de düşürün; kullanım senaryolarından, ekranlardan, `api.md`'den, `DESIGN.md`'den ve koddan çıkarın | CR |
| yeni bir gereksinim | sıradaki boş id; sonra kullanım senaryosu, ekran, test case'ler ve işlevsel bir `must` ise zincirin geri kalanı | CR |
| bir test case: adımlar, beklenen sonuç | id'siyle adlandırılmış test | CR |
| bir `api.md` satırı: path, gövde (body), durum kodu (status code) | route, testleri, onu çağıran sayfalar (sonra telefon da) | tarihli satır |
| bir kullanım senaryosu ya da ekran | `web/` içindeki sayfası; yeni bir davranış eklerse önce bir gereksinim (CR) | tarihli satır |
| `DESIGN.md`'de bir bileşen | yaptıkları değişirse `api.md` ve `server/` | tarihli satır |
| mağaza | `store.json` ve PROPOSAL §12 | tarihli satır |

Örnek: *2026-10-28 — CR-01: REQ-002 artık 15 dakikalık slotlara izin veriyor; etkilenenler:
requirements.json, test_cases.json (TC-002-02), week05/api.md, server/bookings.py.*

Bir test case'e eksik `"run"` alanını eklemek change request değildir.

Her push'tan önce kendinize sorun: biri yalnızca bu parçayı okusa, diğerleriyle aynı şeyi mi söylüyor?
