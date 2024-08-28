# onto-tracker-parse
Parse content made with the Obsidian plugin [Onto Tracker](https://github.com/jdchart/onto-tracker) in python.

## Basic Usage:

```python
import otp

VAULT_PATH = "path/to/vault"

# Define a function that will be run on each item in the freeze:
def my_function(element : otp.FreezeItem, other_params):
    print(element.path)
    print(element.tree)
    print(element.content)
    print(element.metadata)

vault = otp.Vault(VAULT_PATH)
latest = vault.get_latest_freeze()
latest.iter(my_function)
```