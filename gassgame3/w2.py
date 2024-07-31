import random

# רשימת מילים לניחוש
words = ["תפוח", "בננה", "כתום", "תות", "אבטיח"]

# בחירת מילה אקראית מהרשימה
word_to_guess = random.choice(words)

# קבלת ניחוש מהמשתמש
guess = input("נחש את המילה (תפוח, בננה, כתום, תות, אבטיח): ")

# בדיקת הניחוש
if guess == word_to_guess:
    print("נכון! ניחשת את המילה!")
else:
    print(f"טעות! המילה הנכונה הייתה {word_to_guess}. נסה שוב בפעם הבאה.")
