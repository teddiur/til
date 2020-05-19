import random
import matplotlib.pyplot as plt
import matplotlib

writedata = True

def write_data(n):
    with open('unsorted_list.txt', 'w') as datafile:
        for _ in range(n):
            datafile.write("%i\n" %random.randint(0, 1000))
def load_data():
    return [number.strip('\n') for number in open('unsorted_list.txt', 'r').readlines()]

if writedata:
    write_data(100)

def bubble_sort(L):
    print('Bubble sorting iniatialized')
    L1 = L[:]
    for n in range(len(L)):
        print("%i elements sorted" %n, end=" ")
        for m in range(0, len(L)-n-1):
            if L1[m] > L1[m+1]:
                L1[m], L1[m+1] = L1[m+1], L1[m]
    return L1

def insertion_sort(L):
    
    
""" plotting"""
numbers_uns = load_data()
bubble = bubble_sort(numbers_uns)
insert = insertion_sort(numbers_uns)
assert bubble == insert
# plt.figure(1)
# # plt.plot(numbers_sor, 'r.')
# plt.plot(bubble, 'g.')
# plt.locator_params(axis='y', nbins=4)
# plt.show()


