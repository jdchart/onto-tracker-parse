import otp

VAULT_PATH = "/Users/jacob/Documents/plugin-test-vault"

# Define a function that will be run on each item in the freeze:
def my_function(element : otp.FreezeItem, other_params):
    print(element.path)
    print(element.tree)
    print(element.content)
    print(element.metadata)

# Get the obsidian vault:
vault = otp.Vault(VAULT_PATH)

# Get the latest freeze:
latest = vault.get_latest_freeze()

# Trigger the function given above for each item in the freeze:
latest.iter(my_function)