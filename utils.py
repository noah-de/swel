from utils import median


def calc_mid(series):
    notfirst = series[:,1:]
    notlast  = series[:,:-1]
    return .5 * (notlast + notfirst)
