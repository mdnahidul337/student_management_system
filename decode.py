import hashlib
from Crypto.Protocol.KDF import scrypt
import binascii

# Get user input for the password to test
password_to_test = input("Enter the password to check: ")

# Parameters from the scrypt hash (as seen in your provided string)
salt = binascii.a2b_base64('wbFFMaWnImYE9ls0')  # The salt used in the hash
iterations = 32768  # The number of iterations used
block_size = 8      # The block size used in the scrypt function
parallelization_factor = 1  # The parallelization factor used

# The hash value from the second part of your string (after the '$')
hashed = binascii.a2b_base64('c667b62245fbc03e030c6bda34e6edfb02202a714cfeea9724fcdf7860f0218070066f4225e32621741bc16989c96db8bffe1fa7c26c65cbf018cac42eb63d0f')

# Function to check if the entered password matches the hash
def verify_password(password, salt, iterations, block_size, parallelization_factor):
    # Derive the key from the password using scrypt
    key = scrypt(password.encode(), salt, key_len=len(hashed), N=iterations, r=block_size, p=parallelization_factor)
    return key == hashed

# Check if the entered password matches the hash
if verify_password(password_to_test, salt, iterations, block_size, parallelization_factor):
    print("Password matches!")
else:
    print("Password does not match.")
