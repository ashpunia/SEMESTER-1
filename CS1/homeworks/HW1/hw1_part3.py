
frame = str((input('Enter frame character ==> ')))
print(frame)
frame = frame.strip()

height = int(input('Height of box ==> '))
print(height)


width = int(input('Width of box ==> '))
print(width,'\n',sep='')

dimension = str(width) + 'x' + str(height)
emp_line = frame + ' ' * (width -2) + frame + ('\n')

bot_height = (height -2) // 2
up_height = (height - 2) - (bot_height + 1)
width_left = (width - (2 + len(dimension))) // 2
width_right = width - 2 - (width_left) - len(dimension)

print('Box:')
print(frame * width)
print((up_height) * emp_line, end = (''))
print(frame + width_left * ' ' + dimension + width_right * ' ' + frame)
print((bot_height) * emp_line, end = (''))
print(frame * width)