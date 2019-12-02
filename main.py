txt = 'helllllllo'
def count(a, char):
    count = 0
    for i in a:
        if i == char:
            count += 1
    return count
print(count(txt, 'l'))