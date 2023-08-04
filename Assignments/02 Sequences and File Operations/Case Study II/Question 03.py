"""
A website requires a user to input a username and password to register. 
Write a program to check the validity of the password given by the user. 
Following are the criteria for checking password:
	1. At least 1 letter between [a-z]
	2. At least 1 number between [0-9]
	3. At least 1 letter between [A-Z]
	4. At least 1 character from [$#@]
	5. Minimum length of transaction password: 6
	6. Maximum length of transaction password: 12
"""

def valid_password(password):
	"""Validates the password against given policy.

	Args:
		password (str): User password

	Returns:
		bool: True if passes all the policy checks else False
	"""    
	if not 6<= len(password) <= 12:
		return False
    
	password_policy = dict(
		has_digit=False,
		has_capital=False,
		has_small=False,
		has_specials=False
	)
	allowed_specials = "$#@"
    
	for char in password:
		# Putting it in first place because majority of characters in passwords are usually small characters
		# So, We will get benefit of reduced conditional checks.
		
		# Also, instead of using isdigit(), isalpha()... We are directly comparing ascii codes
		# So, We won't have any extra stack frames

		ascii_code = ord(char)
		if 97 <= ascii_code <= 122:
			password_policy["has_small"] = True
		elif 65 <= ascii_code <= 90:
			password_policy["has_capital"] = True
		elif 48 <= ascii_code <= 57:
			password_policy["has_digit"] = True
		elif char in allowed_specials:
			password_policy["has_specials"] = True
		else:
			return False
		
	return all(password_policy.values())


if __name__ == '__main__':
    password = input().strip()
    print("Valid:", valid_password(password))