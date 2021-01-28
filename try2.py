def hello_world():
    print('Hello world!')

hello = hello_world
hello()
#Hello world!

def higher_order(func):
    print('Получена функция {} в качестве аргумента'.format(func))
    func()
    return func

#rapper_function()
