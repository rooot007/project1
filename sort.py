def insert_sort(a):
    '''insert'''
    N = len(a)
    for top in range (1, N):
        k = top
        while k>0 and a[k-1] > a[k]:
            a[k-1],a[k] = a[k],a[k-1]
            k -= 1

def choise_sort(a):
    N =len(a)
    for pos in range(0, N-1):
        for k in range(pos+1, N):
            if a[k] < a[pos]:
                a[k], a[pos] = a[pos], a[k]
def bubble_sort(a):
     N =len(a)
     for bypass in range (1, N):
         for k in range(0, N - bypass):
             if a[k] > a[k+1]:
                 a[k], a[k+1] = a[k+1], a[k]

def test_sort(sort_algorithm):
    print(sort_algorithm.__doc__)
    print("testcase #1 ", end="")
    a = [4,6,2,7,9,1]
    a_sorted = [1,2,4,6,7,9]
    sort_algorithm(a)
    print("ok" if a  == a_sorted else "Fail")

    print("testcase #2 ", end="")
    a = list(range(10,20)) + list(range(0,10))
    a_sorted = list(range(20))
    sort_algorithm(a)
    print("ok" if a == a_sorted else "Fail")

    print("testcase #3 ", end="")
    a = [4, 2, 5, 1, 2]
    a_sorted = [1, 2, 2, 4, 5]
    sort_algorithm(a)
    print("ok" if a == a_sorted else "Fail")

test_sort(insert_sort)
test_sort(choise_sort)
test_sort(bubble_sort)
