
import os
import requests

products = [
    { "id": 1, "img": "https://drive.google.com/uc?export=view&id=1cO3dHJDazv3E00NSOki5GpcEdSE79ABO" },
    { "id": 2, "img": "https://drive.google.com/uc?export=view&id=11ACNvp0CsOAJ46cZATzxclIYaehaWz0t" },
    { "id": 3, "img": "https://drive.google.com/uc?export=view&id=1qYQjzSNKBTV2PLPpMouUn5auh2eyjyRT" },
    { "id": 4, "img": "https://drive.google.com/uc?export=view&id=1Vm2TX9lRTEgX1mT-qVCjS_5aDacAbEQi" },
    { "id": 5, "img": "https://drive.google.com/uc?export=view&id=1kVUvV6JqYnw6B12msJ-rdLRIDa8ikIfF" },
    { "id": 6, "img": "https://drive.google.com/uc?export=view&id=1K57g_ptHtFVT0GHTlR1669lMPJirr9ES" },
    { "id": 7, "img": "https://drive.google.com/uc?export=view&id=1ZtzvVivQh_9JKRC74-_Va6fbe32seOw1" },
    { "id": 8, "img": "https://drive.google.com/uc?export=view&id=1k9hmlUgEIvzUOsiSzLRLoiSvL74ygj_9" },
    { "id": 9, "img": "https://drive.google.com/uc?export=view&id=1hNI7Jq2h_AZAD-H6ynRQYdoTSQELgNCp" },
    { "id": 10, "img": "https://drive.google.com/uc?export=view&id=1CNo8z4wyUvxaxi3qVdwbKq_8jGP3JyRK" },
    { "id": 11, "img": "https://drive.google.com/uc?export=view&id=1csqLQ7EpGtgzcC2rClxf5RSkuD1DOlqy" },
    { "id": 12, "img": "https://drive.google.com/uc?export=view&id=1zLObch_KN_jVdTLFCaFpiaWKDjfzXEil" },
    { "id": 13, "img": "https://drive.google.com/uc?export=view&id=1Qk2AruaQsj-cSKppExZmqCb36ocDv50m" },
    { "id": 14, "img": "https://drive.google.com/uc?export=view&id=11HL73rVIn2wnab9loZINDtoTufkU9fb8" },
    { "id": 15, "img": "https://drive.google.com/uc?export=view&id=1gga8Af_b1O3rzhy3MfYjeELc5zXrC_KR" },
    { "id": 16, "img": "https://drive.google.com/uc?export=view&id=1qTIT-cnugNNfGWEepkjjG7EFAP_GylVq" },
    { "id": 17, "img": "https://drive.google.com/uc?export=view&id=1Vflq9eEr8GcP4vMb9CMz51UcnQe_ZVyb" },
    { "id": 18, "img": "https://drive.google.com/uc?export=view&id=1DDsUykKMqv2lX1rOKWjfuNctVYMPoYD9" },
    { "id": 19, "img": "https://drive.google.com/uc?export=view&id=17-TPe0XzqFv6gikT73M7bahldNzQldyB" },
    { "id": 20, "img": "https://drive.google.com/uc?export=view&id=1-ZC5TIflEq8P6aMRe9u0wByJt-_3uPDP" },
    { "id": 21, "img": "https://drive.google.com/uc?export=view&id=1hLKDLfpQPZz49ygmdmMaGhdmlkLZAJSQ" },
    { "id": 22, "img": "https://drive.google.com/uc?export=view&id=18HEU_hbdhXRxoFNfiqp_pa9IVu-hnirg" },
    { "id": 23, "img": "https://drive.google.com/uc?export=view&id=1kZjc3AVRr7ZVfdhswUjLq8zEpoXRpffU" },
    { "id": 24, "img": "https://drive.google.com/uc?export=view&id=1OVpYME7AyKfI1vS_7v1feLR2ALijEJsQ" },
    { "id": 25, "img": "https://drive.google.com/uc?export=view&id=1Fj_QHnfs4mjqfjSFafWopTcBbzl61OJp" },
    { "id": 26, "img": "https://drive.google.com/uc?export=view&id=1rwvlDF3me9tpTp30iBP2YAzbreVa8JZU" },
    { "id": 27, "img": "https://drive.google.com/uc?export=view&id=1qA8LN0dfxOiZP729aicac73S93_JzfLB" },
    { "id": 28, "img": "https://drive.google.com/uc?export=view&id=1CZbX5NdnferepuWfE5ukdcDbw_CjFrR2" },
    { "id": 29, "img": "https://drive.google.com/uc?export=view&id=1HL8qipp0DsdtIB4KIifiw8kRd_Er0w25" },
    { "id": 30, "img": "https://drive.google.com/uc?export=view&id=13Fop974XNZEuzn1JkwKtSu8P8eGgNXvV" },
    { "id": 31, "img": "https://drive.google.com/uc?export=view&id=1lV9zPK9__NhYDWHnWxrmZRh6RY16qCZu" },
    { "id": 32, "img": "https://drive.google.com/uc?export=view&id=1cF0rVFDx1-P5VsDwY7ujBmpgAAwtsom5" },
    { "id": 33, "img": "https://drive.google.com/uc?export=view&id=1zZIBALhssxJJ8hBlCrdQk-nXqcw5BSAF" },
    { "id": 34, "img": "https://drive.google.com/uc?export=view&id=1T6FaFWdIdXkJU7mJrkufodsGlC1m0NVB" },
    { "id": 35, "img": "https://drive.google.com/uc?export=view&id=114VOnxdLY7g50iWTearIZj6mRsurISpP" },
    { "id": 36, "img": "https://drive.google.com/uc?export=view&id=1kpf3i8XZxGN6tjHqvHrW2fKPeQJjZSNX" },
    { "id": 37, "img": "https://drive.google.com/uc?export=view&id=1_KYLeyp8jHS23PfD-rD6a7awqNNYsIfJ" },
    { "id": 38, "img": "https://drive.google.com/uc?export=view&id=122uz1jAwLbgql5D9yzYwx3oasHFEiL0I" },
    { "id": 39, "img": "https://drive.google.com/uc?export=view&id=10EAxSEM-q8OhTRjFaZFvh_oYEyxqJvsv" },
    { "id": 40, "img": "https://drive.google.com/uc?export=view&id=1aFkxBtu3atjzAiCh9MBzdPOMsL5EpOzp" },
    { "id": 41, "img": "https://drive.google.com/uc?export=view&id=19reJZJ5pB6nouB1NfQla9jshScvpH2-M" },
    { "id": 42, "img": "https://drive.google.com/uc?export=view&id=1LEfYJJzsN19yrjQw2-52tqOkRdXbLPn4" },
    { "id": 43, "img": "https://drive.google.com/uc?export=view&id=1ZzaHN_iMQ319Yswt-51scSXmsPDd2H0a" },
    { "id": 44, "img": "https://drive.google.com/uc?export=view&id=1fAnyfPxYgxaAjsyvkxQTQ4tSvz-fdc93" },
    { "id": 45, "img": "https://drive.google.com/uc?export=view&id=1qDZKM6xQpLH8neKG0No1wI6OY-3tXB97" },
    { "id": 46, "img": "https://drive.google.com/uc?export=view&id=1OEt_qaboFRdL0K06Q552VgJS_epaJDI-" }
]

if not os.path.exists('img'):
    os.makedirs('img')

for p in products:
    url = p['img']
    filename = f"img/{p['id']}.jpg"
    print(f"Downloading {filename}...")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

print("Download complete.")
