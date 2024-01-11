""" Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers. """

if __name__ == '__main__':
    a = int(input('Enter the first number \n'))
    b = int(input('Enter the second number \n'))
    
    result = a + b;
    print("The sum of two numbers are", result)
    result = a - b;
    print("The difference of two numbers are", result)
    result = a * b;
    print("The product of two numbers are", result)