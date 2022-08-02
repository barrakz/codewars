def likes(name):
    if len(name) == 0:
        return []
    elif len(name) == 1:
        return f'{name} likes this'
    elif len(name) == 2:
        return f'{name[0]} and {name[1]} like this'
    elif len(name) == 3:
        return f'{name[0]}, {name[1]} and {name[2]} like this'
    else:
        return f'{name[0]} and {len(name) - 1} others like this'






if __name__ == '__main__':
    print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
    print(likes([]))
