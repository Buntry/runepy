import requests, zipfile, io, os
from itertools import count

def get_set_link(set_number :int) -> str:
    return f"https://dd.b.pvp.net/datadragon-set{set_number}-en_us.zip"

for set_number in count(1):
    if (r := requests.get(get_set_link(set_number))).status_code != 200:
        break
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall()
