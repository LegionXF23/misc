#1
def push(l,sp,x):
	l += [x]
	sp += 1
	return l,sp
def pop(l, sp):
    if sp > -1:  # Ensure the stack is not empty
        t = l[len(l) - 1]  # Get the last element
        l = l[0:len(l) - 1]  # Remove only the last element
        sp -= 1  # Decrease the stack pointer
        return l, sp, t
    return l, sp, None
#2
"""l = []
sp = -1
x = int(input("Enter a number:"))
y = int(input("Enter another number:"))
l,sp = push(l,sp,x)
l,sp = push(l,sp,y)
l,sp,t = pop(l,sp)
print("Popped out",t)"""

#3
"""x = input("Enter a string: ")
x = x.split()
l = []
sp = len(x) - 1
sp2 = -1

# Pop from x and push to l
for i in x:
    x, sp, t = pop(x, sp)
    if t is not None:
        l, sp2 = push(l, sp2, t)

# Build the final string
s = ' '.join(l)
print(s)"""
#4
'''def push(l, sp, x):
    l += [x]
    sp += 1
    return l, sp

def pop(l, sp):
    if sp > -1:
        t = l[len(l) - 1]
        l = l[0:len(l) - 1]
        sp -= 1
        return l, sp, t
    return l, sp, None

# Function to convert decimal to binary using stack
def decimal_to_binary(decimal_number):
    stack = []
    sp = -1

    # Edge case for 0
    if decimal_number == 0:
        return "0"

    # Convert decimal to binary by pushing remainders to stack
    while decimal_number > 0:
        remainder = decimal_number % 2
        stack, sp = push(stack, sp, remainder)
        decimal_number //= 2

    # Pop from stack to get the binary number
    binary_number = ""
    while sp > -1:
        stack, sp, bit = pop(stack, sp)
        binary_number += str(bit)

    return binary_number

# Input from the user
decimal_number = int(input("Enter a decimal number: "))
binary_result = decimal_to_binary(decimal_number)
print(f"The binary equivalent of {decimal_number} is: {binary_result}")'''
#5
'''# Define the stack and stack pointer
employee_stack = []
stack_pointer = -1  # Start with an empty stack

# Define the Employee data structure as a dictionary
def push(stack, sp, employee):
    stack.append(employee)
    sp += 1
    return stack, sp

def pop(stack, sp):
    if sp > -1:
        employee = stack[-1]  # Get the last employee
        stack = stack[:-1]  # Remove the last employee from the stack
        sp -= 1
        return stack, sp, employee
    else:
        return stack, sp, None  # Stack is empty

def hire():
    global employee_stack, stack_pointer
    name = input("Enter employee name: ")
    salary = float(input("Enter employee salary: "))
    employee = {"Name": name, "Salary": salary}
    employee_stack, stack_pointer = push(employee_stack, stack_pointer, employee)
    print(f"Employee {name} hired with salary {salary}.")

def fire():
    global employee_stack, stack_pointer
    employee_stack, stack_pointer, employee = pop(employee_stack, stack_pointer)
    if employee:
        print(f"Employee {employee['Name']} with salary {employee['Salary']} has been fired.")
    else:
        print("No employees to fire; the stack is empty.")

def main():
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Hire Employee")
        print("2. Fire Employee")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            hire()
        elif choice == '2':
            fire()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()'''
#6
'''# Initialize the stack and stack pointer
token_stack = []
stack_pointer = -1  # Start with an empty stack
current_token = 1   # Initial token number

# Define the functions for stack operations
def push(stack, sp, item):
    stack.append(item)
    sp += 1
    return stack, sp

def pop(stack, sp):
    if sp > -1:
        item = stack[-1]  # Get the last item
        stack = stack[:-1]  # Remove the last item from the stack
        sp -= 1
        return stack, sp, item
    else:
        return stack, sp, None  # Stack is empty

# Issue a token to a student
def issue_token():
    global token_stack, stack_pointer, current_token
    name = input("Enter student's name: ")
    token_entry = [current_token, name]
    token_stack, stack_pointer = push(token_stack, stack_pointer, token_entry)
    print(f"Token {current_token} issued to {name}.")
    current_token += 1  # Increment token for the next student

# Issue meals to 'n' students (pop 'n' items from the stack)
def issue_meal():
    global token_stack, stack_pointer
    n = int(input("Enter the number of students to serve meals to: "))
    
    if n > stack_pointer + 1:
        print(f"Only {stack_pointer + 1} students are in the stack. Serving all of them.")
        n = stack_pointer + 1

    for _ in range(n):
        token_stack, stack_pointer, student = pop(token_stack, stack_pointer)
        if student:
            print(f"Serving meal to {student[1]} with token {student[0]}.")
        else:
            print("No more students to serve.")

# Main program loop
def main():
    while True:
        # Display menu options
        print("\nMenu:")
        print("1. Issue a token")
        print("2. Issue meal")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            issue_token()
        elif choice == '2':
            issue_meal()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()'''




