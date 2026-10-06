# AIASD — Dönem Bir Bakışta

**AI-Assisted Software Development · Atlas Üniversitesi · Güz 2026–2027 · Prof. Dr. Vedat Coşkun**

*English: [`AI_SKELETON_EN.md`](AI_SKELETON_EN.md)*

Bu belge, dönemin tamamını iki sayfada anlatır: her hafta ne öğretildiğini, sınıfta ne
yaptığınızı, Cumartesi'ye kadar neyi bitirdiğinizi ve deponuza ne geldiğini söyler. İlk
derste gösterilir ve deponuzda yaşar. Dönem içinde değişebilir ve her değişiklik, kendi
teklifinizdeki değişiklikleri kaydettiğiniz gibi, bu dosyanın sonunda kaydedilir.

## Her hafta geçerli olanlar

- **Tek bir projeyi, yalnız, dönem boyunca** yaparsınız. Proje bir mobil istemci, bir web
  istemcisi ve bir sunucudur; girişi e-posta kodu ve/veya OTP (tek kullanımlık şifre,
  yalnızca bir kez geçerli olan kısa bir kod) ile yapılır ve dönem sonunda **bir public
  mağazada yayınlanmış** olur. Hangi mağazayı kullandığınız ve uygulamanın native mi hybrid
  mi olduğu sizin seçiminizdir (`AI_PLATFORMS_AND_STORES_EN/TR.md`). 13–14. Haftalardaki
  savunma mağazadan yüklenmiş uygulamadan yapılır.
- **Projeniz kendisi hakkında bir sohbet botu içerir.** Onu 6–7. Haftalarda, kendi
  çalıştırdığınız açık ağırlıklı modellerle (gömme için BGE-M3, yani benzer parçaları bulmak
  için kullanılan sayısal metin gösterimleri; yanıt için Ollama üzerinden Qwen) kendi
  belgeleriniz ve verileriniz üzerinde kurarsınız ve iki istemciden de erişilebilir olur. Bu
  özellik için bulut model API'si kullanılamaz.
- **Haftada 10 puan** kazanırsınız: 5'i dersin sonunda, 5'i Cumartesi 23:59'da deponuzdan
  okunur. 1. Hafta 5 puandır ve tamamı Cumartesi okunur. Dönem notu şunlardan oluşur:
  haftalık projeler 60 · mağaza bonusu 15 · sunum (savunma, 13–14. Hafta) 15 · final
  sınavı 40.
- **3. Hafta'dan itibaren dört kişilik bir grupta çalışırsınız.** Grubu 3. Hafta dersinde
  kendiniz kurarsınız ve grup dönem boyunca birlikte kalır. Diğer üç üye
  `weekNN/contributors_NN.json` içindeki katkıcılarınızdır; 4. Hafta'dan itibaren dördünüz
  ayrıca her hafta bir saat çevrimiçi buluşursunuz. Onlar sizin notunuzdan bonus kazanır,
  siz onlarınkinden kazanırsınız. 2. Hafta'da katkıcı zorunlu değildir.
- **İnsan işini kanıtlarsınız**: sizinkini `weekNN/ai_log_NN.md` içinde kanıtlarsınız,
  yardımcılarınız kendilerininkini adlarının yanında kanıtlar. Cumartesi puanlarının ikisi bu
  kanıta bağlıdır.
- **`PROPOSAL.md` kökte yaşar** ve herhangi bir haftada değişebilir; yeter ki değişiklik
  günlüğüne tarihli bir satır ekleyin. Sessiz değişiklik puana mal olur; kaydedilmiş
  değişiklik mühendisliktir. **Projenin kendisi 3. Hafta dersinin sonunda (11:45) kesinleşir**: o andan sonra ayrıntıları değişebilir, problemi ve ürünü değişemez.
- **Yayınlama adım adım notlandırılır** (plandaki S0–S6 adımları), her adımın teslim
  haftasında. Mağazayla ilgili hiçbir şey son haftada yapılamaz.
- **Her diyagram Mermaid'dir** (metin tabanlı bir diyagram gösterimi) ve markdown dosyasının
  içinde yazılır. GitHub onu çizer, denetleyici onu okur.

Puanların nasıl hesaplandığı, denetleyicinin neye baktığı ve bonusun ayrıntıları
`AI_WEEKLY_WORKFLOW_STUDENT_TR.md` / `_EN.md` içindedir.

## Haftalık plan

### Her hafta ne olur

