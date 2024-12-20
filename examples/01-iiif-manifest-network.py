import otp
import os
import uuid
from iiif_prezi3 import Manifest

VAULT_PATH = "/Users/jacob/Documents/plugin-test-vault"
OUTPUT_PATH = "/Users/jacob/Documents/Repos/onto-tracker-parse/output/iiif-manifest-network"
MANIFEST_PREFIX = "https://filebrowser.tetras-libre.fr/files/www/manifests/obsidian_network"
MEDIA_PREFIX = "https://filebrowser.tetras-libre.fr/files/www/manifests/obsidian_network"

# Define a function that will be run on each item in the freeze:
def my_function(element : otp.FreezeItem, other_params):
    print(element.path)
    print(element.tree)
    print(element.content)
    print(element.metadata)

    m = Manifest()

def process():
    if os.path.isdir(OUTPUT_PATH):
        print(f"Something already exists at{OUTPUT_PATH}")
    else:
        os.makedirs(OUTPUT_PATH)
        vault = otp.Vault(VAULT_PATH)
        latest = vault.get_latest_freeze()
        latest.iter(my_function)

process()