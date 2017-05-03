# lst = [x**3 for x in range(1,10)]
# print (lst)

# l = ['1','2','3']
# s = ",".join([str(x)for x in l])
# print (s)
#
# def foo (a, b):
#     print(a)
#     print(b)
# foo(2,3) #присваивание функции, передача параметров, позиционно или по имени


# lst = [2, 5, 9, 24, 15]
# def max_min_diff (lst):
#     min_value = min(lst)
#     max_value = max(lst)
#     diff = max_value - min_value
#     return diff
#
# diff = max_min_diff(lst)
# print (diff)


common_end = ([1,2,3],[7,3])
def same_elem (lst):
    first1 = 1
    first2 = 7
    for i in common_end(lst):
        if x in lst==0:
            return True
        else: