import bcrypt
def testPass(passw):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(passw, salt)

