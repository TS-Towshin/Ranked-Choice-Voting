from db import ballots

def count_ballots(ballots: list[list[str]]) -> dict[str, int]:
    '''
    Count the votes for all candidates
    '''
    status = {}
    for ballot in ballots:
        if len(ballot) == 0:
            continue
        first_choice = ballot[0]
        if first_choice in status:
            status[first_choice] += 1
        else:
            status[first_choice] = 1

    # Eliminate if no one's first choice
    for ballot in ballots:
        i = 0
        while i < len(ballot):
            if not ballot[i] in status:
                ballot.pop(i)
                i -= 1
            i += 1

    return status

def is_equal(status: dict[str, int]) -> list[str] | None:
    '''
    Check if votes from all the candidates are equal
    '''
    if len(set(status.values())) == 1:
        return list(status.keys())
    return
    

def major_candidate(status: dict[str, int]) -> list[str] | None:
    '''
    Check which candidates have more than 50% votes
    '''
    max_vote = max(status.values())
    voters = sum(status.values())
    if max_vote > voters/2:
        return [candidate for candidate, votes in status.items() if votes == max_vote]
    return

def elect_candidate(ballots: list[list[str]], visuals: bool = False) -> list[str]:
    status = count_ballots(ballots)
    if visuals:
        round = 1
        print(f"Round {round}:\n{status}")

    equal = is_equal(status)
    if equal:
        return equal

    while True:
        winner = major_candidate(status)
        if winner:          # Elect the person with more than 50% of the votes
            return winner
        if is_equal(status) or len(status) <= 1:
            return list(status.keys())

        min_vote = min(status.values())
        losers = [candidate for candidate, votes in status.items() if votes == min_vote]
        for loser in losers:
            for ballot in ballots:
                try:
                    ind = ballot.index(loser)
                    if ind == 0 and len(ballot) > 1:
                        next_in_line = ballot[ind+1]
                        if not (next_in_line) in losers:
                            status[next_in_line] += 1
                    del ballot[ind]
                except ValueError:
                    continue
            del status[loser]

        if visuals:
            round += 1
            print(f"Round {round}:\n{status}")



if __name__=='__main__':
    elected_candidates = elect_candidate(ballots, visuals=True)
    for i, winner in enumerate(elected_candidates):
        if i == 0:
            print(f"Elected: {winner}", end="")
        else:
            print(f", {winner}", end="")
