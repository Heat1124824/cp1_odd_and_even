def odd_and_even(lst):
    odd = []
    even = []

    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return odd, even

def main():
    #num_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_lst = [2, 5, 6, 9, 12, 21, 24, 30, 42, 69]
    odd_lst, even_lst = odd_and_even(num_lst)
    print(odd_lst)
    print(even_lst)

if __name__ == '__main__':
    main()