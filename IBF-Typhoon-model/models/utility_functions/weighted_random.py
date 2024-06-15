import secrets


def weighted_random(y_train, y_test):
    options = y_train.value_counts()
    y_pred = secrets.SystemRandom().choices(population=list(options.index), weights=list(options.values), k=len(y_test)
    )
    return y_pred
