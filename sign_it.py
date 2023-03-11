import os
import subprocess
prv="94dd906c2ab03af99a8387c407141c0dedfd72251d0607cd84406d87ef0816fc"
msg="\"hello this is different message\""
print("messsage is :",msg)
# file and directory listing
returned_text = subprocess.check_output("python3 -m secp256k1 sign \
	-k {} \
	-m {}".format(prv,msg), shell=True, universal_newlines=True)
print("digital-signature :",returned_text)
