# Kshitij Pingle & Ju Yeong Kim
# kpingle@csu.fullerton.edu
# 3 March, 2025
# Submission for CPSC 323 HW 2

def left_factorize(alpha, input):
    """
    Applies left factorization grammar technique for a given alpha and input

    Returns:
        str: The output of left factorization grammar
    """
    output = ""
    not_alpha = False

    for i in range(len(alpha)):
        if (alpha[i] != input[i]):
            # We have something else
            not_alpha = True
            break

    if (not not_alpha):
        # We have an alpha at the start
        output += "alpha"

        if (len(input) > len(alpha)):
            # We have a beta attached to the end
            output += " beta"
    else:
        # We have something different
        output += "gamma"
    
    return output


if (__name__ == "__main__"):
    test_1 = left_factorize("iEtS", "iEtS")
    test_2 = left_factorize("iEtS", "iEtSeS")
    test_3 = left_factorize("iEtS", "a")

    print(f"Output for test_1: {test_1}")
    print(f"Output for test_2: {test_2}")
    print(f"Output for test_3: {test_3}")