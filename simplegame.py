import random

# להגריל מספר אקראי בין 1 ל-10
number_to_guess = random.randint(1, 10)

# קבלת ניחוש מהמשתמש
guess = int(input("נחש מספר בין 1 ל-10: "))

# בדיקת הניחוש
if guess == number_to_guess:
    print("נכון! ניחשת את המספר!")
else:
    print(f"טעות! המספר הנכון היה {number_to_guess}. נסה שוב בפעם הבאה.")



    while True:
            user_input = input("הקלד 'דלוק' כדי להדליק את המנורה או 'כבה' כדי לכבות אותה (או 'צא' כדי לצאת): ").strip().lower()
            if user_input == "דלוק":
               turn_on_led()
            elif user_input == "כבה":
                 turn_off_led()
            elif user_input == "צא":
                  print("יציאה מהתוכנית.")
                break
            else:
                print("קלט לא תקין, נסה שוב.")  
