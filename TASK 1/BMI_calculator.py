while True:
    weight_input = input("Enter your Weight in KGs: ")
    height_input = input("Enter your height in meters: ")

    if not weight_input.replace('.', '', 1).isdigit() or not height_input.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter a valid number.")
        continue

    weight = float(weight_input)
    height = float(height_input)

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        print(bmi)
        print("You are underweight")
    elif bmi < 24.9:
        print(bmi)
        print("You are HEALTHY !")
    elif bmi < 29.9:
        print(bmi)
        print("You are OVERweight, Get in shape.")
    elif bmi < 39.9:
        print(bmi)
        print("Your are Obese, Focus on your diet.")
    elif bmi < 40.0:
        print(bmi)
        print("Your are severely Obese. Consult a Doctor")

    break