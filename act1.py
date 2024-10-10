def main():
    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if 10 <= age <= 20:
        print("Your age is within the valid range (10-20).")
    else:
        print("Your age is not within the valid range (10-20).")

if __name__ == "__main__":
    main()