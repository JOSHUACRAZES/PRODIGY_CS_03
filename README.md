PRODIGY_CS_03 PASSWORD COMPLEXITY CHECKER

A Password Complexity Checker is a tool or program designed to evaluate the strength of a password based on various criteria. These criteria typically include factors such as length, the presence of different types of characters (uppercase letters, lowercase letters, numbers, and special characters), and the overall complexity of the password.

The Password Complexity Checker analyzes the input password against these criteria and provides feedback on its strength. This feedback often comes in the form of qualitative assessments (e.g., weak, moderate, strong, very strong) or quantitative scores. The purpose of this tool is to help users create passwords that are resilient against unauthorized access attempts, such as brute-force attacks or dictionary attacks.

TOOL OBJECTIVE : 
   1 --> Function password_strength(password):
        This function takes a password as input and calculates its strength based on several criteria: length, presence of uppercase and lowercase letters, numbers, and special characters.
        It first calculates the length of the password using len(password).
        It then checks whether the password contains at least one uppercase letter, lowercase letter, number, and special character using built-in methods like .isupper(), .islower(), .isdigit(), and a regular expression bool(re. match('[\W_]', password)).
        Based on these criteria, it assigns a score to the password. Each criterion contributes to the score, with uppercase and lowercase letters, numbers, and special characters adding more points.
        It then categorizes the password based on its score into different strength levels: weak, moderate, strong, and very strong.

  2 --> Function main():
        This function is the entry point of the program.
        It prompts the user to enter a password using input("Enter your password: ").
        It then calls the password_strength function with the user-entered password and prints out the feedback on the password's strength.

  3 --> Execution:
        When the program is run, it prompts the user to enter a password.
        After the user enters a password, the program calculates its strength using the password_strength function.
        Finally, it prints out feedback on the password's strength based on the calculated score.

  Feedback:
        The feedback provided includes:
            "Password is too short" if the password does not meet the minimum length requirement.
            "Weak password" if the score falls below a certain threshold.
            "Moderate password" if the score indicates moderate strength.
            "Strong password" if the score indicates strong strength.
            "Very strong password" if the score indicates very strong strength.
