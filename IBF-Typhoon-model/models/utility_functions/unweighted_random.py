import secrets


def unweighted_random(y_train, y_test):
    options = y_train.value_counts(normalize=True)
    y_pred = secrets.SystemRandom().choices(population=list(options.index), k=len(y_test))
    return y_pred
