import hashlib
import hmac
import binascii


def hmac_sha256(key, msg):
    return hmac.new(key, msg, hashlib.sha256).digest()


key = b"12345"
msg = b"sample message"
print(binascii.hexlify(hmac_sha256(key, msg)))
