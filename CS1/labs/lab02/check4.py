first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

x = len(first_name) 
y = len(last_name) + 1
z = max(x,y,6)
numb = z+6

space_hnumb = z - 6
space_fnumb = z - x
space_lnumb = z - y

print('*'*numb)
print('** Hello,'+" " *space_hnumb, '**')
print("**",first_name+" "*space_fnumb,"**")
print("**",last_name+"!"+" "*space_lnumb,"**")
print('*'*numb)