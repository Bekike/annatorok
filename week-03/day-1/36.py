ah = [3, 4, 5, 6, 7]
# print the sum of all numbers in ah

i = 0
summa = 0

while i < len(ah):
    summa = summa + ah[i]
    i += 1

print(summa)


# for i in range(len(ah)):
#     summa += ah[i]
#     i += 1

for szam in ah:
    summa = summa + szam

print(summa)
