import requests
import hashlib
import struct


def get_latest_block_hash():
    url = "https://blockstream.info/api/blocks/tip/hash"
    return requests.get(url).text


def get_block(block_hash):
    url = f"https://blockstream.info/api/block/{block_hash}"
    return requests.get(url).json()


def get_block_header_hex(block_hash):
    url = f"https://blockstream.info/api/block/{block_hash}/header"
    return requests.get(url).text


def double_sha256(header_hex):
    header_bytes = bytes.fromhex(header_hex)
    hash1 = hashlib.sha256(header_bytes).digest()
    hash2 = hashlib.sha256(hash1).digest()
    return hash2[::-1].hex()  # reverse for display


def bits_to_target(bits):
    """
    Convert compact 'bits' representation to full target
    """
    exponent = bits >> 24
    coefficient = bits & 0xFFFFFF
    target = coefficient * 2 ** (8 * (exponent - 3))
    return target


def count_leading_zeros(hex_hash):
    binary = bin(int(hex_hash, 16))[2:].zfill(256)
    return len(binary) - len(binary.lstrip('0'))


def run_m2():
    print("\n=== M2: Block Header Analyzer (PRO) ===\n")

    #  Get latest block
    block_hash = get_latest_block_hash()
    block = get_block(block_hash)

    print("Block Hash:", block_hash)
    print("Height:", block["height"])
    print("Timestamp:", block["timestamp"])
    print("Nonce:", block["nonce"])
    print("Difficulty:", block["difficulty"])
    print("Bits:", block["bits"])

    #  Get REAL header (80 bytes)
    header_hex = get_block_header_hex(block_hash)

    print("\nHeader (hex):", header_hex)
    print("Header length (bytes):", len(bytes.fromhex(header_hex)))

    #  Compute hash
    computed_hash = double_sha256(header_hex)

    print("\nComputed Block Hash:", computed_hash)

    #  Count leading zeros
    zeros = count_leading_zeros(computed_hash)
    print("Leading zero bits:", zeros)

    #  Proof of Work verification
    target = bits_to_target(block["bits"])

    hash_int = int(computed_hash, 16)

    print("\nTarget:", target)
    print("Hash as integer:", hash_int)

    if hash_int < target:
        print("\n VALID Proof of Work")
    else:
        print("\n INVALID Proof of Work")


if __name__ == "__main__":
    run_m2()