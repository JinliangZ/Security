from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import *
from binascii import hexlify
import asn1


class RSACrypto(object):
    """
    RSAModule that implements the RSA encrypt, decrypt
    and signature according to pycrypto
    plaintext must be given when generate the instance
    """

    HASH_METHODS = {
        'MD5': MD5,
#         'SHA-1': SHA,
        'SHA-256': SHA256,
        'SHA-384': SHA384,
        'SHA-512': SHA512,
    }

    def __init__(self, msg):
        self.msg = msg  # plaintext

    def constructPriKey(self, args):
        """
                generate key pair according to the given argument
                argument must be a tuple includes fllowing elements in order:
                n:modulus
                e:Public exponent
                d:Private exponent
                p:First factor of n
                q:Second factor of n
        """
        self.prikey = RSA.construct(args)  # generate private key

        self.pubkey = self.prikey.publickey()  # generate public key

        return self.pubkey, self.prikey

    def signature(self, prikey, method):
        """
                sign message in PKCS1.5 by given hash method
                private key and specific hash method must be given
        """
        h = self.HASH_METHODS[method].new(self.msg)  # hash code

        signer = PKCS1_v1_5.new(prikey)

        signature = signer.sign(h)

        return h, signature

    def verify(self, h, signature):
        verifier = PKCS1_v1_5.new(self.pubkey)
        print(verifier.verify(h, signature))


n = 96593720236010659771827402676643429789938619440952555364622074956435340200061656508060615789030840134203664978505512524142393395270050853990539724973005030936743555266850207882401594704734189906511529782800955972664184033920361943962669563041630205806431828596746559268709959974499729037311769911690888754219
d = 17487594650354249938091950085575694561203926326607901939381432158293869287177190815388852195505606271149525992492300625584776502355602993463200235543352678006383997467860705323250971456335829396517506516991764156256889079821612990896638819945492250519738119781570884479786708912307843283470457443387159862073
e = 65537


f = open('signverify.py', 'r')

message = f.read().encode()

rsa = RSACrypto(message)

pubkey, prikey = rsa.constructPriKey((n, e, d))

h, signature = rsa.signature(prikey, 'SHA-256')

rsa.verify(h, signature)

