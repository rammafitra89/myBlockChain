# import libraries -> Developing Client
import hashlib
import random
import string
import json
import binascii
import numpy as np
import pandas as pd
import pylab as pl
import logging
import datetime
import collections

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Client:
   def __init__(self):
      random = Crypto.Random.new().read
      self._private_key = RSA.generate(1024, random)
      self._public_key = self._private_key.publickey()
      self._signer = PKCS1_v1_5.new(self._private_key)

   @property
   def identity(self):
   	return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

# Dinesh = Client()
# print (Dinesh.identity)

# output public key
# 30819f300d06092a864886f70d010101050003818d0030818902818100c6b0bba31229548ed8533cf162a8945d933f36f8c7fce630a45c2b4d4b928ce573fa102bdfcfbac16824b76f0a05ffb124438901444d4816179bb59d3eda071065a5f350cbe83ff36379f9d2231e205bf7c21da141f49111facda628c392fcccbeeccef89f613745dc9f04aaad0f02a99b10482dccf8548224de3838280899290203010001

# part transaction class..........................->
def __init__(self, sender, recipient,value):
	self.sender = sender
	self.recipient = recipient
	self.value = value
	self.time = datetime.datetime.now()

def to_dict(self):
	if self.sender == "Genesis":
		identity = "Genesis"
	else :
		identity = self.sender.indentify

		return collections.OrderDict({
			'sender' : identity,
			'recipient' : self.recipient,
			'value' : self.value,
			'time' : self.time
			})


def sign_transaction(self):
	private_key = self.sender._private_key
	signer = PKCS1_v1_5.new(private_key)
	h = SHA.new(str(self.to_dict()).encode('utf8'))
	return binascii.hexlify(signer.sign(h)).decode('ascii')

	Dinesh = Client()
	Ramesh = Client()

	t = Transaction(Dinesh,Ramesh.identity,5.0)

	signature = t.sign_transaction()
	print (signature)


