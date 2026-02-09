
import os
import requests

# Missing IDs based on previous run
missing_ids = [35, 40, 41, 42, 43, 44, 45, 46]

products = [
    { "id": 35, "img": "https://drive.google.com/uc?export=view&id=114VOnxdLY7g50iWTearIZj6mRsurISpP" },
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

print(f"Attempting to download {len(products)} missing images...")

for p in products:
    url = p['img']
    filename = f"img/{p['id']}.jpg"
    print(f"Downloading {filename}...")
    try:
        # Added timeout to prevent hanging
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Success: {filename}")
        else:
            print(f"Failed to download {url} (Status: {response.status_code})")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

print("Retry download complete.")
