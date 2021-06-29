
# palindrome of a string

l = list()

def palindrome(str):
    if len(l) == 0:
        l.append(str)
    elif len(l) == 1:
        tmp = l.pop(0)
        first = str + tmp
        last = tmp + str
        l.append(first)
        l.append(last)
    else:
        ll = []
        for element in l:
            tmp = element
            first = str + tmp
            last = tmp + str
            ll.append(first)
            ll.append(last)

            for i in range(1, len(tmp)):
                new = tmp[:i] + str + tmp[i:]
                ll.append(new)

        l.extend(ll)

str = "abcde"

for i in range(len(str)):
    palindrome(str[i])

output = []

for i in l:
    if len(i) == len(str):
        output.append(i)

print(output)