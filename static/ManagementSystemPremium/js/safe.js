// <script src="{% static 'js/jsencrypt.min.js' %}"></script>
var encryptor = new JSEncrypt();
// change -----BEGIN PUBLIC KEY----- and -----END PUBLIC KEY-----
// to -----BEGIN RSA PUBLIC KEY----- and -----END RSA PUBLIC KEY-----
console.log(encryptor.getPublicKey());
console.log(encryptor.getPrivateKey());