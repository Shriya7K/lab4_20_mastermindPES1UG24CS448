
def feedback(code, guess):
    exact = 0
    remaining_code = []
    remaining_guess = []

    # Count exact matches first.
    for actual, attempted in zip(code, guess):
        if actual == attempted:
            exact += 1
        else:
            remaining_code.append(actual)
            remaining_guess.append(attempted)

    # Count partial matches without reusing a code occurrence.
    partial = 0
    for symbol in remaining_guess:
        if symbol in remaining_code:
            partial += 1
            remaining_code.remove(symbol)

    return exact, partial
