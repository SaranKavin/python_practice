def is_armstrong_number(number):
	return sum(int(digit)**len(str(number)) for digit in str(number)) == number


# Example usage:
num = 153
if is_armstrong_number(num):
	print(f"{num} is an Armstrong number")
else:
	print(f"{num} is not an Armstrong number")
