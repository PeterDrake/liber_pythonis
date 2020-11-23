votes = [1, 2, 2, 1, 3, 1, 1, 2]
votes_for_1 = 0
for v in votes:
    if v == 1:
        votes_for_1 = votes_for_1 + 1
print(votes_for_1)