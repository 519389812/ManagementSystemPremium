import base64
import json
import rsa
import os
from Crypto.Cipher import AES
import datetime


def new_rsa_key():
    pub_key, pri_key = rsa.newkeys(1024)
    pub = pub_key.save_pkcs1()
    with open('./pub.pem', 'wb') as f:
        f.write(pub)

    pri = pri_key.save_pkcs1()
    with open('./pri.pem', 'wb') as f:
        f.write(pri)


def load_rsa_pub_key(pem_path='./pub.pem'):
    if not os.path.exists(pem_path):
        print('错误，缺少%s文件' % pem_path, '错误')
        os._exit(0)
    with open(pem_path, 'rb') as f:
        key = f.read()
    key = rsa.PublicKey.load_pkcs1(key)
    return key


def load_rsa_pri_key(pem_path='./pri.pem'):
    if not os.path.exists(pem_path):
        print('错误，缺少%s文件' % pem_path, '错误')
        os._exit(0)
    with open(pem_path, 'rb') as f:
        key = f.read()
    key = rsa.PrivateKey.load_pkcs1(key)
    return key


def rsa_encrypt(text, pub_key):
    return rsa.encrypt(text.encode(), pub_key)


def rsa_decrypt(enc_text, pri_key):
    return rsa.decrypt(enc_text, pri_key)


def create_new_encrypt_file(json_path):
    with open(json_path, 'r') as f:
        text = f.read()
    pub_key = load_rsa_pub_key()
    text = rsa_encrypt(text, pub_key)
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


def aes_encrypt(key, text, iv):
    if type(key) == str:
        key = key.encode()
    if type(iv) == str:
        iv = iv.encode()
    text = add_16(text)
    mode = AES.MODE_CBC
    aes = AES.new(key, mode, iv)
    encrypt_text = base64.b64encode(aes.encrypt(text)).decode()
    return encrypt_text


def aes_decrypt(key, text, iv):
    if type(key) == str:
        key = key.encode()
    if type(iv) == str:
        iv = iv.encode()
    mode = AES.MODE_CBC
    aes = AES.new(key, mode, iv)
    decrypt_text = aes.decrypt(base64.b64decode(text.encode()))
    decrypt_text = decrypt_text.strip(b"\x00")
    decrypt_text = decrypt_text.decode()
    return decrypt_text


def create_usage(key, text, vi):
    usage = {'key': text}
    usage = json.dumps(usage)
    usage = aes_encrypt(key, usage, vi)
    with open('./usage.txt', 'wb') as f:
        f.write(usage)


if __name__ == '__main__':
    new_rsa_key()
    # key, vi = new_aes_key()
    # create_new_encrypt_file('JSONData.json')
    # create_usage(key, key, vi)
