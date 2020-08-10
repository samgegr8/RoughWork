import random

# saturday Lotto Samples


historical_numbers = [
    6,
    9,
    16,
    32,
    37,
    44,
    11,
    12,
    1,
    18,
    21,
    22,
    35,
    43,
    10,
    37,
    22,
    26,
    27,
    29,
    32,
    38,
    30,
    42,
    17,
    31,
    33,
    35,
    39,
    42,
    36,
    41,
    15,
    19,
    24,
    28,
    35,
    41,
    23,
    30,
    9,
    11,
    17,
    19,
    22,
    29,
    14,
    21,
    3,
    17,
    29,
    32,
    34,
    38,
    12,
    28,
    3,
    10,
    18,
    19,
    22,
    27,
    41,
    42,
    3,
    15,
    19,
    22,
    27,
    41,
    42,
    3,
    15,
    19,
    22,
    25,
    44,
    1,
    42,
    1,
    21,
    25,
    30,
    31,
    45,
    31,
    38,
]

churn_numbers = {}
for num in historical_numbers:
    if num in churn_numbers:
        churn_numbers[num] += 1
    else:
        churn_numbers[num] = 1
print(f"Churned numbers are ::{churn_numbers}")

final_numbers = []

for k, v in churn_numbers.items():
    if v >= 3:
        final_numbers.append(k)

print(f"Final numbers are ::{final_numbers}")

for i in range(1, 13):
    print(f"Combination : {i} Random numbers are ::{random.sample(final_numbers,6)}")

