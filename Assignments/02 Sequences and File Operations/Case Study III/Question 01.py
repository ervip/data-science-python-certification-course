"""
Domain:
    Telecom

focus:
    Optimization

Business challenge/requirement:
    LifeTel Telecom is the latest entrant in the highly competitive Telecom market of 
    Singapore. It issues SIM to the verified users. Till now verification was manual 
    through the photocopy of the approved id card document. However, the government 
    has recently introduced a Social ID called Reference ID which is mapped to the 
    fingerprint of the user. LifeTel should now verify the user against the fingerprint and 
    Reference ID

Key issues:
    Build a system where when a user enters Reference ID it is encrypted so that hackers 
    cannot view the mapping of Reference ID and fingerprint

Considerations:
    The system should be secure

Data volume:
    NA

Additional information:
    NA

Business benefits:
    The company will be able to quickly issue SIM to the user and the expected gain in 
    volume is approximately 10 times as the manual process of verification is replaced 
    with a secure automated system

Approach to Solve:
    You must use the fundamentals of Python taught in module 1
        1. Read the input from the command line: Reference ID
        2. Check for validity: it should be 12 digits and allows for number and alphabet
        3. Encrypt the Reference ID and print it for reference

Enhancements for code
    You can try these enhancements in code
        1. Allow some special characters in ReferenceID
        2. Give the option for decryption to the user 
"""

"""
Note:
    There are many fantastic libraries available for encryption / decryption purpose.
    Here, I have not used any external libraries just to keep it simple and portable.
    SO, DO NOT USE THIS IN REAL WORLD PROJECTS.
"""

def valid_ref_id(ref_id):
    return len(ref_id) == 12 and ref_id.isalnum()


def encrypt_ref_id(ref_id, key):
    if not valid_ref_id(ref_id):
        return "Invalid Reference ID"
    
    ref_id = ref_id.lower()
    alphabets = "0123456789abcdefghijklmnopqrstuvwxyz"
    encrypted_ref_id = ""
    
    for letter in ref_id:
        new_position = (alphabets.find(letter) + key) % len(alphabets)
        encrypted_ref_id += alphabets[new_position]
    
    return encrypted_ref_id


def decrypt_red_id(encrypted_ref_id, key):
    if not valid_ref_id(encrypted_ref_id):
        return "Invalid Reference ID"

    encrypted_ref_id = encrypted_ref_id.upper()
    alphabets = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    decrypted_ref_id = ""

    for letter in encrypted_ref_id:
        new_position = (alphabets.find(letter) - key) % len(alphabets)
        decrypted_ref_id += alphabets[new_position]

    return decrypted_ref_id


if __name__ == '__main__':
    print("Welcome to Reference ID Encryption / Decryption Utility")
    while True:
        choice = int(input((
            "Here are available options:\n"
            "\t1. Encrypt Reference ID\n"
            "\t2. Decrypt Reference ID\n"
            "\t3. Exit\n"
            "Enter Your Choice :\n"
        )))
        if choice == 1:
            ref_id = input("Enter Reference ID: ")
            key = int(input("Enter your secret number: "))
            print("Encrypted Reference ID:", encrypt_ref_id(ref_id, key))

        elif choice == 2:
            encrypted_ref_id = input("Enter your encrypted Reference ID: ")
            key = int(input("Enter your secret number: "))
            print("Decrypted Reference ID:", decrypt_red_id(encrypted_ref_id, key))
        
        elif choice == 3:
            print("By, See you soon ;)")
            exit(0)
        
        else:
            print("Invalid Choice: Please enter correct choice !!")