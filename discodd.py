from notoken887.encryptor import TokenCryptor
cryptor = TokenCryptor()
original_string = "special emoji encryption bot token"
encrypted = cryptor.encrypt(original_string)
decrypted = cryptor.decrypt(encrypted)

TOKEN= decrypted
