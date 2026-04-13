import string

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1

    # Lowercase check
    if any(char.islower() for char in password):
        score += 1

    # Numbers check
    if any(char.isdigit() for char in password):
        score += 1

    # Special characters check
    if any(char in string.punctuation for char in password):
        score += 1

    # Result
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength


# Run program
password = input("Enter a password to test: ")
print("Password strength:", check_password_strength(password))
