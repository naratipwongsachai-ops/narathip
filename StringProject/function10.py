import re

def find_number(text):
    numbers = re.findall(r'\d+', text)

    if numbers:
        return "พบตัวเลข: " + ", ".join(numbers)
    else:
        return "ไม่พบตัวเลข"