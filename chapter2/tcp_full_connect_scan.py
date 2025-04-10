from socket import *

def connScan(tgtHost, tgtport):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtport))
        print(f"[+] {tgtport}/tcp open")
        connSkt.close()
    except:
        print(f"[-] {tgtport}/tcp closed")
    
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Unknown host")
        return
    
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(f"[+] Scan results for: {tgtName[0]}")
    except:
        print(f"[+] Scan results for: {tgtIP}")
    
    setdefaulttimeout(1)
    
    for tgtport in tgtPorts:
        print(f"Scanning port {tgtport}...")
        connScan(tgtHost, int(tgtport))

portScan("8.8.8.8", [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 3389])