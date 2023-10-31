def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


def main():
    try:
        print("Name:Gopika Unnikrishnan\nRoll No:22MCA030\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\nDate:03/10/2023")
        number = int(input("Enter a positive number: "))

        if number <= 0:
            print("Please enter a positive number.")

            return

        while number > 0:
            digit_sum = sum_of_digits(number)

            print(f"{number} - {digit_sum} = {number - digit_sum}")

            number = number - digit_sum

    except ValueError:

        print("Invalid input. Please enter a valid positive number.")


if __name__ == "__main__":
    main()

