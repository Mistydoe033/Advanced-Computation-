import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# Define RSA functions (simplified)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def generate_key_pair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537  # A commonly used value for e
    while gcd(e, phi) != 1:
        e += 2

    d = pow(e, -1, phi)  # Calculating modular inverse

    return (n, e), (n, d)

def rsa_encrypt(message, public_key):
    n, e = public_key
    return [pow(ord(char), e, n) for char in message]

def rsa_decrypt(ciphertext, private_key):
    n, d = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Example values
p = 61
q = 53
public_key, private_key = generate_key_pair(p, q)
message = "HELLO"
ciphertext = rsa_encrypt(message, public_key)
decrypted_message = rsa_decrypt(ciphertext, private_key)

# Create animation
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
text = ax.text(0.5, 0.5, "", fontsize=12, ha='center', va='center')

steps = [
    f"Original message: {message}",
    f"Prime numbers: p = {p}, q = {q}",
    f"Generating keys...",
    f"Public key (n, e): {public_key}",
    f"Private key (n, d): {private_key}",
    f"Encrypting message...",
    f"Ciphertext: {ciphertext}",
    f"Decrypting ciphertext...",
    f"Decrypted message: {decrypted_message}",
    "RSA process complete."
]

def animate(frame):
    text.set_text(steps[frame])
    plt.pause(2.5)  # Pause for 2.5 seconds per frame

anim = FuncAnimation(fig, animate, frames=len(steps), repeat=False)

plt.show()
