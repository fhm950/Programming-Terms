# Example 1

a = 'fahim'
print(a)
print('Address of a is {}'.format(id(a)))

a = 'chowdhury'
print(a)
print('Address of a is {}'.format(id(a)))


# Example 2

employees = ['fahim', 'faha', 'farha', 'hridi', 'hritri', 'saifan']

output = '<ul>\n'

for employee in employees:
    output += '\t<li>{}</li>\n'.format(employee)
    print('Address of employee is {}'.format(id(output)))

output += '</ul>'

print(output)
