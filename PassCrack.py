import hashlib
import itertools
import string
import multiprocessing

# Function to hash a given password using the specified algorithm
def hash_password(password, algorithm='md5'):
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif algorithm == 'sha512':
        return hashlib.sha512(password.encode()).hexdigest()
    else:
        raise ValueError("Unsupported algorithm. Use 'md5', 'sha1', 'sha256', or 'sha512'.")

# Function to identify the hashing algorithm based on hash length and characteristics
def identify_hash_algorithm(hash_to_crack):
    hash_length = len(hash_to_crack)
    if hash_length == 32:
        return 'md5'
    elif hash_length == 40:
        return 'sha1'
    elif hash_length == 64:
        return 'sha256'
    elif hash_length == 128:
        return 'sha512'
    else:
        raise ValueError("Unknown hash type. Could not identify the algorithm.")

# Function to load a custom wordlist from a file
def load_custom_wordlist(file_path):
    try:
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("[-] Wordlist file not found.")
        return []

# Dictionary attack function
def dictionary_attack(hash_to_crack, wordlist, algorithm='md5'):
    for password in wordlist:
        if hash_password(password, algorithm) == hash_to_crack:
            print(f"[+] Password found: {password}")
            return
    print("[-] Password not found in wordlist.")

# Worker function for brute force attack using multiprocessing
def brute_force_worker(charset, hash_to_crack, algorithm, length):
    for password in itertools.product(charset, repeat=length):
        password = ''.join(password)
        if hash_password(password, algorithm) == hash_to_crack:
            print(f"[+] Password found: {password}")
            return password
    return None

# Brute force attack function with multiprocessing
def brute_force_attack(hash_to_crack, algorithm='md5', max_length=5):
    chars = string.ascii_letters + string.digits
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_cores)
    
    for length in range(1, max_length + 1):
        jobs = []
        for charset_partition in partition_characters(chars, num_cores):
            job = pool.apply_async(brute_force_worker, (charset_partition, hash_to_crack, algorithm, length))
            jobs.append(job)
        
        for job in jobs:
            result = job.get()
            if result:
                pool.terminate()
                return result

    print("[-] Password not found with brute force attack.")

# Helper function to partition characters for multiprocessing
def partition_characters(chars, num_partitions):
    avg_len = len(chars) // num_partitions
    return [chars[i * avg_len:(i + 1) * avg_len] for i in range(num_partitions)]

# Main function to get user input and start the cracking process
if __name__ == "__main__":
    hash_to_crack = input("Enter the hash to crack: ")
    try:
        algorithm = identify_hash_algorithm(hash_to_crack)
        print(f"[+] Identified hash algorithm: {algorithm}")
    except ValueError as e:
        print(e)
        exit(1)

    method = input("Choose attack method (dictionary (d)/brute-force (b)): ").lower()

    if method == "d":
        wordlist_file = input("Enter the path to the wordlist file: ")
        wordlist = load_custom_wordlist(wordlist_file)
        dictionary_attack(hash_to_crack, wordlist, algorithm)
    elif method == "b":
        max_length = int(input("Enter the maximum password length for brute-force: "))
        brute_force_attack(hash_to_crack, algorithm, max_length)
