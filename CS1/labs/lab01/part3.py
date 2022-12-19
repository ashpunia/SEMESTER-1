base10size = int(input("Disk size in GB => "))
print(base10size)
base2size = (base10size*10**9)//2**30
lost_size = base10size - base2size
print(int(base10size), "GB in base 10 is actually", int(base2size),"GB in base 2,",int(lost_size),"GB less than advertised.")
print("Input: ","*"*base10size)
print("Actual:", "*"*base2size)