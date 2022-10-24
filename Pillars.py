def pillars(num_pill, dist, width):
    all_pillars_width = (num_pill - 2) * width
    all_distance_between = (num_pill - 1) * dist * 100
    if num_pill == 1:
        return 0
    else:
        return all_pillars_width + all_distance_between


if __name__ == '__main__':
    print(pillars(2, 20, 25))
    print(pillars(11, 15, 30))
    print(pillars(3, 15, 30))
