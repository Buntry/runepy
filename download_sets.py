import requests, zipfile, io, os
from itertools import count

set_download_folder = '.sets'

def get_set_file(set_number :int) -> str:
    return f"datadragon-set{set_number}-en_us"

def get_set_link(set_number :int) -> str:
    return f"https://dd.b.pvp.net/{get_set_file(set_number)}.zip"

p = os.path.abspath(set_download_folder)
if not os.path.exists(p):
    os.mkdir(p)

for set_number in count(1):
    if (r := requests.get(get_set_link(set_number))).status_code != 200:
        break
    sp = os.path.join(p, get_set_file(set_number))
    if not os.path.exists(sp):
        os.mkdir(sp)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(sp)
