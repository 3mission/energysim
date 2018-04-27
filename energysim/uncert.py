import numpy as np

from .params import infra_params, traffic_params, ads_params


def _deviation(n, uncertainty):

    deviation = n * uncertainty
    min_value = n - deviation
    max_value = n + deviation

    return min_value, max_value


def _variations(p, values=200):

    for key in p.keys():
        range_values = _deviation(p[key][0], p[key][1])
        step = (range_values[1] - range_values[0]) / values
        out = np.arange(range_values[0], range_values[1], step)
        p[key].append(out)

    return p


def _random_pick(p):

    l = []
    for key in p.keys():
        round_value = np.random.choice(p[key][2])
        l.append(round_value)

    return l


def _rescaling(data):

    data = np.array(data)

    total_sum = sum(data)
    rescale_sum = total_sum - 1
    percent_shares = data / sum(data)
    rescaled = data - (percent_shares * rescale_sum)

    return list(rescaled)


def sim_infra():

    p = infra_params()
    p = _variations(p)
    out = _random_pick(p)

    return out


def sim_traffic():

    p = traffic_params()
    p = _variations(p)
    out = _random_pick(p)

    # rescaling fixed and mobile to total 100%
    out[-4:] = _rescaling(out[-4:])
    out[-8:-4] = _rescaling(out[-8:-4])

    return out


def sim_ads():

    p = ads_params()
    p = _variations(p)
    out = _random_pick(p)

    return out
