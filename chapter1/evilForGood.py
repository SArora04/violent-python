# import zipfile

# def extractFile(zFile, password):
#     try:
#         zFile.extractall(pwd=password)
#         return password
#     except Exception as e:
#         print(f"[-] Password not found: {password} because {e}")
#         return
# def main:
#     zFile = zipfile.ZipFile('chapter1/evil.zip')
#     passFile = open('chapter1/dict.txt')
#     for line in passFile.readlines():
#         pwd = line.strip('\n')
#         found = extractFile(zFile, pwd)
#         if found:
#             print(f"[+] Password found: {found}")
#             exit(0)

# if __name__ == "__main__":
#     main()
# from threading import Thread
# def extractFile(zFile, password):
#     try:
#         zFile.extractall(pwd=password)
#         print(f"[+] Password found: {password}")
#     except:
#         pass
# def main:
#     parser=optparser.OptionParser("usage%prog -f <zipfile> -d <dictionary>")
#     parser.add_option('-f', dest='zname', type='string', help='specify zip file')
#     parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
#     (options, args) = parser.parse_args()
#     if (options.zname == None) | (options.dname == None):
#         print(parser.usage)
#         exit(0)
#     else:
#         zname = options.zname
#         dname = options.dname
#     zFile = zipfile.ZipFile(zname)
#     passFile = open(dname)
#     for line in passFile.readlines():
#         password = line.strip('\n')
#         t = Thread(target=extractFile, args=(zFile, password))
#         t.start()

# if __name__ == "__main__":
#     main()
# Doesn't work with AES-128/256 or compression type 99
from threading import Thread
from optparse import OptionParser
import pyzipper

def extractFile(zname, password):
    try:
        with pyzipper.AESZipFile(zname) as zf:
            zf.extractall(pwd=password.encode())  # password must be bytes
            print(f"[+] Password found: {password}")
            exit(0)
    except Exception:
        pass

def main():
    parser = OptionParser("usage: %prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()

    if options.zname is None or options.dname is None:
        print(parser.usage)
        exit(0)

    zname = options.zname
    dname = options.dname

    with open(dname, 'r') as passFile:
        for line in passFile:
            password = line.strip()
            t = Thread(target=extractFile, args=(zname, password))
            t.start()

if __name__ == "__main__":
    main()



