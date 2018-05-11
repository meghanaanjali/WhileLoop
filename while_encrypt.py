a = "Iron"
b = ""
val = 0
while val < len(a) :
    b = b + (chr(ord(a[val])+1))
    val = val + 1
print (b)    