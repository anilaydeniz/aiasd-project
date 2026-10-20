# On dakikada FastAPI — asistanınızın yazdığını nasıl okursunuz

*AIASD · 5. hafta · tek sayfa. Elle çok FastAPI yazmayacaksınız; çok FastAPI okuyacaksınız.
Bu kart, onu okumak, çalıştırmak ve ona hayır demek için gerekenlerdir.*

## 1. Uygulama ve bir route

```python
from fastapi import FastAPI

app = FastAPI(title="StudyRoom")          # the server; uvicorn runs this object


@app.get("/health")                      # method + path: one row of api.md
def health() -> dict:
    return {"status": "ok"}               # a dict becomes JSON: {"status": "ok"}
```

`@app.get`, `@app.post`, `@app.put`, `@app.patch`, `@app.delete`: dekoratör, fonksiyonun hangi
metoda ve hangi yola cevap verdiğini söyler. **Önce onu `api.md` satırınızla karşılaştırın**:
aynı metot, aynı yol, harfi harfine.

## 2. İstemcinin gönderdiği: istek

```python
from pydantic import BaseModel


class CodeRequest(BaseModel):             # the JSON body, field by field
    email: str


@app.post("/auth/code")
def ask_for_code(body: CodeRequest) -> dict:
    ...
```

Bir `BaseModel`, JSON gövdesinin alanlarını listeler. Bir alan eksikse FastAPI, fonksiyonunuz
çalışmadan önce kendiliğinden **422** ile cevap verir. **Her alanı okuyun**: bir giriş modeline
`password: str` ekleyen bir asistan REQ-001'i bozmuştur.

Yolun değişen bir parçası: `@app.get("/rooms/{room_id}")` ve `def room(room_id: int)`.

## 3. Çalışmadığında: hata

```python
from fastapi import HTTPException

raise HTTPException(status_code=401, detail="Wrong code")
```

`api.md` satırınızdaki her hata, kendi durum koduyla bir `raise HTTPException(...)` olur. Bu
hafta henüz yapılmamış her route tek bir şey yapar:
`raise HTTPException(status_code=501, detail="Not built yet: Week 6")`.

## 4. Çalıştırın ve bakın

```bash
uvicorn server.main:app --reload          # from the root of your repository
```

- http://127.0.0.1:8000/docs her route'u listeler. Asistan ne derse desin, **orada olmayan bir
  route yoktur**. "Try it out" gerçek bir istek gönderir.
- `--reload` her kayıtta sunucuyu yeniden başlatır. Ctrl+C onu durdurur.
- Terminal her isteği durum koduyla gösterir: `"POST /auth/code HTTP/1.1" 501`.

## 5. Bir test

```python
from fastapi.testclient import TestClient

from server.main import app

client = TestClient(app)                  # a client that talks to the app without a network


def test_TC_002_02_a_busy_slot_is_refused():
    response = client.post("/bookings", json={"room": 3, "start": "14:00", "minutes": 60})
    assert response.status_code == 409
```

`python -m pytest`, adı `test_` ile başlayan her fonksiyonu çalıştırır. Her `assert`, test
case'in beklenen sonuçlarından biridir. Son satır onları sayar: `1 failed, 2 passed`.

## 6. Reddedilecek beş şey

1. Metodu ya da yolu `api.md`'dekinden farklı bir route.
2. Hiçbir gereksinimin istemediği bir alan: `password`, `phone`, `is_admin`.
3. `print()` ile yazdırılan ya da bir log'a yazılan bir giriş kodu, şifre ya da token.
4. Geçsin diye beklenen değeri değiştirilmiş bir test.
5. Sormadığınız bir dosyada yapılmış bir değişiklik.