| Hafta | İçerik | Sınıfta | Ders sonrası | Notlar |
|---|---|---|---|---|
| 1 | Derse giriş; araçlar; Git; LLM'lerle (büyük dil modelleri) ilk temas | • Ödev adım adım anlatılır<br>• henüz bir şey yapılmaz | Araçları kur, şablondan private depoyu oluştur, Collaborator ekle, student.json'ı doldur, hello.py yaz ve iki LLM'i keşfet | • Hafta 5 puandır, tamamı Cumartesi okunur (3 otomatik · 1 commit · 1 AI günlüğü)<br>• Bu hafta katkıcı yok |
| 2 | Teklif Bölüm A + Gereksinimler (SRS, sistemin ne yapması gerektiğini listeleyen belge) | • Problemi ve çözümü yaz<br>• iki paydaşla görüş<br>• gereksinim listesine başla | • Teklif Bölüm A'yı bitir<br>• SRS'yi diyagramlarıyla yaz | • Teklif kökte yaşar ve onu herhangi bir haftada bir değişiklik günlüğü satırıyla revize edebilirsiniz<br>• Rol: stakeholder |
| 3 | Pitch, inceleme, Teklif Bölüm B | • Dört kişilik grubunu kur<br>• pitch'ini grupta sun; diğer üçü cevaplarını yazar<br>• Bölüm A'yı gözden geçir ve değişiklik günlüğünü başlat<br>• ana akışın ekranlarını yaz; proje dersin sonunda (11:45) kesinleşir | • Bölüm B'yi yaz: pazar, rakipler, karşılaştırma, ticari potansiyel, mağaza seçimiyle birlikte teknik riskler<br>• AI log: asistan düşman gözden geçiren olarak<br>• her kabul ölçütünü 4. Hafta için test edilebilir hâle getir | • S0: teklifin §12'si mağazayı, ücreti ve inceleme süresini adlandırır<br>• Cumartesiden itibaren bir gereksinim id'sinin anlamı değişmez; liste 5. Hafta sonundaki taban çizgisine kadar açık kalır<br>• Rol: gözden geçiren; grup dönem boyunca kalır |
| 4 | Tıklanabilir prototip ve test case'ler | • Ana akışı düz HTML ekranlarla kur<br>• her must gereksinim için bir test case yaz<br>• grup bunları prototip üzerinde yürütür (walk-through) | • Başarısız olanları düzelt; grup toplantısında ikinci tur<br>• gereksinimleri ve test case'leri güncelle<br>• ekran akışını tamamla<br>• geliştirici hesabını aç | • S1: dersin olduğu gün başvur, çünkü kimlik kontrolü günler sürer<br>• Rol: prototype-tester |
| 5 | Tasarım ve API sözleşmesi; geliştirme başlar | • Tasarımı yaz (bileşenler ve hizmet ettikleri REQ id'leri)<br>• sunucu iskeleti yerelde çalışır | • API sözleşmesini yaz (sunucunun her endpoint'i)<br>• e-posta kodu / OTP ile giriş uçtan uca çalışır<br>• TC id'leriyle adlandırılmış ilk otomatik testler | • Cumartesi gereksinimler ve test case'ler taban çizgin (baseline) olur; ondan sonra bir değişiklik bir değişiklik isteğiyle yapılır<br>• Rol: design-reviewer |
| 6 | Sohbet botu I — motor | • Ollama + Qwen çalışıyor<br>• projenin kendi belgeleri üzerinde BGE-M3 gömmeleri oluşturulmuş<br>• sunucudaki bir chat endpoint'i proje hakkında bir soruyu yanıtlar | • Getirmeyi ayarla (chunking, yani belgelerin parçalara nasıl bölündüğü; top-k, yani modele kaç parça verildiği)<br>• model notlarını yaz: hangi modelleri denediniz, neyi yanlış yaptılar<br>• mağazada uygulama kaydını oluştur | • S2: uygulama kaydı / bundle id (mağazanın uygulamanızı tanıdığı benzersiz ad)<br>• Rol: code-reviewer |
| 7 | Sohbet botu II — istemcilerde | Web istemcisindeki sohbet ekranı sunucuyla konuşur | • Mobil istemcide sohbet ekranını kur<br>• testleri yaz<br>• CI'ı kur (sürekli entegrasyon, her push'ta çalışan kontroller) | • İlk özellik üç katmanda da canlı<br>• Rol: chat-tester |
| 8 | Geliştirme — projenin kendi özelliği | Projenin çekirdek özelliği üç istemcide de çalışır | • Özelliği tamamla<br>• ilk build'i test kanalına yükle | • S3 mağazanın zorunlu test süresini başlatır<br>• Rol: test-user |
| 9 | Beta testi | • Testçileri kanala kaydet<br>• hata listesini aç | • Hataları düzelt<br>• test raporunu yaz | • Beta testçileri mağazanın testçileriyle aynı kişiler olmalıdır<br>• Rol: beta-tester |
| 10 | UAT (Kullanıcı Kabul Testi, gerçek kullanıcıların ürünü denediği bir oturum) + gönderim | UAT oturumunu katılımcılarla yürüt | • UAT raporunu yaz<br>• dağıtım diyagramını çiz<br>• uygulamayı incelemeye gönder | • S5, ret ve yeniden gönderim için bir hafta bırakır<br>• Rol: uat-participant |
| 11 | Yayın + sağlamlaştırma | • İnceleme düzeltmelerini uygula<br>• release-tester uygulamayı mağazadan yükler | • Canlıya çık<br>• son README'yi yaz | • S6: uygulama canlı<br>• Rol: release-tester |
| 12 | Kapanış | • Poster taslağı gözden geçirilir<br>• savunma provası | Son posteri bitir | • Savunmanın kendisi 13–14. Hafta'dadır ve mağaza kurulumundan yapılır<br>• Rol: poster-reviewer |

