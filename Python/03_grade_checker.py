# Mission

# Ask the user for a student's score.

# The score must be 0–100.

# If the user enters something outside that range, keep asking until they enter a valid score.

# Then determine:

# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# 0–59   → E

score = int(input("Masukan Nilai anda : " ))

while score < 0 or score > 100:
    print("Nilai anda invalid!")
    score = int(input("Masukan Nilai anda : " ))

    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")  
    elif score >= 70:
        print("C") 
    elif score >= 60:
        print("D") 
    else:
        print("E")