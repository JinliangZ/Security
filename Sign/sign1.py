import hashlib

def sign(filename,n,d):
    f = open("sign1.py","r")
    msg = f.read()
    m = hashlib.sha256()
    hash = hashlib.sha256()
    m.update(msg.encode())
    # calculate hash of file
    hash = m.digest()
    
    #The    (256-bit)    hash    of    certificate
    hashofcertificate = hash.hex()
    #    ASN.1    Encoding    header    specifying    the    hash    algorithm    (SHA    256    in    this    case)
    encodingheader = "3031300d060960864801650304020105000420"
    num = len(hex(n))
    num1 = len(encodingheader)
    num2 = len(hashofcertificate)
    num3 = num-num1-num2-6
    #PKCS1    1.5    Padding
    signaturebeforeRSA = '0001' + 'f'*num3 + '00' + encodingheader + hashofcertificate
    print(signaturebeforeRSA)
    #RSA    Sign
    signature1 = pow(int(signaturebeforeRSA,16), d, n)
    signature = hex(signature1)
    return signature
 
n = 96593720236010659771827402676643429789938619440952555364622074956435340200061656508060615789030840134203664978505512524142393395270050853990539724973005030936743555266850207882401594704734189906511529782800955972664184033920361943962669563041630205806431828596746559268709959974499729037311769911690888754219

e = 65537

d = 17487594650354249938091950085575694561203926326607901939381432158293869287177190815388852195505606271149525992492300625584776502355602993463200235543352678006383997467860705323250971456335829396517506516991764156256889079821612990896638819945492250519738119781570884479786708912307843283470457443387159862073

signature = sign('sign1.py',n,d)
print("signature = ",signature)