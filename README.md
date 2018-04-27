# Energy Sim

Simulator for approximating the energy consumption of the internet, and separately online advertising. Output in TWh.

## Installation

    pip install git+https://github.com/3mission/energysim.git
   
## Use

    from energysim import energysim
   
    # run the simulation with 10000 rounds
    result = energysim.energy(10000)
   
    # plot a histogram for the result with 100 bins
    result.hist(bins=100)
   
    # view the dataframe with the results 
    result.df
   
    # get the mean value for ads TWh
    result.ads_mean
   
    # get the mean value for total TWh
    result.total_mean
   
    # get the standard deviation for ads TWh
    result.ads_std
   
    # save the results to a file
    result.df.to_csv('output.csv', index=False)
