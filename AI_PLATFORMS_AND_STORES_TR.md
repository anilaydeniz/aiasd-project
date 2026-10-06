# Platformlar ve Mağazalar: Ne Geliştirebilirsiniz, Nerede Yayınlayabilirsiniz

AI-Assisted Software Development · Atlas Üniversitesi · Güz 2026–2027

*Prof. Dr. Vedat Coşkun · English: [`AI_PLATFORMS_AND_STORES_EN.md`](AI_PLATFORMS_AND_STORES_EN.md)*

Projeniz bir **mobil uygulama, bir web istemcisi ve bir sunucu** olarak teslim edilir ve
mobil uygulama dönem sonuna kadar **public bir mağazadan yüklenmiş** olmalıdır. Bu el
kitabı, 2. Hafta'da her birinizin sorduğu sorunun yanıtlarını içermek üzere oluşturulmuştur: *elimdeki bilgisayar ve
telefonla ne geliştirebilirim ve hangi mağazaya gerçekten ulaşabilirim?* Teklifinizin §6
(teknoloji yığını) ve §12 (riskler) bölümlerini yazmadan önce bu dokümanı okumanız önemlidir.

Ücretler, süreler ve mağaza politikaları değişir. Bu el kitabındaki rakamlar yazıldığı
tarihte geçerli olanlardır; bir plana bağlanmadan önce mağazanın kendi sayfasına bakın.

# 1. Kurallar

- **En az bir public mağazada yayınlarsınız** ve hangisi olduğu sizin seçiminizdir: Google
  Play, Huawei AppGallery, Samsung Galaxy Store ya da Apple App Store. Bir mağaza yeter.
  Bu sınıftaki her bilgisayar + telefon kombinasyonu bunlardan en az birine ulaşabilir (§3).
- **Native Android, native iOS ya da hybrid: üçü de kabul edilir.** Native iOS, bir Mac ve
  Apple'ın yıllık üyeliğine ihtiyacınız olduğu anlamına gelir; native Android, yalnızca tek
  platforma hizmet ettiğiniz anlamına gelir; hybrid (çapraz platform bir çatıda yazılmış tek
  kod tabanı) tek kod tabanından iki platformu da verir. Teslim edebileceğinizi seçin ve
  §6'da gerekçelendirin.
- **Savunma, mağazadan yüklenmiş build'den yapılır**, o platformun bir telefonunda; bu
  telefon ya sizinkidir ya da salonda ödünç aldığınız bir telefondur. Bir mağazada
  yayınlıyorsanız ve kendi telefonunuz diğer platformsa, uygulamayı kendi telefonunuza da
  getirin; böylece sınav yapan ikisini de görür.
- **"Teslim edildi" sayılan tek şey mağaza yayınıdır.** Kendi telefonunuzdaki geliştirici
  build'i test etmek ve göstermek içindir; yayınlamak için değildir.

# 2. Native mi hybrid mi?

| | Native | Hybrid |
|---|---|---|
| Android | Kotlin + Jetpack Compose (Android Studio) | Flutter (Dart), React Native / Expo (TypeScript), Capacitor (web teknolojileri) |
| iOS | Swift + SwiftUI (Xcode, **yalnızca Mac**) | yukarıdakiyle aynı kod tabanı; iOS build'i için bir Mac ya da bulut build hizmeti (uygulamayı sizin için kendi Mac'lerinde derleyen bir şirket) gerekir |
| Kod tabanı | iki platform istiyorsanız iki | bir |
| Web istemcisi | ayrıca yazarsınız | Flutter ve Expo web için de derler; Capacitor zaten web istemcisidir |
| iOS tarafının maliyeti | bir Mac + Apple Developer üyeliği | aynı; hybrid, Apple'ın ücretini kaldırmaz |
| Ne zaman uygun | dili zaten biliyorsanız ya da tek platform hedefliyorsanız | tek kod tabanından iki platform istiyorsanız ya da Windows bilgisayarınız var ve iOS da istiyorsanız |

Uygulamanızın içindeki sohbet botu (6–7. Haftalar) *sizin sunucunuzla* konuşur; bu yüzden
hangi mobil çatıyı seçtiğiniz onu ilgilendirmez. Denetleyiciyi de ilgilendirmez. Teslim
edebileceğinizi seçin.

# 3. Bilgisayarınız + telefonunuz → yollarınız

Her satır, bu sınıftaki birinin sahip olduğu bir kurulumdur. **X**, o yolun o mağazaya
çıktığı anlamına gelir; boş hücre, ne yaparsanız yapın çıkmadığı anlamına gelir.

