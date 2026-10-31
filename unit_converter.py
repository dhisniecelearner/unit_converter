print("===== UNIT CONVERTER =====")

while True:

    print("""
1. Length

2. Weight

3. Temperature

""")

    choice = int(input("Enter your choice :"))

    if choice == 1:
        print("""Length conversion menu:

          a : Kilometres to Metres
          b : Metres to Centimetres
          c : Metres to Kilometres
""")

        selected_choice = input("Enter (a,b or c):")

        if selected_choice == "a":
            print("Kilometres to Metres\n")
            len_in_km = float(input("Enter the length in kilometers :"))
            len_in_m = 1000 * len_in_km
            print(f"Your length in meters is : {len_in_m}")

        elif selected_choice == "b":
            print("Metres to Centimetres\n")
            len_in_m = float(input("Enter the length in meters :"))
            len_in_cm = 100 * len_in_m
            print(f"Your length in centimeters is : {len_in_cm}")

        elif selected_choice == "c":
            print("Metres to Kilometres\n")
            len_in_m = float(input("Enter the length in meters :"))
            len_in_km = 0.001 * len_in_m
            print(f"Your length in kilometers is : {len_in_km}")

        else:
            print("Invalid conversion choice")

    elif choice == 2:
        print("""Weight conversion menu:

          a : Kilograms to Grams
          b : Grams to Kilograms
          c : Kilograms to Pounds
""")

        selected_choice = input("Enter (a,b or c):")

        if selected_choice == "a":
            print("Kilograms to Grams\n")
            weight_in_kg = float(input("Enter the weight in kilograms :"))
            weight_in_g = 1000 * weight_in_kg
            print(f"Your weight in grams is : {weight_in_g}")

        elif selected_choice == "b":
            print("Grams to Kilograms\n")
            weight_in_g = float(input("Enter the weight in grams :"))
            weight_in_kg = 0.001 * weight_in_g
            print(f"Your weight in kilograms is : {weight_in_kg}")

        elif selected_choice == "c":
            print("Kilograms to Pounds\n")
            weight_in_kg = float(input("Enter the weight in kilograms :"))
            weight_in_pounds = 2.20462 * weight_in_kg
            print(f"Your weight in pounds is : {weight_in_pounds}")

        else:
            print("Invalid conversion choice")

    elif choice == 3:
        print("""Temperature conversion menu:

          a : Celsius to Fahrenheit
          b : Fahrenheit to Celsius
          c : Celsius to Kelvin
""")

        selected_choice = input("Enter (a,b or c):")

        if selected_choice == "a":
            print("Celsius to Fahrenheit\n")
            temp_in_c = float(input("Enter temperature in Celsius :"))
            temp_in_f = (temp_in_c * 9/5) + 32
            print(f"Your temperature in Fahrenheit is : {temp_in_f}")

        elif selected_choice == "b":
            print("Fahrenheit to Celsius\n")
            temp_in_f = float(input("Enter temperature in Fahrenheit :"))
            temp_in_c = (temp_in_f - 32) * 5/9
            print(f"Your temperature in Celsius is : {temp_in_c}")

        elif selected_choice == "c":
            print("Celsius to Kelvin\n")
            temp_in_c = float(input("Enter temperature in Celsius :"))
            temp_in_k = temp_in_c + 273.15
            print(f"Your temperature in Kelvin is : {temp_in_k}")

        else:
            print("Invalid conversion choice")

    else:
        print("Invalid menu choice")

    repeat = input("\nDo you want to convert again? (yes/no):")

    if repeat.lower() != "yes":
        print("Thank you for using Unit Converter!")
        break
