import os
import sys
import pyaes

## abrir o arquivo criptografado
if len(sys.argv) != 2:
    print("Uso: python encrypt.py <arquivo>")
    sys.exit(1)

file_name = sys.argv[1]

if not os.path.isfile(file_name):
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
    sys.exit(1)

file = open(file_name, "rb")
file_data = file.read()
file.close()

## chave para descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

## remover o arquivo criptografado
os.remove(file_name)

## criar o arquivo descriptografado
new_file = file_name.removesuffix(".ransomwaretroll")
new_file = open(f'{new_file}', "wb")
new_file.write(decrypt_data)
new_file.close()