def sum_of_intervals(intervals):
    sum = 0
    for item in intervals:
        count = item[1] - item[0]
        sum += count

    return sum




def main():
    """ This is the main routine for the program """
    print("Starting the sequence:")
    print(sum_of_intervals([(1, 5)]), 4)
    print(sum_of_intervals([(1, 5), (6, 10)]), 8)
    print(sum_of_intervals([(1, 5), (1, 5)]), 4)
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)
    print(sum_of_intervals([[1,2],[6, 10],[11, 15]] ), 9)
    print(sum_of_intervals([[1,4],[7, 10],[3, 5]]), 7)
    print(sum_of_intervals([[1,5], [10, 20], [1, 6], [16, 19], [5, 11]] ), 19)


if __name__ == '__main__':
    main()
