import base64
import json
import rsa
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_v1_5, PKCS1_OAEP
import datetime
from ManagementSystemPremium.settings import PEM_VERSION


def set_crypto_pub_key(mode='PKCS1_OAEP/PKCS1_v1_5', current_version='v1'):
    crypto_pub_key = RSA.import_key(open("./ManagementSystemPremium/pub_%s.pem" % current_version).read())
    if mode == 'PKCS1_OAEP':
        cipher_pub_PKCS1_OAEP = PKCS1_OAEP.new(crypto_pub_key)
        return cipher_pub_PKCS1_OAEP, current_version
    elif mode == 'PKCS1_v1_5':
        cipher_pub_PKCS1_v1_5 = PKCS1_v1_5.new(crypto_pub_key)
        return cipher_pub_PKCS1_v1_5, current_version


def new_rsa_key(engine='rsa/PyCryptodome'):
    if engine == 'rsa':
        pub_key, pri_key = rsa.newkeys(1024)
        pub = pub_key.save_pkcs1()
        with open('./pub.pem', 'wb') as f:
            f.write(pub)
        pri = pri_key.save_pkcs1()
        with open('./pri.pem', 'wb') as f:
            f.write(pri)
    elif engine == 'PyCryptodome':
        key = RSA.generate(1024)
        private_key = key.export_key()
        with open("pri.pem", "wb") as f:
            f.write(private_key)
        public_key = key.publickey().export_key()
        with open("pub.pem", "wb") as f:
            f.write(public_key)
    else:
        return "engine mode error."


def crypto_rsa_encrypt(cipher, text, mode='PKCS1_OAEP/PKCS1_v1_5'):
    if mode == 'PKCS1_OAEP':
        return cipher.encrypt(text)
    elif mode == 'PKCS1_v1_5':
        return cipher.encrypt(text)
    else:
        return "mode error."


def rsa_encrypt(text, pem_path='./pub.pem'):
    if not os.path.exists(pem_path):
        return "encrypt error, public pem file not found."
    with open(pem_path, 'rb') as f:
        pub_key = f.read()
    pub_key = rsa.PublicKey.load_pkcs1(pub_key)
    return rsa.encrypt(text.encode(), pub_key)


def create_new_encrypt_file(json_path):
    with open(json_path, 'r') as f:
        text = f.read()
    text = rsa_encrypt(text)
    with open('./msg.txt', 'wb') as f:
        f.write(text)


ROT13 = str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")


def rot13_encode(text):
    return str.translate(text, ROT13)


def new_aes_key():
    n = datetime.datetime.now()
    key = str(n.strftime("%Y%m%d%H%M%S%f"))[:16]
    iv = n.timestamp().hex()[:16]
    return key, iv


def add_16(text):
    if type(text) == str:
        text = text.encode()
    while len(text) % 16 != 0:
        text += b'\x00'
    return text


def aes_encrypt(text, key, iv):
    if type(key) == str:
        key = key.encode()
    if type(iv) == str:
        iv = iv.encode()
    text = add_16(text)
    mode = AES.MODE_CBC
    aes = AES.new(key, mode, iv)
    encrypt_text = base64.b64encode(aes.encrypt(text)).decode()
    return encrypt_text


def create_usage(key, text, vi):
    usage = {'key': text}
    usage = json.dumps(usage)
    usage = aes_encrypt(key, usage, vi)
    with open('./usage.txt', 'wb') as f:
        f.write(usage)


if __name__ == '__main__':
    new_rsa_key('PyCryptodome')
    # key, vi = new_aes_key()
    # create_new_encrypt_file('JSONData.json')
    # create_usage(key, key, vi)
