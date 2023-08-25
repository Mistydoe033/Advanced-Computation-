import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Define a simple hash function (modulus)
def basic_hash_function(key, size):
    return key % size

# Create a hash table
hash_table_size = 10
hash_table = [None] * hash_table_size

# Generate example data
data = list(range(101))

# Animation setup
fig, ax = plt.subplots(figsize=(8, 6))
plt.axis('off')
frames = len(data)

def animate(frame):
    ax.clear()
    value = data[frame]
    index = basic_hash_function(value, hash_table_size)
    
    if hash_table[index] is None:
        hash_table[index] = [value]
    else:
        hash_table[index].append(value)
    
    for i, bucket in enumerate(hash_table):
        if bucket is None:
            bucket_str = "Empty"
        else:
            bucket_str = " | ".join(map(str, bucket))
        
        plt.text(0.1, 0.9 - i*0.1, f'Bucket {i}: {bucket_str}', transform=plt.gca().transAxes)
    
    plt.title(f"Inserting {value} (Hashed to Bucket {index})")
    plt.axis('off')

anim = FuncAnimation(fig, animate, frames=frames, repeat=False)
plt.show()
