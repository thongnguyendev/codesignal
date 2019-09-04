def electionsWinners(votes, k):
    _max = max(votes)
    w = 0 if k == 0 else len([x for x in votes if x + k > _max])
    return w if w > 0 else 0 if votes.count(_max) > 1 else 1
