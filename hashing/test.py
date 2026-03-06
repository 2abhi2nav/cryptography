import hashlib
import time
import matplotlib.pyplot as plt

def generate_mac_library(key, message, hash_name, block_size):
    
    if len(key) > block_size: 
        key = hashlib.new(hash_name, key).digest()
    if len(key) < block_size: 
        key = key.ljust(block_size, b'\x00')
    
    ipad = bytes([x ^ 0x36 for x in key])
    opad = bytes([x ^ 0x5c for x in key])
    
    inner_hash = hashlib.new(hash_name, ipad + message.encode()).digest()
    return hashlib.new(hash_name, opad + inner_hash).hexdigest()

def plot_results(results):
    sizes = [r[0] for r in results]
    md5_times = [r[1] for r in results]
    sha_times = [r[2] for r in results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, md5_times, label='Library MD5', marker='o', linestyle='-', color='blue')
    plt.plot(sizes, sha_times, label='Library SHA-512', marker='s', linestyle='--', color='red')
    
    plt.title('Message Size vs Execution Time (Library Functions)')
    plt.xlabel('Message Size (Bytes)')
    plt.ylabel('Time Consumption (Seconds)')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.5)
    plt.show()


sizes = [128, 512, 1024, 8*1024, 32*1024, 128*1024] 
results = []
key = b"secret_key"

print(f"{'Size (Bytes)':<15} | {'MD5 MAC Time (s)':<20} | {'SHA-512 MAC Time (s)':<20}")
print("-" * 65)

for size in sizes:
    msg = "A" * size
    
    
    start = time.perf_counter()
    generate_mac_library(key, msg, 'md5', 64)
    t_md5 = time.perf_counter() - start
    
    
    start = time.perf_counter()
    generate_mac_library(key, msg, 'sha512', 128)
    t_sha = time.perf_counter() - start
    
    results.append((size, t_md5, t_sha))
    print(f"{size:<15} | {t_md5:<20.8f} | {t_sha:<20.8f}")

plot_results(results)



key = b"key123"

msg = "HELLO"
result1 = generate_mac_library(key, msg, "md5", 64)   
result2 = generate_mac_library(key, msg, "sha512", 128)

print(result1)
print(result2)