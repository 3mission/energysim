# energysim
A simulator for assessing energy consumption distribution of infrastructure and Internet service. The simulator is suitable for any service, a case example is Online Advertising. Simulation is done for Python

## 1. Overview 

params.py provides input parameters for the simualtor. The main domains for parameters include infra_params, traffic_params, and ads_params. energysim.py contains the actual simulator and histogram settings. The simulation picks randomly input parametes for the simulation from the range of uncertainty. The number of possible permutations is billions. The histogram contains 200 bins in the default setup. All input paraters can be changed. 

### 1.1. About energysim

There are no well-established ways to assess the total power consumption of the Internet. Estimating the internet's energy footprint is challenging because the interconnectedness associated with even seemingly simple aspects of power consumption creates a problem. 
This simulator takes infrastructure energy consumption, shares of traffic from different access networks and CDNs, shares of protocols, shares of traffic classes, and finally shares of investigated service as input parameters. Then simulator computes tha energy consumption distribution for the service in question. The main phases in the simulator are: 1) infrastructure energy consumption estimation, 2) estimating traffic shares of access networks and CDNs, 3) estimating protocol shares, 4) estimating traffic class shares in different access networks, 5) estimating shares of online advertising in each traffic class in different access tecnologies, and 6) presenting the distribution of results.

## 2. Install and Use

### 2.1 Install 

to install: 

    pip install git+https://github.com/3mission/energysim.git
    
to import: 
    
    from energysim import energysim

to use:

    #### run the simulation with 10000 rounds
    result = energysim.energy(10000)

    #### plot a histogram for the result with 200 bins
    result.hist(bins=200)

    #### view the dataframe with the results 
    result.df

    #### get the mean value for ads TWh
    result.ads_mean

    #### get the mean value for infrastructure total TWh
    result.total_mean

    #### get the standard deviation for ads TWh
    result.ads_std

    #### get the standard deviation for infrastructure total TWh
    result.total_std

    #### get the median value for ads TWh
    result.ads_median

    #### get the median value for infrastructure total TWh
    result.total_median

    #### get the mode value for ads TWh
    self.ads_mode

    #### get the mode value for infrastructure total TWh
    self.total_mode

    #### get the minimum value for ads TWh
    result.ads_min

    #### get the minimum value for infrastructure total TWh
    result.total_min

    #### get the maximum value for ads TWh
    result.ads_max

    #### get the maximum value for infrastructure total TWh
    result.total_max

## 3. Parameters

### 3.1. Parameter Taxonomy

Parameter | Example Value | Uncertainty | Description
-------|---------|---------|---------
infra_params
ran | 140 | 0.2 | Mobile Radio Access Network energy consumption in TWh [1]
ps_core | 146.65 | 0.25 | Packet switched core network energy consumption in TWh [2]
fixed_line_cpe | 162.06 | 0.2 | Fixed Access CPE devices energy consumption in TWh [1]
operator_dc | 29.33 | 0.25 | Operator data center energy consumption in TWh [2]
office_networks | 49.67 | 0.25 | Office network energy consumption in TWh [3]
internet_core | 29.64 | 0.4 | The Internet core network energy consumption in TWh [4]
applications | 385.04 | 0.25 | Service data center energy consumption in TWh [5], [6]
smartphone_dev_millions | 2562 | 0.1 | The number of smartphone devices [7]
smartphone_avg_energy | 3.34 | 0.3 | Average smartphone energy consumption in kWh [8]
pc_dev_millions | 325 | 0.1 | The number of PC devices [9]
pc_avg_energy | 233 | 0.3 | Average PC energy consumption in kWh [10]
laptop_dev_millions | 548 | 0.1 | The number of laptop devices [1]
laptop_avg_energy | 41.8 | 0.3 | Average laptop energy consumption in kWh [10]
tablet_dev_millions | 742 | 0.1 | The number of tablet devices [11]
tablet_avg_energy | 12.9 | 0.3 |  Average tablet energy consumption in kWh [12]
traffic_params
fixed_ip | 0.6863 | 0.1 | The share of fixed network IP traffic of total traffic [13]
mobile_ip | 0.075 | 0.1 | The share of mobile network IP traffic of total traffic [13]
cdn_ip | 0.3992 | 0.1 | The share of CDN IP traffic of total traffic [13]
ipv4 | 0.985 | 0.005 | Share of IP version 4 traffic [14], [15]
tcp | 0.8977 | 0.05 | Share of TCP traffic [15]
http | 0.7420 | 0.1 | Share of HTTP [14]
fixed_video | 0.7284 | 0.1 | Share of video traffic class in fixed networks [13]
fixed_file | 0.1253 | 0.1 | Share of file sharing traffic class in fixed networks [13]
fixed_web | 0.1290 | 0.1 | Share of web, email, and data traffic class in fixed networks [13]
fixed_gaming | 0.0174 | 0.1 | Share of gaming traffic class in fixed networks [13]
mobile_video | 0.6148 |0.1 | Share of video traffic class in mobile networks [13]
mobile_file | 0.0049 | 0.1 | Share of file sharing traffic class in mobile networks [13]
mobile_web | 0.3801 | 0.1 | Share of web, email, and data traffic class in mobile networks [13]
mobile_gaming | 0.0002 | 0.1 | Share of gaming traffic class in mobile networks [13]
ads_params
fixed_video | 0.1 | 0.8 | Share of ads in video traffic class in fixed networks
fixed_of_file | 0.1 | 0.9 | Share of ads in file sharing traffic class in fixed networks
fixed_web | 0.5 | 0.5 | Share of ads in web, email, and data traffic class in fixed networks
fixed_gaming | 0.1 | 0.9 | Share of ads in gaming traffic class in fixed networks
mobile_video | 0.14 | 0.8 | Share of ads in video traffic class in mobile networks
mobile_file | 0.1 | 0.9 | Share of ads in file sharing traffic class in mobile networks
mobile_web | 0.5 | 0.5 | Share of ads in web, email, and data traffic class in mobile networks
mobile_gaming | 0.1 | 0.9 | Share of ads in gaming traffic class in mobile networks

