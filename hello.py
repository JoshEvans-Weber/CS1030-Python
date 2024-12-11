def hello():    
    print('hello world!') #String output
    hello = []
    hello.append('hello')
    hello.append('world!')
    hello_world =' '.join(hello) #String output from joined list
    print(hello_world)
    hello_dict = {}
    hello_dict['1'] = 'hello'
    hello_dict['2'] = 'world!'
    print(hello_dict['1'], hello_dict['2']) #String output from dictionary values

def calculate(num1, num2, operation):
    if operation == 'add':
        return (num1 + num2)
    if operation == 'subtract':
        return (num1 - num2)
    if operation == 'divide':
        return f'{(str(num1 / num2)).split('.')[0]} remainder {num1 % num2}'
    if operation == 'mulitply':
        return (num1 * num2)
    
def calculator():
    num1 = int(input('enter the first number'))
    num2 = int(input('enter the next number'))
    operation = input('would you like to add, subtract, mulitply or divide?')
    if num1 == 0 or num2 == 0 and operation == 'divide':
        raise ZeroDivisionError('You cant divide by zero!')
    
    print(calculate(num1, num2, operation))

def word_length():
    word = (input('please enter a word!'))
    return len(word)



hello()

print(f'The length of your word is {word_length()}')

calculator()