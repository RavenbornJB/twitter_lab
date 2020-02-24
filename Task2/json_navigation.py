# This file is part of Task 2. The others are Task 3.
import json


def navigate(jsn: object, depth: int = 0):
    """ object, int -> None

    This is a recursive function. It displays the contents of a JSON object
    and lets you get attributes from it.

    The function allows navigating through the object with ease.
    """
    if depth == 0:
        print("""\nType 'Back' to go back a level at any time,
or quit if you're at the top level.""")

    while True:
        if isinstance(jsn, dict):
            print("""
-----------------------------------------------------\n
This is a JSON object. This object has these attributes:
(type the name to see that attribute or 'Object' to see the whole object
, or 'Back' to go back a level)
""")
            for key in jsn.keys():
                print(key)
            ipt = input('\nAttribute: ')
            if ipt == 'Back':
                break
            elif ipt == 'Object':
                print(''.join(['\n', repr(jsn), '\n']))
            elif ipt in jsn.keys():
                navigate(jsn[ipt], depth = depth + 1)

        elif isinstance(jsn, list):
            ln = len(jsn)
            if ln == 0:
                print('\nThis in an empty list.')
                break
            print(f"""
----------------------------------------------------\n
This is an array.
(type a number between 0 and {ln - 1} to access the element
with that index or 'Array' to see the whole array
, or 'Back' to go back a level)
""")
            ipt = input('Index: ')
            if ipt == 'Back':
                break
            elif ipt == 'Array':
                print(''.join(['\n', repr(jsn), '\n']))
            elif ipt.isdigit() and 0 <= int(ipt) <= ln - 1:
                navigate(jsn[int(ipt)], depth = depth + 1)

        else:
            print(f"""
The value of this attribute is:
{jsn}""")
            break


if __name__ == "__main__":
    with open('Task2/twitter.json', 'r', encoding='utf-8') as f:
        json_object = json.load(f)
    navigate(json_object)