## Python - Hello, World

## Tasks

0. Run Python File

	[0-run](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/0-run): Bash script that runs a Python script file saved in the environment variable `$PYFILE`.

1. Run inline

	- [1-run_inline](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/1-run_inline): Bash script that runs Python code saved in the environment variable `$PYCODE`.

2. Hello, print

	- [2-print.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/2-print.py): Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line using the function print.

3. Print integer

	- [3-print_number.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/3-print_number.py): Python script that prints the integer stored in the variable number, followed by `Battery street`, followed by a new line.
Completion of this source [code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py).

4. Print float [4-print_float.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/4-print_float.py): 
	- Python script that prints the float stored in the variable number with a precision of two digits.
	- Completion of this source [code](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py).

5. Print string [5-print_string.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/5-print_string.py): 
	- Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable str, followed by its first 9 characters.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py)
	- The output of the program should be:
		- 3 times the value of `str`
		- followed by a new line
		- followed by the 9 first characters of `str`
		- followed by a new line
	- You are not allowed to use any loops or conditional statement
	- Your program should be maximum 5 lines long

6. Play with strings : [6-concat.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/6-concat.py): 

	- Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py)
	- You are not allowed to use any loops or conditional statements.
	- You have to use the variables `str1` and `str2` in your new line of code
	- Your program should be exactly 5 lines long

7. Copy - Cut - Paste [7-edges.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/7-edges.py): 

	- Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
	- You are not allowed to use any loops or conditional statements
	- Your program should be exactly 8 lines long
	- `word_first_3` should contain the first 3 letters of the variable `word`
	- `word_last_2` should contain the last 2 letters of the variable `word`
	- `middle_word` should contain the value of the variable `word` without the first and last letters.

8. Create a new sentence: [8-concat_edges.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/8-concat_edges.py): 
	- Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py)
	- You are not allowed to use any loops or conditional statements
	- Your program should be exactly 5 lines long
	- You are not allowed to create new variables
	- You are not allowed to use string literals

9. Easter Egg: [9-easter_egg.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/9-easter_egg.py): 

	- Write a Python script that prints `“The Zen of Python”`, by TimPeters, followed by a new line.
	- Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

10. Linked list cycle: [10-check_cycle.c](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/10-check_cycle.c): 
Technical interview preparation:

	- You are not allowed to google anything
	- Whiteboard first
	- This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.

Write a function in C that checks if a singly linked list has a cycle in it.
	- Prototype: `int check_cycle(listint_t *list)`;
	- Return: `0` if there is no cycle, `1` if there is a cycle
Requirements:
	- Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`
	- [lists.h](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/list.h): Header file containing definitions and prototypes for all types and functions used in `linked_lists.c` and `10-check_cycle.c`.

11. Hello, write: [100-write.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/100-write.py): 
	- Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line.
	- Use the function `write` from the `sys` module
	- You are not allowed to use `print`
	- Your script should print to `stderr`
	- Your script should exit with the status code `1`

12. Compile: [101-compile](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/101-compile): 
	- Write a script that compiles a Python script file.
	- The Python file name will be stored in the environment variable `$PYFILE`
	- The output filename has to be `$PYFILEc` (ex: `export PYFILE=my_main.py` => output filename: `my_main.pyc`)

13. ByteCode -> Python #1: [102-magic_calculation.py](https://github.com/Callistus25/alx-higher_level_programming/blob/master/0x00-python-hello_world/102-magic_calculation.py): 
	- Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
	- Tip: [Python bytecode](https://alx-intranet.hbtn.io/rltoken/B38QeZHREbvgq-wY7Ze3vQ)
