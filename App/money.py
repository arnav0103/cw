from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
import json
from helpers import amount
import cv2
import kivy
from pyzbar import pyzbar
import os
import threading
from kivy.uix.screenmanager import Screen,ScreenManager
import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse


Window.size = (400, 700)
######################################
class Blockchain:

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof = 1, previous_hash = '0')
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions' : self.transactions}
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys = True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True
    def add_transaction(self, sender, receiver , amount):
        self.transactions.append({'sender' : sender,
                                'receiver' : receiver,
                                'amount' : amount})
        previous_block = self.get_previous_block()
        return previous_block['index'] + 1

    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for i in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain =longest_chain
            return True
        return False

app = Flask(__name__)

node_address = str(uuid4()).replace('-', '')

blockchain = Blockchain()


@app.route('/mine_block', methods = ['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    blockchain.add_transaction(sender = node_address, receiver= 'User', amount = 1)
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions' : block['transactions']}
    return jsonify(response), 200

@app.route('/get_chain', methods = ['GET'])
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


@app.route('/is_valid', methods = ['GET'])
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200

@app.route('/add_transaction' , methods = ['POST'])
def add_transaction():
    a_file = open("transaction.json", "r")
    json_objects = json.load(a_file)
    a_file.close()
    transaction_keys = ['sender' , 'receiver' , 'amount']
    if not all (key in json_objects for key in transaction_keys):
        return'Some elements of the transaction are missing', 400
    index = blockchain.add_transaction(json_objects['sender'], json_objects['receiver'], json_objects['amount'])
    response = {'message' : f'this transaction will be added to block {index}'}
    return jsonify(response), 201

@app.route('/connect_node', methods = ['POST'])
def connect_node():
    a_file = open("nodes.json", "r")
    json_objects = json.load(a_file)
    a_file.close()
    nodes = json_objects.get('nodes')
    if nodes is None:
        return "No node", 400
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': 'all the nodes are now connected. The bankcoin blockchain now contains the following nodes:',
                'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201

@app.route('/replace_chain', methods = ['GET'])
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'many chains so replaced',
                    'new_chain': blockchain.chain}
    else:
        response = {'message': 'we have the largest',
                    'actual_chain': blockchain.chain}
    return jsonify(response), 200
def start_app():
    print("Starting Flask app...")
    app.run(port=5000, debug=False)

#######################################
class qr(MDApp):
    def read_barcodes(frame):
        barcodes = pyzbar.decode(frame)
        qr_text = ''
        cv2.rectangle(frame, (232, 181),(232+220, 181+220), (0, 255, 0), 2)
        for barcode in barcodes:
            qr_text = barcode.data.decode('utf-8')
        if qr_text:
            return frame,qr_text
        else:
            return frame,''

    def build(self):
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()
            frame,qr_text = qr.read_barcodes(frame)
            if qr_text:

                dictionary ={
                            "sender" : "tijil",
                            "receiver" : qr_text,
                            "amount" : 10
                            }

                json_object = json.dumps(dictionary, indent = 3)
                with open("transaction.json", "w") as outfile:
                    outfile.write(json_object)

                my_app().run()
            cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break

class my_app(MDApp):
    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = "500"
        self.amount = Builder.load_string(amount)
        a_file = open("transaction.json", "r")
        json_objects = json.load(a_file)
        a_file.close()
        payto = MDLabel(text="You are paying", halign="center", font_style="H4",
                        pos_hint={"center_x": 0.5, "center_y": 0.9})
        payto_user = MDLabel(text=json_objects["receiver"], halign="center", font_style="H4",
                        pos_hint={"center_x": 0.5, "center_y": 0.84}, bold=True)
        userbal = MDLabel(text="Your reward points: 500", halign="center", font_style="Subtitle2",
                        pos_hint={"center_x": 0.5, "center_y": 0.6}, theme_text_color="Secondary")
        button = MDRaisedButton(text="        Pay        ", pos_hint={"center_x": 0.5, "center_y": 0.5},
                                on_release=self.show_data)
        screen.add_widget(payto)
        screen.add_widget(payto_user)
        screen.add_widget(userbal)
        screen.add_widget(self.amount)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
            a_file = open("transaction.json", "r")
            json_objects = json.load(a_file)
            a_file.close()
            json_objects['amount'] = self.amount.text
            a_file = open("transaction.json", "w")
            json.dump(json_objects, a_file)
            a_file.close()
            with app.app_context():
                connect_node()
                add_transaction()
                replace_chain()
                
if __name__ == '__main__':
    if os.environ.get("WERKZEUG_RUN_MAIN") != 'true':
        threading.Thread(target=start_app).start()
    qr().run()
