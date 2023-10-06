from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Define the function to pad the data to match block size
def pad(data):
    block_size = AES.block_size
    return data + (block_size - len(data) % block_size) * chr(block_size - len(data) % block_size).encode()

# Generate a random encryption key and initialization vector (IV)
encryption_key = get_random_bytes(16)  # 128-bit key for AES encryption
iv = get_random_bytes(16)              # Initialization vector

# Create the AES cipher object in CBC mode
cipher = AES.new(encryption_key, AES.MODE_CBC, iv)

# Specify the file names
input_file = "input.txt"
output_file = "encrypted_file.enc"

# Open and read the input file
with open(input_file, "rb") as file:
    plaintext = file.read()

# Pad the plaintext to match the block size
padded_plaintext = pad(plaintext)

# Encrypt the data
cipher_text = cipher.encrypt(padded_plaintext)

# Write the encrypted data to the output file
with open(output_file, "wb") as file:
    file.write(cipher_text)

print(f"File '{input_file}' has been encrypted and saved as '{output_file}'.")
