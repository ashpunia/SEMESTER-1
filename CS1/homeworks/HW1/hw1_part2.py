
m = input('Minutes ==> ')
print(m)
m = int(m)

s = input('Seconds ==> ')
print(s)
s = int(s)

mi = input('Miles ==> ')
print(mi)
mi = float(mi)

td = input('Target Miles ==> ')
print(td)
td = float(td)
print('')

a = int(round((((60*m)+s)/mi) // 60,2))
b = int((((60*m)+s)/mi) % 60)
print('Pace is',a,'minutes and',b,'seconds per mile.')

x = (s/3600)+(m/60)
print('Speed is',format((mi/x),'.2f'),'miles per hour.')

x1 = td/mi
x2 = x1*((60*m)+s)
x3 = int(x2//60)
x4 = int(x2%60)
print('Time to run the target distance of',format(td, '.2f'),'miles is',x3,'minutes and',x4,'seconds.')