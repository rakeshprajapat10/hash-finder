import hashlib
import os
from pyfiglet import Figlet

def get_user_input(prompt):
  while True:
    file_path = input(prompt)
    if os.path.exists(file_path):
      return file_path
    else:
      print("Invalid file path. Please enter a valid path:")

def calculate_md5(file_path):
  try:
    with open(file_path, 'rb') as file:
      data = file.read()
      md5_hash = hashlib.md5(data).hexdigest()
      return md5_hash
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
  except PermissionError:
    print(f"Error: Insufficient permissions to access '{file_path}'.")
  return None

def check_hash_database(md5_hash):
  sample_hashes = {"00000000000000000000000000000000": "Known Malware 1"}
  if md5_hash in sample_hashes:
    return f"WARNING: The file hash matches a known malware: {sample_hashes[md5_hash]}"
  else:
    return "The hash does not match any known malware in the sample database."

if __name__ == "__main__":
  f = Figlet(font='slant')  
  print(f.renderText('Hash Finder'))
  text = "By: Rakesh"
padding = int((80 - len(text)) / 2)
print(" " * padding + text + " " * padding)
file_path = get_user_input("Enter the path to the file: ")
md5_hash = calculate_md5(file_path)

if md5_hash:
    print(f"MD5 hash of {file_path}: {md5_hash}")
    malware_check = check_hash_database(md5_hash)
    print(malware_check)
else:
    print("An error occurred while calculating the hash.")