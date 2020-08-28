# formula:
# f(f(x)) == f(x)

# Example: Not Idempotence
# add_num(add_num(10)) = 30 | add_num(10) = 20
def add_num(num):
    return num + 10

print(add_num(add_num(10)))


# Example: Idempotence
# No matter how many time you call abs function it won't change the result
print(abs(abs(-10)))


# HTTP Methods:
# GET ==> Idempotence
# POST ==> Not Idempotence
# PUT ==> Idempotence
# DELETE ==> Idempotence