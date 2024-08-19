import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'\d', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])
    
    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Very Weak"
    }
    
    feedback = "Password Strength: " + strength_levels[criteria_met] + "\n"
    
    if not length_criteria:
        feedback += "- Your password should be at least 8 characters long.\n"
    if not uppercase_criteria:
        feedback += "- Your password should contain at least one uppercase letter.\n"
    if not lowercase_criteria:
        feedback += "- Your password should contain at least one lowercase letter.\n"
    if not number_criteria:
        feedback += "- Your password should contain at least one number.\n"
    if not special_criteria:
        feedback += "- Your password should contain at least one special character.\n"
        
    return feedback

password = input("Enter your password: ")
print(check_password_strength(password))
