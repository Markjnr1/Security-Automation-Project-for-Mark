# Security-Automation-Project-for-Mark
Building a Password Strength Analyzer Tool: Detecting Common Attack Techniques

Overview
The Password Strength Analyzer Tool is written in Python and analyzes input passwords for weaknesses and poor password practices that attackers commonly exploit.

Objectives
Identify passwords that would easily be cracked with basic attacks
Education about secure passwords
Simple example of security automation using Python

Features
Identifies short passwords
Identifies commonly used passwords (“123456”, “password”, and others)
Identifies passwords that are just numbers
Identify passwords made of repeating characters

Displays
Security score (0–100)
Strength rating (Strong / Moderate / Weak)
Actionable feedback for found issues

Technologies
Written in Python 3.12exe

Run Program
https://github.com/Markjnr1/Security-Automation-Project-for-Mark
python password_strength_analyzer_Code.py

Sample Results
Decide strength level
Score >= 80
Strength: Strong
Score >= 50
Strength: Moderate
Score 0-49    
Strength: Weak

Issues Detected:
Password is too short.

AI tool used
I used GitHub Copilot to assist me with coding this project. All code suggestions were reviewed and understood before implementation. It helped me debug and simplify my code.


"""
Building a Password Strength Analyzer Tool: Detecting Common Attack Techniques

This program is designed to assess a password's strength by checking it against several common security vulnerabilities that attackers often exploit. The tool evaluates the password based on the following criteria:
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
