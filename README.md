Create a Plain Text File
You can create a plain text file using any text editor (like Notepad, TextEdit, or a code editor like VSCode). Here's an example of the content you can write:

kotlin
Copy code
Hello, this is a sample text file.
Save this file as sample.txt.

Step 2: Convert the Text to MD5 and SHA-256
You can use various tools or programming languages to compute MD5 and SHA-256 hashes. Below are methods using Python and command line tools.

Using Python
Install Python if you haven't already. You can download it from python.org.

Create a Python script (e.g., hash_generator.py) with the following code:

python
Copy code
import hashlib

# Read the content of the file
with open('sample.txt', 'r') as file:
    content = file.read()

# Generate MD5 hash
md5_hash = hashlib.md5(content.encode()).hexdigest()
print(f'MD5: {md5_hash}')

# Generate SHA-256 hash
sha256_hash = hashlib.sha256(content.encode()).hexdigest()
print(f'SHA-256: {sha256_hash}')
Run the script:

Open a terminal or command prompt, navigate to the directory where your script is saved, and run:

bash
Copy code
python hash_generator.py
Using Command Line Tools
If you prefer using the command line, you can use built-in tools like md5 and shasum (on macOS and Linux):

MD5:

bash
Copy code
md5 sample.txt
SHA-256:

bash
Copy code
shasum -a 256 sample.txt
Explanation of MD5 and SHA-256
MD5 (Message Digest Algorithm 5):

Produces a 128-bit hash value (32 hexadecimal characters).
Fast and widely used but not collision-resistant (meaning two different inputs can produce the same hash).
Commonly used for checksums and data integrity verification but not recommended for cryptographic security.
SHA-256 (Secure Hash Algorithm 256):

Part of the SHA-2 family and produces a 256-bit hash value (64 hexadecimal characters).
More secure than MD5 and designed to resist collision attacks.
Commonly used in various security applications and protocols, including TLS and Bitcoin.
