# This is a sample Python script.
op1 = float(input('Enter first operand: '));
op2 = float(input('Enter second operand: '));
print('Calculator Menu');
print('---------------');
print('1. Addition');
print('2. Subtraction');
print('3. Multiplication');
print('4. Division');
operation = int(input('Which operation do you want to perform? '));
if operation == 1 or operation ==2 or operation ==3 or operation ==4:
    if operation == 1:
        result = op1 + op2;
    elif operation == 2:
        result = op1 - op2;
    elif operation == 3:
        result = op1 * op2;
    elif operation == 4:
        result = op1 / op2;
    print('The result of the operation is '+str(result)+ '. Goodbye!')
else:
    print('Error: Invalid selection! Terminating program.');







