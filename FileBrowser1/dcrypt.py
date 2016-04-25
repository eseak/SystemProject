#-*- coding: utf-8 -*-
import os, random, struct
from Crypto.Cipher import AES
import sys
def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    """ Decrypts a file using AES (CBC mode) with the
        given key. Parameters are similar to encrypt_file,
        with one difference: out_filename, if not supplied
        will be in_filename without its last extension
        (i.e. if in_filename is 'aaa.zip.enc' then
        out_filename will be 'aaa.zip')
    """
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
inputFileName=''
for k in range(1, len(sys.argv)):
    if (k==(len(sys.argv)-1)):
        inputFileName=inputFileName+sys.argv[k]
    else:
        inputFileName=inputFileName=sys.argv[1]+' '+sys.argv[k]
print(inputFileName, 'adlı dosya deşifre edlecek')
decrypt_file('1234567891234567',inputFileName, out_filename=None, chunksize=64*1024)