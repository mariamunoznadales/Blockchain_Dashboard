import requests
import hashlib

def get_latest_block_hash():
    url = "https://blockstream.info/api/blocks/tip/hash"
    return requests.get(url).text

def get_block_header(block_hash):
    url = f"https://blockstream.info/api/block/{block_hash}"
    return requests.get(url).json()

def double_sha256(header_hex):
    header_bytes = bytes.fromhex(header_hex)
    hash1 = hashlib.sha256(header_bytes).digest()
    hash2 = hashlib.sha256(hash1).digest()
    return hash2.hex()

def count_leading_zeros(hex_hash):
    binary = bin(int(hex_hash, 16))[2:].zfill(256)
    return len(binary) - len(binary.lstrip('0'))

def run_m2():
    block_hash = get_latest_block_hash()
    block = get_block_header(block_hash)

    print("Block Hash:", block_hash)
    print("Height:", block["height"])
    print("Timestamp:", block["timestamp"])
    print("Nonce:", block["nonce"])
    print("Difficulty:", block["difficulty"])

    # Simulación del header (simplificado)
    header_hex = block_hash  # ⚠️ luego lo mejoramos

    computed_hash = double_sha256(header_hex)

    print("Computed Hash:", computed_hash)
    print("Leading zeros:", count_leading_zeros(computed_hash))

if __name__ == "__main__":
    run_m2()