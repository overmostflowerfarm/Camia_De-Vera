try:
    score = int(input("Enter examination score: "))
    print("Valid score: ", score)

except ValueError:
    print("Invalid score. Enter a whole number.")