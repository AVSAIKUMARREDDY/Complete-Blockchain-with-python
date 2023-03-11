import os
import subprocess
# file and directory listing
returned_text = subprocess.check_output("python3 -m secp256k1 privkey -p", shell=True, universal_newlines=True)

lis=returned_text.split()
sk=lis[0]
pk=lis[3]
print("private_key",sk)
print("public_key",pk)
