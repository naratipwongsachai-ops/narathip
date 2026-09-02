import random                         # * นำเข้า random เพื่อสุ่มตัวเลข

number = random.randint(1, 100)       # * สุ่มเลขตั้งแต่ 1 ถึง 100
guess = 0                             # * สร้างตัวแปรเก็บคำตอบของผู้เล่น
attempts = 0                          # * เก็บจำนวนครั้งที่ทาย

print("=== Guess the Number Game ===") # * แสดงชื่อเกม
print("I have chosen a number 1-100")  # * บอกผู้เล่นว่ามีเลขที่ถูกซ่อนไว้

while guess != number:                # * ทำซ้ำจนกว่าจะทายถูก

    guess = int(input("Guess: "))     # * รับตัวเลขจากผู้เล่น
    attempts += 1                     # * เพิ่มจำนวนครั้งที่ทาย 1 ครั้ง

    if guess < number:                # * ถ้าตัวเลขที่ทายน้อยกว่าคำตอบ
        print("Too low!")             # * บอกว่าเลขน้อยเกินไป

    elif guess > number:              # * ถ้าตัวเลขที่ทายมากกว่าคำตอบ
        print("Too high!")            # * บอกว่าเลขมากเกินไป

    else:                             # * ถ้าไม่มากกว่าและไม่น้อยกว่า แสดงว่าถูก
        print("Correct!")             # * แสดงว่าทายถูก
        print("Attempts:", attempts)  # * แสดงจำนวนครั้งที่ใช้