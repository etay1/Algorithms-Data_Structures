def toggle(d):
    if d == 'O':
        return 'C'
    if d == 'C':
        return 'O'

#Initialize vars
n = int(input("Enter a number\n"))
L = []

#Let's update our list to have n "C"'s
for i in range(n):
    L.append("C")
print(L)

#if the char at i if a factor of the ith iteration
# toggle i
for i in range(len(L)):
    if n%(i+1) == 0:
        L[i] = toggle(L[i])
print(L)
