import numpy as np
import pandas as pd
import astetik as ast

from .uncert import sim_infra, sim_traffic, sim_ads
from .params import *


class energy():

    def __init__(self, rounds, df=False):

        self.rounds = rounds
        self.results = self._sim_full()
        self.df = self._create_df(self.results)

        # creating the numeric outputs
        self.ads_mean = self.df.ad_total_twh.mean()
        self.ads_median = self.df.ad_total_twh.median()
        self.ads_std = self.df.ad_total_twh.std()
        self.total_mean = self.df.total_twh.mean()
        self.ads_std = self.df.total_twh.std()

        # cleaning up the namespace
        del self.infra_totals
        del self.infra_total
        del self.rounds
        del self.infra_result
        del self.traffic_result
        del self.ads_result

    def hist(self, bins=5):

        '''HISTOGRAM PLOT VISUALIZATION'''

        ast.hist(self.df, 'ad_total_twh', bins=bins, x_limit=None,
                 title='Online Advertising',
                 sub_title='Consumption in TWh')

        ast.hist(self.df, 'total_twh', bins=bins, x_limit=None,
                 title='Total Consumption')

    def _uncertainty(self):

        '''PICKING THE ROUND VALUES'''

        self.ads_result = sim_ads()
        self.traffic_result = sim_traffic()
        self.traffic_index = traffic_params().keys()
        self.infra_result = sim_infra()
        self.infra_totals = self._infra_totals()
        self.infra_total = self.infra_totals.sum()

        return

    def _ads_stack(self, mode=None):

        '''AD TRAFFIC TYPE PER CLASS (video, games, etc)'''

        out = []

        if mode == 'fixed':
            temp = self.ads_result[:4]
        elif mode == 'mobile':
            temp = self.ads_result[4:]

        out.extend(temp)

        return out

    def _traffic_stack(self, mode=None):

        '''TRAFFIC TYPE PER CLASS (video, games, etc)

        '''

        out = []

        if mode == 'fixed':
            temp = self.traffic_result[6:10]
        elif mode == 'mobile':
            temp = self.traffic_result[10:14]

        out.extend(temp)

        return out

    def _protocol_stack(self):

        '''PROTOCOL STACK SHARE (%)'''

        return self.traffic_result[3] * self.traffic_result[4] * self.traffic_result[5]

    def _cdn(self, mode):

        if mode == 'fixed':
            mode = 3
        elif mode == 'mobile':
            mode = 10

        total_traffic = (self.traffic_result[3] + self.traffic_result[10])
        share = self.traffic_result[mode] / total_traffic
        out = self.traffic_result[mode] - (share * self.traffic_result[0])

        return out

    def _mobile_labels(self):
        mobile_labels = ['ran', 'smartphone', 'operator_dc',
                         'internet_core', 'applications', 'ps_core']
        return mobile_labels

    def _fixed_labels(self):
        fixed_labels = ['ps_core', 'fixed_line_cpe', 'operator_dc',
                        'office_networks', 'internet_core',
                        'applications', 'pc', 'laptop', 'tablet']
        return fixed_labels

    def _infra_totals(self):

        # compute total values
        smartphone_total = self.infra_result[7] * self.infra_result[8] / 1000
        pc_total = self.infra_result[9] * self.infra_result[10] / 1000
        laptop_total = self.infra_result[11] * self.infra_result[12] / 1000
        tablet_total = self.infra_result[13] * self.infra_result[14] / 1000

        # drop compute values
        self.infra_result = self.infra_result[:7]

        # add totals
        computed_values = []
        computed_values.append(round(smartphone_total, 2))
        computed_values.append(round(pc_total, 2))
        computed_values.append(round(laptop_total, 2))
        computed_values.append(round(tablet_total, 2))
        self.infra_result.extend(computed_values)

        # create the labels
        labels = list(infra_params().keys())[:7]
        labels.extend(['smartphone', 'pc', 'laptop', 'tablet'])

        return pd.Series(self.infra_result, index=labels)

    def _create_df(self, out):

        df = pd.DataFrame(out)
        df.columns = ['ad_total_twh', 'total_twh']

        return df

    def _sim_full(self):

        output = []

        for i in range(self.rounds):

            self._uncertainty()

            out = np.array([0, 0, 0, 0])

            for label in self._mobile_labels():
                temp = self._twh_totals(self.infra_totals, label, mode='mobile')
                out = np.vstack([out, temp])

            for label in self._fixed_labels():
                temp = self._twh_totals(self.infra_totals, label, mode='fixed')
                out = np.vstack([out, temp])

            ads_out = out.sum()
            output.append([ads_out, self.infra_total])

        return output

    def _twh_totals(self, data, col, mode):

        if col in ['ps_core', 'operator_dc', 'applications']:
            special_class = col
        else:
            special_class = None

        out = self._sim_sub(data[col], mode, special_class)

        return np.array(out)

    def _sim_sub(self, value, mode, special_class=None):

        out = []

        ad_traffic = self._ads_stack(mode=mode)
        traffic = self._traffic_stack(mode=mode)
        traffic_result = pd.Series(self.traffic_result, index=self.traffic_index)

        for i in range(4):

            if special_class in ['ps_core', 'operator_dc', 'applications']:
                value = traffic_result[mode + '_ip'] * self.infra_totals[special_class]

            elif special_class is 'internet_core':
                value = self._cdn(mode) * self.infra_result[5] * traffic_result[mode + '_ip']

            # compute values
            temp = value * self._protocol_stack() * ad_traffic[i] * traffic[i]

            out.append(temp)

        return out
