def points(games):
    points = 0
    for score in games:
        if score[0] > score[2]:
            points += 3
        if score[0] == score[2]:
            points += 1
        else:
            points += 0
    return points


if __name__ == '__main__':
    print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']))
