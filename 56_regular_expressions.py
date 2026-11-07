"""Program 56: Regular Expressions"""

import re

text = "Contact us at support@example.com or sales@example.org"
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)
phone_text = "Call 9876543210 for assistance."
phone = re.search(r"\b\d{10}\b", phone_text)

print("Email addresses:", emails)
print("Phone number:", phone.group() if phone else "Not found")