### Dosya akışı — öğrencinin aldığı ve push ettiği

Ödevler `_EN` ve `_TR` olarak gelir ve aşağıda bu ek atlanmıştır. Okumalar (`AI_DocN`) İngilizcedir. Ders sunumu depoda bir dosya değildir.

| Hafta | Verilen (`weekNN/` ya da köke gelir) | Ders sonuna kadar push (5) | Cumartesi'ye kadar push (5) |
|---|---|---|---|
| 1 | • `AI_Doc1`–`AI_Doc4` ön okuma (kök)<br>• `week01/ASSIGNMENT_01`<br>• iskeletler (başlıkları hazır, içeriği boş gelen dosyalar) `llm_notes.md`, `ai_log_01.md`<br>• kök: `student.json`, `README`, `AI_SETUP_CARD`, `AI_WEEKLY_WORKFLOW_STUDENT` | — | • `student.json`<br>• `week01/setup_proof.md`<br>• `hello.py`<br>• `llm_notes.md`<br>• `ai_log_01.md` (5 puanın tamamı) |
| 2 | • `week02/ASSIGNMENT_02`<br>• kök `PROPOSAL.md` iskeleti<br>• `week02/SRS.md` iskeleti<br>• `requirements.json` iskeleti<br>• `contributors_02.json`<br>• `ai_log_02.md`<br>| • `PROPOSAL.md` §1–§4<br>• `week02/requirements.json` ilk liste<br>• `contributors_02.json` | • `PROPOSAL.md` §5–§7<br>• `week02/SRS.md` + diyagramlar<br>• `requirements.json` son hâli<br>• `ai_log_02.md` |
| 3 | • `week03/ASSIGNMENT_03`<br>• `PITCH_03.md`<br>• `group_03.json`<br>• `contributors_03.json`<br>• `screens_03.md`<br>• `ai_log_03.md`<br>• kökte `AI_Doc5` | • `PITCH_03.md` (dersten önce)<br>• `group_03.json` (her üye için aynı liste)<br>• `contributors_03.json` (üç gözden geçiren)<br>• gözden geçirilmiş `PROPOSAL.md` Bölüm A + değişiklik günlüğü<br>• `screens_03.md` (ana akış) | • `PROPOSAL.md` §8–§12<br>• güncel `requirements.json`<br>• `ai_log_03.md` |
| 4 | • `week04/ASSIGNMENT_04`<br>• üç başlangıç ekranıyla `prototype/`<br>• `test_cases.json`, `walkthrough_04.json` ve `store.json` iskeletleri<br>• `contributors_04.json`<br>• `ai_log_04.md` | • `week04/prototype/` (en az beş ekran)<br>• `test_cases.json` (her must)<br>• `walkthrough_04.json` (birinci tur)<br>• `contributors_04.json` | • tam ekran akışı (en az yedi ekran)<br>• ikinci tur; güncellenmiş `requirements.json` ve `test_cases.json`<br>• `week04/store.json` S1<br>• `ai_log_04.md` |
| 5 | • `week05/ASSIGNMENT_05`<br>• `DESIGN.md` ve `api.md` iskeletleri<br>• `contributors_05.json`<br>• `ai_log_05.md` | • `week05/DESIGN.md`, ilk sürüm<br>• sunucu iskeleti<br>• `contributors_05.json` | • `week05/api.md`<br>• çalışan giriş<br>• TC id'siyle adlandırılmış ilk testler<br>• `ai_log_05.md` |
| 6 | • `week06/ASSIGNMENT_06`<br>• `week06/requirements.txt` (Ollama istemcisi, sentence-transformers)<br>• `embedder.py`/`chat` iskeletleri<br>• `model_notes.md` iskeleti<br>• `contributors_06.json`<br>• `ai_log_06.md` | • `embedder.py`<br>• bir soruyu yanıtlayan `chat` endpoint'i<br>• `contributors_06.json` | • tüm proje belgeleri üzerinde çalışan getirme<br>• `week06/model_notes.md`<br>• `store.json` S2<br>• `ai_log_06.md` |
| 7 | • `week07/ASSIGNMENT_07`<br>• test + CI iskeleti<br>• `contributors_07.json`<br>• `ai_log_07.md` | • web istemcisinde sohbet ekranı<br>• `contributors_07.json` | • mobil istemcide sohbet ekranı<br>• testler + CI yeşil<br>• `ai_log_07.md` |
| 8 | • `week08/ASSIGNMENT_08`<br>• `contributors_08.json`<br>• `ai_log_08.md` | • çekirdek özellik üç istemcide<br>• `contributors_08.json` | • tamamlanmış özellik<br>• `store.json` S3 (ilk build, kanal)<br>• `ai_log_08.md` |
| 9 | • `week09/ASSIGNMENT_09`<br>• test raporu iskeleti<br>• `contributors_09.json`<br>• `ai_log_09.md` | • kayıtlı testçiler (= `contributors_09.json`)<br>• hata listesi | • düzeltmeler<br>• test raporu<br>• `store.json` S4<br>• `ai_log_09.md` |
| 10 | • `week10/ASSIGNMENT_10`<br>• UAT raporu iskeleti<br>• `contributors_10.json`<br>• `ai_log_10.md` | • UAT bulguları<br>• `contributors_10.json` | • UAT raporu<br>• dağıtım diyagramı<br>• `store.json` S5<br>• `ai_log_10.md` |
| 11 | • `week11/ASSIGNMENT_11`<br>• son README iskeleti<br>• `contributors_11.json`<br>• `ai_log_11.md` | • inceleme düzeltmeleri<br>• `contributors_11.json` | • `store.json` S6 (mağaza URL'si + web URL'si)<br>• son README<br>• `ai_log_11.md` |
| 12 | • `week12/ASSIGNMENT_12`<br>• poster şartnamesi<br>• `contributors_12.json`<br>• `ai_log_12.md` | • poster taslağı<br>• `contributors_12.json` | • son poster<br>• `ai_log_12.md`<br>• mağaza kurulumundan savunma |

