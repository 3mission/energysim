# energysim
A simulator for assessing energy consumption distribution of infrastructure and Internet service. The simulator is suitable for any service, a case example is Online Advertising. Simulation is done for Python

## 1. Overview 

params.py provides input parameters for the simualtor. The main domains for parameters include infra_params, traffic_params, and ads_params. energysim.py contains the actual simulator and histogram settings. The simulation picks randomly input parametes for the simulation from the range of uncertainty. The number of possible permutations is billions. The histogram contains 200 bins in the default setup. All input paraters can be changed. 

### 1.1. About energysim

There are no well-established ways to assess the total power consumption of the Internet. Estimating the internet's energy footprint is challenging because the interconnectedness associated with even seemingly simple aspects of power consumption creates a problem. 
This simulator takes infrastructure energy consumption, shares of traffic from different access networks and CDNs, shares of protocols, shares of traffic classes, and finally shares of investigated service as input parameters. Then simulator computes tha energy consumption distribution for the service in question. 

## 2. Install and Use

### 2.1 Install 

to install: 

    pip install git+https://github.com/3mission/energysim.git
    
### 2.2. Use
from energysim import energysim

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
ran | 140 | 0.2 | Mobile Radio Access Network energy consumption in TWh [1]
revenue | 30000 | 100 | revenue per delivery [2]
resource | 8500 | 100 | cost of resource per delivery [1]
core_change | 0.5 | 100 | maximum annual change of deliverable [1]
core_incertainty | 1 | 100 | level of incertainty [1]
core_steps | 30 | 100 | number choices between minimum and maximum [1]
revenue_change | 0.2 | 100 | max annual change of revenue [1]
revenue_incertainty | 1 | 100 | level of incertainty [1]
revenue_steps | 100 | 100 | number choices between minimum and maximum [1]
resource_change | 0.2 | 100 | max annual change of resouce cost [1]
resource_incertainty | 0.2 | 100 | level of incertainty [1]
resource_steps | 10 | 100 | number choices between minimum and maximum [1]
sales_salary | 96000 | 100 | annual salary per sales person [1]
production_salary | 75000 | 100 | annual salary per production person [1]
manager_salary | 132000 | 100 |  annual salary per manager [1]
service_salary | 96000 | 100 | annual salary per service person [1]
admin_salary | 60000 | 100 | annual salary per admin person [1]
core_per_sales | 10 | 100 | number deliverables a sales person can handle [1]
core_per_production | 5 | 100 | number of deliverables a production person can handle [1]
core_per_manager | 50 | 100 | number of deliverables a manager can handle [1]
core_per_service | 20 | 100 | number of deliverables a service person can handle [1]
core_per_admin | 200 | 100 | number of deliverables an admin person can handle [1]
salaries_change | 0.05 | 100 | max annual change in sales [1]
salaries_incertainty | 0.1 | 100 | level of incertainty [1]
salaries_steps | 10 | 100 | number choices between minimum and maximum [1]
employer_liabilities | 0.45 |100 | extra costs in addition to salaries [1]
employer_misc | 0.03 | 100 | other employer costs [1]
marketing_cost | 0.1 | 100 | marketing cost as a factor of revenue [1]
other_cost | 0.1 | 100 | other business costs [1]
tax_rate | 0.21 | 100 | the tax rate the business is subject to [1]
number_of_years | 10 | 100 | number of years to model [1]
depreciation_years | 10 | 100 | how many years to depreciate investment [1]
capital_investment | 100000 | 100 | initial investment into the business [1]
rate_of_return | 0.1 | 100 | the rate of return (ROR) [1]
risk_factor | 2 | 100 | a factor effects the likeliness of change to be negative [1]
core_static | False | 100 | cores are same every year if True [1]
revenue_static | False | 100 | revenue is same every year if True [1]
resource_static | False | 100 | resource is same every year if True [1]

## References

[1] Andrae, A. S., & Edler, T., 2015. On global electricity usage of communication technology: trends to 2030. Challenges, 6(1), 117-157.
[2] https://hbr.org/2014/11/a-refresher-on-net-present-value
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
[2]
