from passlib.hash import des_crypt

def testPass(hashed_pass):
    salt = hashed_pass[:2]  # First 2 characters are the salt
    print(f"[*] Salt: {salt}")
    with open('chapter1\dict.txt') as dictF:
        for word in dictF:
            word = word.strip()
            # Hash using same salt
            guess_passw = des_crypt.using(salt=salt).hash(word)
            print(f"[*] Testing password: {guess_passw}")
            if guess_passw == hashed_pass:
                print(f"[+] Password found: {word}")
                return True
    print("[-] Password not found")
    return False

def main():
    with open('chapter1\passwords.txt') as passF:
        for line in passF:
            if ":" in line:
                user, passw = line.strip().split(":")
                passw = passw.strip()
                print(f"\n[*] Testing password for user: {user}")
                print(f"[*] Hashed password: {passw}")
                testPass(passw)

if __name__ == "__main__":
    main()
