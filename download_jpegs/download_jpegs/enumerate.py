import requests
import time

base = "https://cdn5.vscdns.com/images/models/photos/photo"
existing = []
for i in range(1, 5000):
    url = f"{base}{i:04d}.jpg"
    try:
        r = requests.head(url)
        if r.status_code == 200:
            existing.append(url)
    except requests.RequestException as e:
        # Optionally log the error or pass
        pass
print(f"Found {len(existing)} files")
print("List of found URLs:")
for url in existing:
    print(url)

# Save the URLs to a file for further processing
with open("found_urls.txt", "w") as f:
    for url in existing:
        f.write(url + "\n")
        existing.append(url)
    time.sleep(0.1)  # Add a short delay to avoid rate limiting

print(f"Found {len(existing)} files")
