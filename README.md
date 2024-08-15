# Advanced Password Cracker

## What is Brute Force and This Tool?

### Brute Force Attack
A brute force attack is a method used to crack passwords or encryption by systematically trying every possible combination until the correct one is found. It is a straightforward but time-consuming approach, making it effective against weak or short passwords but less efficient as the password length and complexity increase.

### This Tool
This tool is an **Advanced Password Cracker** that can perform both dictionary and brute-force attacks on various hashes (MD5, SHA-1, SHA-256, SHA-512). It can identify the hash algorithm automatically, take a custom wordlist, and optimize brute-force attacks using multiprocessing to make the cracking process faster.

## Objective

The objective of this project is to create a robust and efficient password cracker that can be used to test the strength of passwords by attempting to crack them using various methods. This tool is designed to educate cybersecurity students and professionals on the importance of using strong and complex passwords.

## Special Features: Why It's Advanced

### 1. **Automatic Hash Algorithm Identification**
   - The tool automatically identifies the hashing algorithm (MD5, SHA-1, SHA-256, or SHA-512) based on the provided hash, saving time and ensuring accuracy in the cracking process.

### 2. **Optimized Brute Force with Multiprocessing**
   - Unlike many basic password crackers, this tool uses multiprocessing to distribute the brute-force attack across multiple CPU cores. This significantly reduces the time required to crack complex passwords by leveraging the full power of your machine.

### 3. **Custom Wordlist Integration**
   - The tool allows users to provide their custom wordlist for dictionary attacks, making it highly adaptable to different cracking scenarios and enabling targeted attacks based on known password patterns.

### 4. **Cross-Platform Compatibility**
   - Written in pure Python, this tool is cross-platform and can run on any operating system that supports Python, making it versatile and accessible to a wide range of users.

### 5. **User-Friendly Interface**
   - The tool provides a straightforward command-line interface that guides the user through the process, making it easy to use even for those who are new to password cracking.

### 6. **Highly Customizable Brute Force Parameters**
   - Users can define the character set and maximum password length for brute-force attacks, giving them control over the balance between speed and thoroughness.

## Skills Learned

- **Python Programming**: Writing efficient and optimized code using Python.
- **Hashing Algorithms**: Understanding and implementing various hashing algorithms (MD5, SHA-1, SHA-256, SHA-512).
- **Brute Force Techniques**: Learning how to implement and optimize brute force attacks.
- **Multiprocessing**: Using multiprocessing in Python to speed up tasks by leveraging multiple CPU cores.
- **Cybersecurity Concepts**: Gaining insights into password security and the importance of using complex passwords.

## Tools Used

- **Python**: The primary programming language used to build this tool.
- **Hashlib**: A Python library used for hashing operations.
- **Itertools**: A Python library used for creating iterators for efficient looping.
- **Multiprocessing**: A Python module used to implement parallel processing to speed up the brute-force attack.

## How It Works

1. **Hash Identification**: The tool first identifies the hash algorithm based on the length and characteristics of the hash provided by the user.
2. **Dictionary Attack**: If the user chooses a dictionary attack, the tool attempts to crack the password using a custom wordlist.
3. **Brute Force Attack**: If the user opts for a brute-force attack, the tool systematically tries every possible combination of characters up to a user-defined length. It uses multiprocessing to divide the task across multiple CPU cores, making the attack faster.
4. **Password Cracking**: The tool compares the hash of each attempted password with the given hash until a match is found or all possibilities are exhausted.

## Steps to Use

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/yourusername/advanced-password-cracker.git
   cd advanced-password-cracker
   ```

2. **Install Dependencies**: 
   Ensure you have Python installed. No additional libraries are needed as the tool uses standard Python libraries.

3. **Run the Tool**:
   ```bash
   python password_cracker.py
   ```

4. **Input the Hash**:
   - When prompted, enter the hash you want to crack.

5. **Choose the Attack Method**:
   - Choose between a dictionary attack (d) or brute-force attack (b).

6. **Provide a Wordlist (For Dictionary Attack)**:
   - If you choose a dictionary attack, provide the path to the wordlist file.

7. **Set Maximum Length (For Brute-Force Attack)**:
   - If you choose a brute-force attack, set the maximum password length to try.

8. **View Results**:
   - The tool will attempt to crack the password and display the result.

## Conclusion

This advanced password cracker is an educational tool that demonstrates the techniques and complexities involved in password cracking. It highlights the importance of using strong and secure passwords to protect sensitive information.

---

Thank you for exploring this project! If you have any questions or suggestions, feel free to open an issue or contribute to the repository.

