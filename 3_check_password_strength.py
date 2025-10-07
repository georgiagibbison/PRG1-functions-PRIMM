def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")
    
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain uppercase letters")
    
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should contain lowercase letters")
    
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain numbers")
    
    return score, feedback

# Test passwords
passwords = ["hello", "Hello123", "PASSWORD", "MyPass123!"]
special_chars=[".", ",", "!", "@", "?", "/", "£", "&", "*"]
for pwd in passwords:
    score, issues = check_password_strength(pwd)
    print(f"'{pwd}': Score {score}/4")

    for issue in issues:
        print(f"  - {issue}")
    if score<=1:
            print("Password is Weak")
    elif score == 2 or score == 3:
        print("Password is Medium")
    elif score >= 3:
        print("Password is strong")
    for char in pwd:
        if char in special_chars:
            print("Valid")
        else:
            print("Invalid")

print()