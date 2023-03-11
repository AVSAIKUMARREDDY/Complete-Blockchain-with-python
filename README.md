# Complete-Blockchain-with-python
The description and demonstration of the project you can find here..https://youtu.be/I1hJeWZlOQQ

infuture i will extend this project to \
        1.real payent transaction along with keeping UTXO model. \
        2.smart contracts. \
        3.central bank digital currency model. 
        

steps to run the project \
step1: \
clone the repository: \
command: \
$ git clone https://github.com/AVSAIKUMARREDDY/Complete-Blockchain-with-python.git 

step2: \
navigate to the directory \
$ cd Complete-Blockchain-with-python 

step3: \
install basic utilities required to run the appcation \
$ pip install -r requirements.txt 

step4: \
Start a blockchain node server, 

$ export FLASK_APP=node_server.py \
$ flask run --port 8000 

step5: \
also run 2 more servers ,take the new shell and run \
$ export FLASK_APP=node_server.py \
$ flask run --port 8001 \
now the server will be running at 8001 \
take the shell again and run \
$ export FLASK_APP=node_server.py \
$ flask run --port 8002 

now total 3 servers are runinng the main one is at 8000 and other peers at 8001,8002 

step6: \
run the application \
$ python3 run_app.py \
now you can see the applcation running at port 5000 in your local address.

through client application you can submit transactions. 
  1.before submiting you need to run the key_gen.py to create private and public keys save both the keys and \
  2.sign the messge with the sign_it.py program here change the msg variable field to your desired message and in the place of string prv keep the priavte \      key and run the program and save the digital signature so that you can use this in the signature field in client application.

Join the nodes with each other  \
step7: \
register 8001 with 8000 \
$ curl -X POST http://127.0.0.1:8001/register_with -H 'Content-Type: application/json' -d '{"node_address": "http://127.0.0.1:8000"}' \
register 8002 with 8000 \
$ curl -X POST http://127.0.0.1:8002/register_with -H 'Content-Type: application/json' -d '{"node_address": "http://127.0.0.1:8000"}' 

step8: \
you can check the chain status by \
$ curl -X GET http://localhost:8001/chain \
$ curl -X GET http://localhost:8002/chain 

or 
in your browser type \
http:/localhost:80001/chain \
http://localhost:8002/chain 


for more details you can refer the video link https://youtu.be/I1hJeWZlOQQ 


all the above commands will work for linux and macOs. If you are a windows user kindly check im not sure. 










