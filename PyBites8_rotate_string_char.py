
def rotate(word, displacement):
    n = displacement % len(word)
    # if n > 0: #hello, 3 = llo + he
    #     word = word[-n:] + word[:-n]
    # elif n < 0: #hello, -3 = lo + hel
    #     word = word[-n:] + word[:-n]
    return word[-n:] + word[:-n]

def test():
    tests = [('hello', 3, 'llohe'),
            ('hello', -3, 'lohel')]
    for word, displacement, answer in tests:
        print(answer)
        assert rotate(word, displacement) == answer

test()
# a = 'hello'
# print(a[])