## Değişiklik günlüğü

- 21 Eyl 2026 — v2, gösterilen ilk sürüm.
- 26 Eyl 2026 — dönem notu syllabus'a göre (60 · 15 · 15 · 40, final sınavı); savunma 13–14. Hafta'ya taşındı.
- 26 Eyl 2026 — mağaza seçimi öğrencinin (dört mağazadan biri; native ya da hybrid), kökte Platforms and Stores el kitabı (`AI_PLATFORMS_AND_STORES_EN/TR.md`); 1. Hafta okumaları kökte `AI_Doc1–4`; `GRADING.md` atfı yerine öğrenci iş akışı.
- 4 Eki 2026 — 3. Hafta satırı ve katkıcı kuralı güncellendi (pitch, dörtlü gruplar, gereksinim id'leri kalıcı, taban çizgisi 5. Hafta sonunda).
- 4 Eki 2026 — 4. ve 5. haftalar yeniden yazıldı: 4. Hafta, kabul ölçütlerinden yazılan ve grubun yürüttüğü test case'lerle tıklanabilir prototiptir; 5. Hafta tasarım, API sözleşmesi, sunucu iskeleti ve giriştir, sonunda gereksinimler ve test case'ler taban çizgisi olur. `store.json` dosyası `week04/` içinde durur.
- 5 Eki 2026 — 3. Hafta: proje dersin sonunda (11:45) kesinleşir (ayrıntılar değişiklik günlüğüne bir satırla değişmeye devam edebilir); ana akışın ekranları derste `week03/screens_03.md` dosyasına yazılır; geliştirici hesabı (S1) 3. haftada da açılabilir; her üye aynı grup listesini `week03/group_03.json` dosyasına yazar.
