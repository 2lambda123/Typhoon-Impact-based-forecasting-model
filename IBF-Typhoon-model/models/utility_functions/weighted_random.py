import secrets


def weighted_random(y_train, y_test):
    """Generate weighted random predictions based on the distribution of
    y_train.

    It generates random predictions for the test set y_test based on the
    weighted distribution of the training set y_train.

    Args:
        y_train (pandas Series): The target values of the training set.
        y_test (pandas Series): The target values of the test set.

    Returns:
        list: A list of randomly generated predictions for the test set.
    """

    options = y_train.value_counts()
    y_pred = secrets.SystemRandom().choices(population=list(options.index), weights=list(options.values), k=len(y_test)
    )
    return y_pred
