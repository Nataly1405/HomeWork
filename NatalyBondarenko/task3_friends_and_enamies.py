friends = ['Ben', 'David', 'Sara', 'Steven', 'Monica', 'Luci', 'James']
enamies = ['Sara', 'Gregory', 'Ben', 'Lili', 'Tamara', 'Diana']

for friend in friends:

    if friend in enamies:
        print(f'{friend} we are not the friends anymore')
    elif friend == 'James':
        continue
    else:
        print(f'{friend} we are the best friends')
