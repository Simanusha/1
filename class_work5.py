# def fill_truck(weight_limit):
#
#         import random
#         total_boxes = 0
#         total_weight = 0
#         while(total_weight < weight_limit):
#             box_weight = random.randint (1,100)
#             free_space = weight_limit - total_weight
#             if free_space < box_weight:
#                 print ("Skipped box = %d" % box_weight)
#             total_weight = total_boxes + box_weight
#             total_boxes = total_boxes + 1
#             print ("Total weight = %d, num. of boxes = %d, last box = %d," % (total_weight, total_boxes, box_weight))

# def fill_truck_fixed(weight_limit, box_weight):
#     total_weight = 0
#     total_boxes = weight_limit // box_weight  #// целочисленное деление
#
#     for i in range (1, total_boxes + 1):
#         total_weight = total_weight + box_weight
#         print("Total weight = %d, num. of boxes = %d, last box = %d," % (total_weight, i, box_weight))
#
#
# # fill_truck(2000)
# fill_truck_fixed(2000, 50)

# def random_numbers(num_randoms):
#
#     import random
#     for i in range (num_randoms):
#         print (random.randint (0, 100))
#
# random_numbers(20)


def max_random_numbers(num_randoms, lower_limit, upper_limit):
    import random
    max_num = lower_limit
    for i in range(num_randoms):
        num = random.randint(lower_limit, upper_limit)
        print(num)
        if (num > max_num):
            max_num = num

    return max_num


def min_random_numbers(num_randoms, lower_limit, upper_limit):
    import random
    min_num = upper_limit
    for i in range(num_randoms):
        num = random.randint(lower_limit, upper_limit)
        print(num)
        if (num < min_num):
            min_num = num

    return min_num

max_num = max_random_numbers(5, 100, 150)
print ("Max num =", max_num)

min_num = min_random_numbers(5, 100, 150)
print ("Min num =", min_num)


