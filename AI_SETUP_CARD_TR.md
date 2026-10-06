# Kurulum Kartı — her şey tek sayfada

**AI-Assisted Software Development · Atlas Üniversitesi · Güz 2026–2027**

Bu sayfayı açık tutun. Dönemin tamamı boyunca çalıştırmanız gereken her şey bu
sayfadadır.

---

## Bir kez, 1. Hafta'dan önce

**1 · Deponuzu oluşturun.** Ders şablonunda (GitHub'ın sizin için kopyaladığı hazır bir
depo) **Use this template → Create a new repository** düğmesine tıklayın. Adını
`aiasd-project` koyun. **Private** yapın, çünkü form Public seçili açılır. Sonra
**Settings → Collaborators → Add people** bölümüne gidin ve `VedatCOSKUN` ekleyin.

**2 · Bilgisayarınızın GitHub ile konuşmasını sağlayın.** Şifreler 2021'de bu amaç için
çalışmaz oldu. Bu adımı bir kez yapın; bir daha yapmanız gerekmez:

```bash
brew install gh          # Windows: winget install GitHub.cli
gh auth login
```

Soruları şu sırayla yanıtlayın: `GitHub.com` → `HTTPS` → `Y` → `Login with a web browser`.

*Bilgisayarınıza yazılım kuramıyor musunuz?* O zaman bunun yerine token kullanın (token,
şifrenizin yerine geçen uzun ve rastgele bir dizedir). **Settings → Developer settings →
Personal access tokens → Tokens (classic) → Generate new token (classic)** yolunu izleyin,
yalnızca bir kutuyu, yani **`repo`** kutusunu işaretleyin ve token'ı kopyalayın. git şifre
sorduğunda token'ı yapıştırın. Ona tüm hesabınızın şifresi gibi davranın: asla bir
dosyaya, bir sohbete ya da bir commit'e koymayın.

**3 · Bilgisayarınıza kopyalayın.**

```bash
git clone https://github.com/<kullanıcı-adınız>/aiasd-project.git
cd aiasd-project
```

**4 · Kim olduğunuzu söyleyin ve push edin.** `student.json` dosyasını açın ve beş alanın
tamamını doldurun. `section` alanı `en` ya da `tr` olur. Sonra şunu çalıştırın:

```bash
git add student.json
git commit -m "week01: student identity"
git push
```

**Bu push çalışıyorsa işiniz bitti.** Bu push, testin tamamıdır.

---

## Her hafta, aynı dört komut

```bash
python .github/check_deliverables.py

git add .
git commit -m "week01: what I did"
git push
```

On iki hafta boyunca başka hiçbir şey değişmez. Yalnızca commit mesajı değişir.
Denetleyiciyi (haftanın gerektirdiği dosyaları arayan ilk komutu) istediğiniz kadar
çalıştırın. Bir not değil, yapılacaklar listesidir ve çalıştırmanın bir maliyeti yoktur.

Bir hafta gerektirdiğinde iki komut daha çalıştırırsınız:

```bash
pip install -r weekNN/requirements.txt
streamlit run app.py
```

---

## Ders dosyaları kendiliğinden gelir

`python .github/check_deliverables.py` her çalıştığında dersin dosyalarını da reponuza
getirir. Bir hafta yayınlandığında o haftanın klasörünü getirir ve kökte değişen her
ders belgesini (`AI_*`) getirir. Bir hafta klasöründe zaten olan bir dosyanıza asla
dokunmaz. Gelenler siz `git add .` çalıştırana kadar izlenmez (git dosyaları görür ama
henüz kaydetmez) ve denetleyici bu dosyaları listeler. Aşağıdaki bölüm, çevrimdışı
olduğunuzda kullanacağınız elle yapma yolunu anlatır.

## İki remote, birbirinden çok farklı iki komut

Deponuzda `origin` adlı bir remote vardır (remote, deponuzun başka bir bilgisayardaki
kopyasının adresidir) ve `origin`, GitHub'daki kendi kopyanızdır. Bazı haftalar ders
şablonundan size bir başlangıç klasörü de verilir; bunun için `template` adlı ikinci bir
remote eklersiniz. Bu iki remote birbirinin yerine geçmez.