## References

[1] Andrae, A. S., & Edler, T., 2015. On global electricity usage of communication technology: trends to 2030. Challenges, 6(1), 117-157.
[2] Han, C., Harrold, T., Armour, S., Krikidis, I., Videv, S., Grant, P. M., ... & Le, T. A., 2011. Green radio: radio techniques to enable energy-efficient wireless networks. IEEE communications magazine, 49(6).
[3] Lambert, S., Van Heddeghem, W., Vereecken, W., Lannoo, B., Colle, D., & Pickavet, M., 2012. Worldwide electricity consumption of communication networks. Optics express, 20(26), B513-B524.
[4] Taylor, C., & Koomey, J., 2008. Estimating energy use and greenhouse gas emissions of internet advertising. Network.
[5] Koomey, J., 2011 b. Growth in data center electricity use 2005 to 2010. A report by Analytical Press, completed at the request of The New York Times, 9.
[6] Whitehead, B., Andrews, D., Shah, A., & Maidment, G., 2014. Assessing the environmental impact of data centres part 1:
Background, energy use and metrics. Building and Environment, 82, 151-159.
[7] https://www.statista.com/statistics/371889/smartphone-worldwide-installed-base/
[8] https://www.canstarblue.com.au/energy/electricity/surprising-cost-charging-phone/
[9] https://www.statista.com/statistics/541339/worldwide-pc-market-installed-base-by-type/
[10] Van Heddeghem, W., Lambert, S., Lannoo, B., Colle, D., Pickavet, M., & Demeester, P., 2014. Trends in worldwide ICT electricity consumption from 2007 to 2012. Computer Communications, 50, 64-76.
[11] https://www.nakono.com/tekcarta/market-forecasts/tablets-installed-base/tablet-installed-base-by-os-worldwide/
[12] http://www.zdnet.com/article/how-much-does-it-cost-to-charge-an-iphone-for-a-year/
[13] https://www.cisco.com/c/en/us/solutions/collateral/service-provider/visual-networking-index-vni/complete-white-paper-c11-481360.html
[14] Czyz, J., Allman, M., Zhang, J., Iekel-Johnson, S., Osterweil, E., & Bailey, M. (2014, August). Measuring ipv6 adoption. In ACM SIGCOMM Computer Communication Review (Vol. 44, No. 4, pp. 87-98). ACM.
[15] Pujol, E., Richter, P., Chandrasekaran, B., Smaragdakis, G., Feldmann, A., Maggs, B. M., & Ng, K. C., 2014. Back-office web traffic on the internet. In Proceedings of the 2014 Conference on Internet Measurement Conference. pp. 257-270. ACM.
