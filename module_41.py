def test_function():
    def inner_function():
        print('in inner_function Я')
    print('in test_function y =', y)
    inner_function()


y = 59
test_function()
print('Я =', y)


def inner_function():
    print('in inner_function Я')


inner_function()














