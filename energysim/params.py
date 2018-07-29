def infra_params():

    p = {

        # connectivity
        'ran': [140, 0.2],
        'ps_core': [146.65, 0.25],
        'fixed_line_cpe': [162.06, 0.2],
        'operator_dc': [29.33, 0.25],
        'office_networks': [49.67, 0.25],
        'internet_core': [29.64, 0.4],
        'applications': [385.04, 0.25],

        # devices
        'smartphone_dev_millions': [2562, 0.1],
        'smartphone_avg_energy': [3.34, 0.3],
        'pc_dev_millions': [325, 0.1],
        'pc_avg_energy': [233, 0.3],
        'laptop_dev_millions': [548, 0.1],
        'laptop_avg_energy': [41.8, 0.3],
        'tablet_dev_millions': [742, 0.1],
        'tablet_avg_energy': [12.9, 0.3],
    }

    return p


def traffic_params():

    p = {

        # traffic shares
        'fixed_ip': [0.6863, 0.1],
        'mobile_ip': [0.075, 0.1],
        'cdn_ip': [0.3992, 0.1],

        # protocal
        'ipv4': [0.985, 0.005],

            'tcp': [0.8977, 0.05], # < subset of ipv4
            'http': [0.7420, 0.1], # < subset of tcp
    }

    return p


def traffic_params_triangular():

    p = {

    'fixed_video': [0.6984, 0.7284, 0.7584],   # subset of fixed
    'fixed_file': [0.0953, 0.1253, 0.1553],    # subset of fixed
    'fixed_web': [0.099, 0.1290, 0.1590],     # subset of fixed
    'fixed_gaming': [0, 0.0174, 0.0474],  # subset of fixed

    'mobile_video': [0.5848, 0.6148, 0.6448],  # subset of mobile
    'mobile_file': [0, 0.0049, 0.0349],   # subset of mobile
    'mobile_web': [0.3501, 0.3801, 0.4101],    # subset of mobile
    'mobile_gaming': [0, 0.0002, 0.0302],  # subset of mobile
    
    }

    return p


def ads_params():

    p = {
        # http breaks down to 'fixed' and 'mobile'

        'fixed_video': [0.1, 0.8],   # subset of fixed
        'fixed_file': [0.1, 0.9],    # subset of fixed
        'fixed_web': [0.5, 0.5],     # subset of fixed
        'fixed_gaming': [0.1, 0.9],  # subset of fixed

        'mobile_video': [0.14, 0.8],  # subset of mobile
        'mobile_file': [0.1, 0.9],    # subset of mobile
        'mobile_web': [0.5, 0.5],     # subset of mobile
        'mobile_gaming': [0.1, 0.9],  # subset of mobile
    }

    return p


def Smartphone_usage():
    # Return smartphone usage share relevant to service under assessment
    return 1

