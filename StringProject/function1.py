def find_text(text, keyword):
    if keyword in text:
        return f"พบคำว่า '{keyword}' ในข้อความ"
    else:
        return f"ไม่พบคำว่า '{keyword}'"