import re

def password_strength(password):
    length = len(password)
    uppercase = any(char.isupper() for char in password)
    lowercase = any(char.islower() for char in password)
    numbers = any(char.isdigit() for char in password)
    special_chars = bool(re.match('[\W_]', password))

    score = length * 4
    if uppercase:
        score += 10
    if lowercase:
        score += 10
    if numbers:
        score += 10
    if special_chars:
        score += 10

    if length < 8:
        feedback = "Password is too short"
    elif score < 40:
        feedback = "Weak password"
    elif score < 70:
        feedback = "Moderate password"
    elif score < 100:
        feedback = "Strong password"
    else:
        feedback = "Very strong password"

    return feedback

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    print("Password strength:", strength)

if __name__ == "__main__":
    main()
