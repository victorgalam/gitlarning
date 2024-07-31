import time

  def turn_on_led():
      print("המנורה דולקת 💡")

  def turn_off_led():
       print("המנורה כבויה ⚫")

    def main():
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
