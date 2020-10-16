#sWAP cASE:
def swap_case(s):
    y = list()
    for l in s:
            if l.islower() == True:
                    y.append(l.upper())
            elif l.isupper() == True:
                    y.append(l.lower())
            else:
                y.append(l)
    y = ''.join(y)
    return y


#String Split and Join:
def split_and_join(line):
    line = line.split(" ")
    y = '-'.join(line)

    return y


#What's Your Name?
def print_full_name(a, b):
    print("Hello " + a + " " + b + "! You just delved into python.")


#Muations:
def mutate_string(string, position, character):
    string = list(string)
    string[position] = character
    string = ''.join(string)

    return string


#Find a String:
def count_substring(string, sub_string):
    x = 0
    for l in range(len(string)):
        if string[l:].startswith(sub_string):
            x += 1
    return x


#String Validators:
if __name__ == '__main__':
    s = input()

    alnum = alpha = digit = lower = upper = 'False'

    for i in s:
        if i.isalnum():
            alnum = 'True'
        if i.isalpha():
            alpha = 'True'
        if i.isdigit():
            digit = 'True'
        if i.islower():
            lower = 'True'
        if i.isupper():
            upper = 'True'

    print(alnum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)


#Text Alignment:
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


#Text Wrap:
import textwrap

def wrap(string, max_width):
    x = textwrap.fill(string,max_width)
    return x


#String Formatting:
def print_formatted(number):
    sp = len(bin(number)) - 2

    for i in range(1, int(number) + 1):
        l = []
        D = str(i)
        O = oct(i).replace('0o', '', 1)
        H = hex(i).replace('0x', '', 1).upper()
        B = bin(i).replace('0b', '', 1)

        print(D.rjust(sp), O.rjust(sp), H.rjust(sp), B.rjust(sp))


#Capitalize!
def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())

    return s