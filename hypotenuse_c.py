import math

side_A = float(input("Give side A of a right-angled triangle: "))
side_B = float(input("Give side B of a right-angled triangle: "))

hypothenuse_c = round(math.sqrt(pow(side_A, 2) + pow(side_B, 2)),2)

print(f"The Hypothenuse of a Right-Angled Triangle is: {hypothenuse_c}")