| Bilgisayar + telefon | Geliştirme | Google Play | AppGallery | Galaxy Store | App Store |
|---|---|:---:|:---:|:---:|:---:|
| **Mac + Android** | native Android (Kotlin) | X | X | X | |
| | native iOS (Swift) \*\* | | | | X |
| | hybrid | X | X | X | X |
| **Mac + iPhone** | native Android (Kotlin) \*\* | X | X | X | |
| | native iOS (Swift) | | | | X |
| | hybrid | X | X | X | X |
| **Windows + Android** | native Android (Kotlin) | X | X | X | |
| | native iOS (Swift) | | | | |
| | hybrid | X | X | X | X\* |
| **Windows + iPhone** | native Android (Kotlin) \*\* | X | X | X | |
| | native iOS (Swift) | | | | |
| | hybrid | X | X | X | X\* |

\*\* Telefonunuz diğer platformdur; bu yüzden emülatörde ya da simülatörde (bilgisayarınızda
telefon gibi davranan bir program) geliştirir ve test edersiniz.

\* Windows'tan iOS binary'si (derlenmiş uygulama dosyası) Expo EAS ya da Codemagic gibi
bir hizmet tarafından bulutta derlenir ve Apple üyeliği yine gerekir. Windows'tan native
iOS yoktur, çünkü Xcode yalnızca Mac'te çalışır. Her App Store hücresi ayrıca ≈ 99 $/yıl
üyeliği varsayar (§4).

Aynı tabloyu sütun sütun okuyun: **dört mağazanın üçü herkese açıktır**; her bilgisayar,
her telefon ve üç geliştirme yolunun herhangi biriyle. Sahip olduklarınıza bağlı olan tek
mağaza App Store'dur.

Tabloda saklı iki gerçek vardır:

- **Bir Android mağazasında yayınlamak için kendi Android telefonunuz gerekmez.**
  Android Studio'daki emülatör geliştirmek ve test etmek için yeter ve mağaza paketi her
  iki durumda da kabul eder. Bir istisna var: Google Play, yeni bir kişisel hesaptan bir
  kez, Play Console uygulamasıyla gerçek bir Android telefonda (Android 10 ya da sonrası;
  emülatör kabul edilmez) onay ister. Bir arkadaşınızın telefonunu bir dakikalığına ödünç
  almanız yeter.
- **Native iOS derlemek için Mac gerekir.** App Store isteyen Windows kullanıcıları, iOS
  binary'sini bulutta derleyen Expo EAS ya da Codemagic'ten geçer; ama Apple üyeliğini
  yine siz ödersiniz.

# 4. Mağazalar

| | Google Play | Huawei AppGallery | Samsung Galaxy Store | Apple App Store |
|---|---|---|---|---|
| Geliştirici ücreti | tek seferlik (≈ 25 $) | ücretsiz | ücretsiz | yıllık (≈ 99 $) |
| Kayıt | bir Google hesabı, kimlik doğrulama ve bir kez gerçek bir Android telefon | bir Huawei ID, kimlik belgesi ve birkaç günlük onay | bir Samsung hesabı ve satıcı onayı | bir Apple ID, kimlik doğrulama ve ödeme |
| Derleme | Mac ya da Windows | Mac ya da Windows | Mac ya da Windows | Mac (ya da bulut build) |
| Yayından önce | yeni bireysel hesaplar 14 gün boyunca 12 testçiyle kapalı test (yalnızca adı yazılı testçilere açık bir test) yapmak zorundadır | inceleme; birkaç gün sürer | inceleme; birkaç gün sürer | inceleme; genellikle günler sürer ve retle sonuçlanabilir |
| Bu sınıftaki erişim | neredeyse her Android telefon | Huawei telefonlar; diğer Android kullanıcıları AppGallery uygulamasını kurabilir | Samsung telefonlar; diğer Android kullanıcıları Galaxy Store'u kurabilir | her iPhone |
| Dikkat | yukarıdaki kapalı test kuralı: 12 testçiyi ve 14 günü 9. Hafta'ya planlayın, kuralı 10. Hafta'da keşfetmeyin | Google servislerine (Firebase, Google Maps, Google Sign-In) bağımlı uygulamalar Huawei telefonlarda çalışmaz ve reddedilebilir | — | tek ücretli yol ve Mac gerektiren tek yol |
| Toplam ödediğiniz | ≈ 25 $, bir kez | hiç | hiç | her yıl ≈ 99 $; öğrenci indirimi yok |

Bundan iki sonuç çıkar:

- **Google Play'in test kanalı kuralı, planlarsanız bir armağandır.** On dört gün boyunca
  on iki testçi, tam olarak sınıf arkadaşlarınızın testçi olduğu beta haftasıdır (9. Hafta)
  ve o testçiler sizin `contributors_09.json` dosyanızdır. Kuralı ilk kez 10. Hafta'da
  duyarsanız felakettir. Kural yalnızca yeni *bireysel* hesaplara uygulanır.
- **Google servislerine bağımlı olmayın.** Girişiniz *kendi* sunucunuzdan e-posta kodu ya
  da OTP ile yapılır; öyle kalsın, uygulamanız her mağazada çalışır. Harita ya da push
  bildirimi gerekiyorsa tek mağazaya bağlı olmayan bir sağlayıcı seçin.
