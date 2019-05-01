#!/usr/bin/python3
for value in range(1, 80):
    if (int(str(value).zfill(2)[1]) - int(str(value).zfill(2)[0])) > 0:
        print('{}'.format(str(value)).zfill(2), end=', ')
print('89')
