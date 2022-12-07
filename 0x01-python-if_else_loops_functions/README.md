## 0x01-python-if_else_loops_functions

## Task

0. Positive anything is better than negative nothing

	- [0-positive_or_negative.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/0-positive_or_negative.py): This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.

	- You can find the source code [here](https://alx-intranet.hbtn.io/rltoken/rkvoXPA-lS3TAaemM9sChg)
	- The variable `number` will store a different value every time you will run this program
	- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code
	- The output of the program should be:
		- The number, followed by
			- if the number is greater than 0: `is positive`
			- if the number is 0: `is zero`
			- if the number is less than 0: `is negative`
		- followed by a new line

1. The last digit

	- [1-last_digit.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/1-last_digit.py): This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

	- You can find the source code [here](https://alx-intranet.hbtn.io/rltoken/hU682hcMxVchqWAcmh32tA)
	- The variable `number` will store a different value every time you will run this program
	- You don’t have to understand what `import`, `random.randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000, 10000)`
	- The output of the program should be:
		- The string `Last digit of`, followed by
		- the number, followed by
		- the string `is`, followed by the last digit of `number`, followed by
			- if the last digit is greater than 5: the string `and is greater than 5`
			- if the last digit is 0: the string `and is 0`
			- if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
		- followed by a new line

2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game

2-print_alphabet.py: Python program that prints the alphabet in lowercase, not followed by a new line.
Using only one print and one loop.
Without storing characters in variables or importing modules.
3. When I was having that alphabet soup, I never thought that it would pay off

3-print_alphabt.py: Python program that prints the alphabet in lowercase, followed by a new line.
Using only one print and one loop.
Without storing characters in variables or importing modules.
Prints every letter except for q and e.
4. Hexadecimal printing

4-print_hexa.py: Python program that prints all numbers from 0 to 98 in decimal and hexadecimal.
Using only one print and one loop.
Without storing numbers or strings in variables or importing modules.
Printing format: [decimal] = [hexadecimal]
5. 00...99

5-print_comb2.py: Python program that prints numbers from 0 to 99 two digits each.
Numbers are separated by , , except for the last number, which is followed by a new line.
Using no more than two print functions and one loop.
Without storing numbers or strings in variables or importing modules.
6. Inventing is a combination of brains and materials. The more brains you use, the less material you need

6-print_comb3.py: Python program that prints all possible different combinations of two digits in ascending order.
Numbers are separated by , , except for the last number, which is followed by a new line.
The two digits must be different - 01 and 10 are considered identical.
Using no more than three print functions and two loops.
Without storing numbers or strings in variables or importing modules.
7. islower

7-islower.py: Python function that checks for lowercase characters.
Returns True if c is lowercase, False otherwise.
Without importing modules or using str.upper() or str.isupper().
8. To uppercase

8-uppercase.py: Python function that prints a string in uppercase followed by a new line.
Using no more than two print functions and one loop.
Without importing modules or using str.upper() or str.isupper().
9. There are only 3 colors, 10 digits, and 7 notes; its what we do with them that's important

9-print_last_digit.py: Python function that prints the last digit of a number.
Returns the value of the last digit.
Without importing modules.
10. a + b

10-add.py: Python function that returns the addition of two integers.
Without importing modules.
11. a ^ b

11-pow.py: Python function that returns a to the power of b.
Without importing modules.
12. Fizz Buzz

12-fizzbuzz.py: Python function that prints the numbers from 1 to 100 followed by a space.
For multiples of three, Fizz is printed instead of the number.
For multiples of five, Buzz is printed instead of the number.
For multiples of three and five, FizzBuzz is printed instead of the number.
Without importing modules.
13. Insert in sorted linked list

13-insert_number.c: C function that inserts a number into a sorted linked list.
If the function fails, returns NULL.
Otherwise, returns the address of the new node.
Helper files:
linked_lists.c: C functions handling linked lists for testing 13-insert_number.c (provided by Holberton School).
lists.h: Header file containing definitions and prototypes for all types and functions used in linked_lists.c and 13-insert_number.c.
14. Smile in the mirror

100-print_tebahpla.py: Python program that prints the alphabet in reverse order, alternating lowercase and uppercase, not followed by a new line.
Using only one print and one loop.
Without storing characters in variables or importing modules.
15. Remove at position

101-remove_char_at.py: Python function that creates a copy of a string without the character at position n.
Without importing modules.
16. ByteCode -> Python #2

102-magic_calculation.py: Python function matching exactly a bytecode provided by Holberton School.
