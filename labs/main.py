def top_scorers(results):
    highest = max (score for name, score in results)
    winners = [name for name, score in results if score == highest]
    return tuple(sorted(winners))
    # TODO: find the highest score, collect all players who achieved it,
    # and return their names as a sorted tuple
    pass