| | |
|---|---|
| `git pull` | Bu komut `origin`'den, yani kendi deponuzdan çeker; örneğin başka bir makinede çalıştıktan ya da tarayıcıda bir dosyayı düzenledikten sonra. Normal, günlük ve güvenlidir. |
| `git pull template main` | **Bu komutu asla çalıştırmayın.** |

Şablon, sizinkiyle ortak geçmişi olmayan ayrı bir depodur, çünkü kopyanız ondan
oluşturuldu, klonlanmadı. İkisini birleştirmek (birleştirmek, git'ten iki geçmişi tek
geçmişte toplamasını istemektir) git'in her dosyayı aynı anda uzlaştırmaya kalkmasına yol
açar: doldurduğunuz `student.json` boş olanla, bitirdiğiniz `hello.py` iskeletle ve
çalışmanız taslakla. Dersi çakışmaları çözmekle geçirirsiniz ve bir kez başarılı olan bir
`git pull` her seferinde aynısını yeniden dener.

Bunun yerine yalnızca gerçekten istediğiniz tek yolu alın:

```bash
git remote add template https://github.com/vedatcoskun-course/aiasd-template.git   # bir kez, hep
git fetch template
git checkout template/main -- week06
```

Bu komutlar tam olarak adını verdiğiniz yolu kopyalar ve başka hiçbir şeye dokunmaz. O
klasöre bir şey yazmadan **önce** çalıştırın. Sonra çalıştırırsanız çalışmanızın üzerine
yazarlar.

---

## Bir şey ters gittiğinde

> **Hatanın İLK değil SON satırını okuyun.** Git teşhisi en alta yazar. Üstündeki
> satırlar bağlamdır.

| Gördüğünüz | Anlamı |
|---|---|
| `Authentication failed`<br>`could not read Username for 'https://github.com'` | GitHub kim olduğunuzu bilmiyor. `gh auth login` çalıştırın. Hâlâ olmuyorsa `gh auth status` çalıştırın, çünkü yanlış hesapla girmiş olabilirsiniz. |
| `Support for password authentication was removed` | Bunun nedeni aynıdır. GitHub şifreniz burada kullanılamaz ve yeniden yazmak işe yaramaz. |
| `! [rejected] main -> main (fetch first)` | GitHub'da sizde olmayan bir commit var; genellikle tarayıcıda bir dosyayı düzenlediğiniz için. `git pull --rebase` çalıştırın, sonra yeniden push edin. |
| `nothing to commit, working tree clean` | Git bir değişiklik görmüyor. Ya editör kaydetmedi ya da yanlış klasördesiniz. `pwd` çalıştırın ve yazdığı klasöre bakın. |
| `fatal: not a git repository` | Projenin dışındasınız. `aiasd-project` içine `cd` yapın ve yeniden deneyin. |
| `index.lock ... File exists` | Bir git komutu yarıda kesildi. `rm -f .git/index.lock` çalıştırın ve yeniden deneyin. |
| Denetleyici *Cannot tell which week it is* diyor | Bu ilk çalıştırmadır ve ağ yoktur. Bir kez bağlanıp yeniden çalıştırın; sonrasında çevrimdışı da çalışır. |
| `command not found: python` | Bunun yerine `python3` deneyin. macOS'ta genellikle var olan `python3`tür. |
| `refusing to merge unrelated histories` | `origin` yerine `template`'ten pull yaptınız. `--allow-unrelated-histories` vermeyin; yukarıdaki bölüme bakın. |

---

**Hâlâ takıldınız mı?** Bir yapay zekâ asistanına sorun, ama özellikle git kimlik
doğrulaması konusunda kuşkucu olun. Kimlik doğrulama 2021'de değişti ve internetin çoğu
hâlâ eski yolu anlatıyor. Size GitHub şifrenizi kullanmanız ya da `git config credential.helper store` çalıştırmanız söyleniyorsa o tavsiye eskimiştir. Görmezden gelin
ve bu karta dönün.

Haftalık rutinin tamamı
[`AI_WEEKLY_WORKFLOW_STUDENT_TR.md`](AI_WEEKLY_WORKFLOW_STUDENT_TR.md) dosyasındadır.
Puanların neye verildiğini, her dersin sonunda ne olduğunu ve derse gelemezseniz ne
yapacağınızı söyler.
