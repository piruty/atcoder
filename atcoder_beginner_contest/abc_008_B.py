n = int(input())

people = []
votes = []

max_vote = 0
for i in range(n):
    name = input()
    if not name in people:
        people.append(name)
        votes.append(1)
        if max_vote == 0:
            max_vote = 1
    else:
        index = people.index(name)
        votes[index] += 1
        if votes[index] > max_vote:
            max_vote = votes[index]

print(people[votes.index(max_vote)])
