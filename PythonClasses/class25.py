"""
Flag - Mark a location
None = no value
is and is not = is or is not (type, value, indentity)
id = identity
"""

condition = True
pass_on_if = None

if condition:
    print('Does something')
    pass_on_if = True
else:
    print('Does nothing')

if pass_on_if is None:
    print("Didn't pass on the if")

if pass_on_if is not None:
    print('It passed the if')