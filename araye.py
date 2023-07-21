n = int(input("tedad adad arye ra vared konid : "))
araye = []

for i in range(n):
    num = int(input("adady ra vared konid: "))
    while num in araye:
        print("adad gablan zade shode . lotfa adad digary vared konid.")
        num = int(input("Enter a number: "))
    araye.append(num)

print("Array:", araye)
