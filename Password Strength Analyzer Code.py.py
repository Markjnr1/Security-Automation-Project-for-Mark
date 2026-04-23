"""
Password Strength Analyzer Tool Detecting Common Attack Techniques

This program is designed to analyze the strength of a password by checking it against several common security vulnerabilities that attackers often exploit. The tool evaluates the password based on the following criteria:
1. Short length
2. Common password match
3. Number-only password
4. Simple repeated characters
"""

from getpass import getpass


def analyze_password(password):
    issues = []
    score = 100

    # 1. Check length
    if len(password) < 8:
        issues.append("Password is too short.")
        score -= 25

    # 2. Check common passwords
    common_passwords = ["password", "123456", "qwerty", "admin", "welcome"]
    if password.lower() in common_passwords:
        issues.append("Password is a common password.")
        score -= 30

    # 3. Check if password uses only numbers
    if password.isdigit():
        issues.append("Password uses only numbers.")
        score -= 20

    # 4. Check repeated characters
    if len(set(password)) == 1:
        issues.append("Password uses repeated characters only.")
        score -= 25

    # Decide strength level
    if score >= 80:
        strength = "Strong"
    elif score >= 50:
        strength = "Moderate"
    else:
        strength = "Weak"

    return score, strength, issues


def main():
    print("Password Strength Analyzer Tool Detecting Common Attack Techniques")
    password = getpass("Enter a password: ")

    score, strength, issues = analyze_password(password)

    print("\n--- Password Analysis Result ---")
    print(f"Score: {score}/100")
    print(f"Strength: {strength}")

    if issues:
        print("Detected Issues:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No major problems detected.")


if __name__ == "__main__":
    main()
