from quartil import find_Quartil

dataLen_odd1 = [2, 1, 3, 5, 4, 6, 7, 11, 9,
                10, 8, 20, 21, 55, 14, 32, 17]  # length 17
dataLen_odd2 = [2, 1, 3, 6, 5, 8, 7, 9, 11, 12, 13, 10,
                4, 2, 6, 9, 10, 21, 21, 34, 20, 11, 14]  # length 23

dataLen_even1 = [2, 3, 4, 1, 5, 7, 6, 9, 10, 8]  # length 14
dataLen_even2 = [12, 10, 8, 9, 6, 7, 11, 5, 3, 4, 2, 1]  # length 16

print("Quartil 1 2 3 from odd data length\n")
find_Quartil(dataLen_odd1)
print()
find_Quartil(dataLen_odd2)

print("\nQuartil 1 2 3 from even data length\n")
find_Quartil(dataLen_even1)
print()
find_Quartil(dataLen_even2)
