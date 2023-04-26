import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from filtered_dataset import filter_muon
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--data', default='muon.data',type=str)
args = parser.parse_args()
dataset = args.data
# Read the data file into a numpy array
#datasets= ['5hrdata.data','23-03-24-15-22.data','23-03-27-14-56.data','23-03-28-14-52.data','23-03-29-15-04.data','23-04-03-14-43.data','23-04-18-00-43.data','23-04-18-11-43.data','23-04-19-11-03.data']

#datasets= ['5hrdata.data','23-03-24-15-22.data']

filtered = filter_muon(dataset)
data = np.loadtxt(filtered)
events=len(data)
#data.iloc[:, 0] /= 1000
# Define the exponential function to fit the data
def exponential(x, A, tau):
    return A * np.exp(-x / tau)

# Define the bin edges for the histogram
bin_edges = np.arange(0, 23, 0.9)

# Plot the histogram of the data
n, bins, patches = plt.hist(data/1000, bins=bin_edges, alpha=0.5, density=True)

# Fit the data to the exponential function using curve_fit
p0 = [1, 22] # initial guess for fitting parameters
popt, pcov = curve_fit(exponential, bins[:-1], n, p0=p0)

# Plot the fitted curve
x = np.linspace(0, 30, 1000)
y = exponential(x, *popt)
plt.plot(x, y, 'r-', label=f'Fit: $y = {popt[0]:.5f} e^{{-x/{popt[1]:.3f}}}$')

# Calculate the chi-squared value of the fit
chi2 = np.sum((exponential(bins[:-1], *popt) - n) ** 2 / exponential(bins[:-1], *popt))
ndof = len(bins) - len(popt)
chi2_red = chi2 / ndof



# Add the chi-squared value to the plot
plt.text(0.8,0.8,r'Total Events = {:d}'.format(events), ha='right', va='top', transform=plt.gca().transAxes,bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))
plt.text(0.8,0.7,r'$\tau$={:3f} $\mu$s'.format(popt[1]), ha='right', va='top', transform=plt.gca().transAxes,bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))

plt.text(0.8, 0.6, r'reduced $\chi^2$ = {:3f}'.format(chi2_red), ha='right', va='top', transform=plt.gca().transAxes,bbox=dict(facecolor='white', edgecolor='black', boxstyle='round'))

# Add a legend and axis labels
plt.legend()
plt.xlabel('Muon decay time ($\mu$ s)')
plt.title('Muon Decay Time Histogram')
plt.ylabel('Counts (normalized)')

# Show the plot
plt.savefig('{}.png'.format(dataset))
with open('output_{}.txt'.format(dataset),'w') as f:
    print('the number of events in each bin is:\n ',file=f)    
    print(n,file=f)
    print("\n the parameters are: \n",file=f)
    print(*popt,file=f)
    print('\n $\chi ^{2}$ :',file=f)
    print(chi2,file=f)
    print("\n the number of bins: ",file=f)
    print(ndof,file=f)

