echoes = [3, 6, 9, 12]

def predictNext(echoes):
    """
    Predicts the next value in a sequence based on the given echoes.

    Args:
        echoes (list): A list of numeric values representing the echoes.

    Returns:
        float: The predicted next value in the sequence.

    Raises:
        ValueError: If the length of the echoes list is less than 2.
    """
    if len(echoes) < 2:
        raise ValueError("At least two echoes are required to predict the next value in the sequence.")
    difference = echoes[1] - echoes[0]
    return echoes[-1] + difference


print(predictNext(echoes))