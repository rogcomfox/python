a = int(input())
for b in range(a):
    b = input()
    for i in b:
        if b(chr(i)) == b(chr(-i)):
            print("Palindrom")
        else:
            print("Bukan")