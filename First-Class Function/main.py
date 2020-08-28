# Example 1

def square(x):
    return x * x

f = square(5)

print(square)
print(f)


# Example 2

def square(x):
    return x * x

def cube(x):
    return x * x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)


# Example 3

def logger(msg):

    def log_message():
        print('Log:', msg)
        
    return log_message

log_hi = logger('hi')
log_hi()


# Example 4

def html_tag(tag):

    def wrap_text(text):
        print("<{0}>{1}</{0}>".format(tag, text))

    return wrap_text

tag_h1 = html_tag('h1')
tag_h1("This is a h1 text")

tag_p = html_tag('p')
tag_p("This is a paragraph")