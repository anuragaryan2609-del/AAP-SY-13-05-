#1.	Develop a Python script using regular expressions (regex) to find email patterns. 
import re
text = """
Contact us at support@example.com or admin@test.org.
You can also email student123@university.edu.
"""
pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(pattern, text)
print("Email addresses found:")
for email in emails:
    print(email)

#2.	Develop a Python script to identify and extract valid email addresses from a text file using regular expressions.
#Sample Text File: input.txt

#Welcome to our university.
#For technical support, contact support@example.com.
#The administration email is admin@university.edu.
#Invalid addresses:
#student@com
#user@.com

#For further information, contact info@gmail.com.


 
import re
filename = "input.txt"
pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
with open(filename, "r") as file:
    text = file.read()

emails = re.findall(pattern, text)
print("Valid email addresses found:")
for email in emails:
    print(email)

print("\nTotal email addresses:", len(emails))

