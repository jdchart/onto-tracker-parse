import otp
import nakalapycon as nklco

VAULT_PATH = "/Users/jacob/Documents/plugin-test-vault"
NAKALA_API_KEY = "01234567-89ab-cdef-0123-456789abcdef"
CREATOR_VALUE = {'givenname': 'Etienne', 'surname': 'Balazs', 'orcid': '', 'authorId': 'f6aff924-485b-4cbb-9b38-26ce2a07504a', 'fullName': 'Etienne Balazs'}
LICENSE_VALUE = "etalab-2.0" # https://documentation.huma-num.fr/nakala-guide-de-description/#licence-obligatoire

# If COLLECTION_ID == None, a collection will be created with the given title.
# Otherwise, the collection of given ID will be retrieved and added to.
COLLECTION_TITLE = "Test collection onto tracker"
COLLECTION_ID = "10.34847/nkl.6a448553"

# Define a function that will be run on each item in the freeze:
def my_function(element : otp.FreezeItem, other_params):
    print("Treating " + element.metadata["file_name"] + "...")

    # Upload file:
    file_rep = nklco.post_datas_uploads(other_params["nakala_target"], element.metadata["path"])

    # Create data:
    data_data = {
        "status": "published",
        "metas": [
            {"value": element.metadata["file_name"], "propertyUri": "http://nakala.fr/terms#title", "lang": None, "typeUri": None},
            {"value": "http://purl.org/coar/resource_type/c_c513", "propertyUri": "http://nakala.fr/terms#type", "lang": None, "typeUri": "http://purl.org/dc/terms/URI"}, # TODO Automate https://documentation.huma-num.fr/nakala-guide-de-description/#type-de-depot-obligatoire
            {"value": CREATOR_VALUE, "propertyUri": "http://nakala.fr/terms#creator", "lang": None, "typeUri": None},
            {"value": "2024", "propertyUri": "http://nakala.fr/terms#created", "lang": None, "typeUri": None}, # TODO Automate
            {"value": LICENSE_VALUE, "propertyUri": "http://nakala.fr/terms#license", "lang": None, "typeUri": None}
        ],
        "files": [
            {"sha1": file_rep.dictVals["sha1"], "description": element.content}
        ],
        "collectionsIds": [other_params["coll_id"]],
        "rights": [{"id": other_params["user_id"], "role": "ROLE_READER"}]
    }

    # Upload data:
    rep = nklco.post_datas(other_params["nakala_target"], data_data)

    # Add the markdown content as description metadata:
    if element.content != "":
        desc_data = {"value": element.content, "propertyUri": "http://purl.org/dc/terms/description", "lang": None, "typeUri": None}
        nklco.post_datas_metadatas(other_params["nakala_target"], rep.dictVals["payload"]["id"], desc_data)

def process():
    # Connect to test instance of nakala using our API key and get our user id::
    nkl_tar = nklco.NklTarget(False, NAKALA_API_KEY)
    user_id = nklco.get_users_me(nkl_tar).dictVals["userGroupId"]
    
    # Create a new collection and return it's id (or retrive existing one):
    if COLLECTION_ID == None:
        coll_id = create_nakala_collection(COLLECTION_TITLE, nkl_tar, user_id)
        print(f"Created a collection. Id: \"{coll_id}\".")
    else:
        coll_id = COLLECTION_ID

    # Get obsidian vault content and iter:
    vault = otp.Vault(VAULT_PATH)
    latest = vault.get_latest_freeze()
    latest.iter(my_function, {"nakala_target" : nkl_tar, "coll_id" : coll_id, "user_id" : user_id})

    # Delete temporary files on nakala server:
    nklco.delete_datas_uploads_all(nkl_tar)

    # coll = nklco.get_collections(nkl_tar, "10.34847/nkl.c57c6ep9")

def create_nakala_collection(collection_title, nakala_target, user_id):
    # Create the collection data:
    collection_data = {
        "status": "public",
        "metas": [
            {"value": collection_title, "propertyUri": "http://nakala.fr/terms#title", "lang": None, "typeUri": None}
        ],
        "datas": [],
        "rights": [{"id": user_id, "role": "ROLE_READER"}]
    }

    # Create the collection and retrieve the id:
    coll = nklco.post_collections(nakala_target, collection_data)
    coll_id = coll.dictVals["payload"]["id"]

    return coll_id

process()