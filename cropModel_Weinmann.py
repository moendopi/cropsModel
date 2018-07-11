import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import random, math


class Crop(object):
    '''Used to project yearly yield for a crop based on fertilizer and rainfall 
    inputs.'''
    
    def __init__(self, NFert, irrigation):
        self.NFert = NFert
        self.irrigation = irrigation
        self.rainAmt = 0
        
    
        
    def rainfall(self):
        '''returns an annual rainfall amount based on normal probability distribution.
        Average rainfall during growth period is 50 cm and a standard deviation of 20 cm 
        return self.rainAmt'''
        self.rainAmt = random.gauss(50, 20)
        #print("Rain amount: {} cm".format(self.rainAmt))
        if self.rainAmt < 0:
            self.rainAmt = 0
        

    def Nloss(self):
        '''Loss of N based on amount of rainfall that occurred.  For every cm of rain,
        3.0% loss of N occurs.
        Runs self.rainfall() to get self.rainAmt, returns an int of NAmt remaining based
        on yearly rainfall.  Int returned is not a object variable and does not replace
        self.NAmt'''
        self.rainfall()
        self.Nrem = self.NFert - (self.rainAmt * 0.03)
        return self.Nrem
        
        
    def cropYield(self):
        '''Predicts the yearly yield of a crop based on rainfall and fertilizer
        inputs.
        Average yield is 100 bushels per acre based on average rainfall and 200 kg/ha
        per year N fertility.  A very basic model was used to predict yield where
        yield = rainAmt + (0.25 * N amt in kg/ha).  Need to use NAmt after rainfall
        for calcualtion.  
        RETURN: self.yearYield which is the yield in bushels per acre'''
        self.Nloss()
        #print("Nitrogen remaining: {:.2f} kg".format(self.Nrem))
        self.yearYield = self.rainAmt + (0.25 * self.Nrem)
        #print("Yield: {} bushels".format(self.yearYield))
        return self.yearYield
        
        
    def profit(self):
        '''Assume $7 per bushel yield.  However, a loss of $10 for each cm below 
        50 cm.  If irrigation is True, rainfall is supplemented up to 50 cm if it is 
        below.  If rainfall is 50 cm or greater, no additional irrigation takes
        place.
        RETURN grossProfit, not an object attribute'''
        self.cropYield()
        self.loss = 0
        if self.irrigation == True:
            if self.rainAmt < 50:
                self.loss = 50 - self.rainAmt
            self.grossProfit = (7 * self.yearYield) - (self.loss * 10)
            return self.grossProfit
        else:
            self.grossProfit = 7 * self.yearYield
            return self.grossProfit


def modelYield(NFert, Irrigation = False, cycles = 10000):
    '''Model yield for 10,000 iterations and plot the yield in a histogram.'''
    crops = []
    for i in range(cycles):
        i = Crop(NFert, Irrigation)
        crops.append(i)
    
    yields = []
    
    for crop in crops:
        yearYield = crop.cropYield()
        yields.append(yearYield)
    sb.set()
    plt.hist(yields, bins = 20)
    plt.xlabel("Number of bushels (avg {:.2f}) in bins of 50".format(np.mean(yields)))
    plt.ylabel("Frequency of bushel amount")
    plt.title("Crop Yield Model (10,000 iterations)")
    plt.show()
    plt.savefig("cropModelYields_Weinmann.png", format='png', dpi=300)
    

modelYield(200)
 
def modelProfit(NFert, cycles=1000):
    '''Model profit for 10,000 iterations for both irrigated and non-irrigated.
    Plot the predictions in four (2x2) subplot windows - histogram and boxplot for
    each of the data sets.'''
    
    irrigated = []
    for i in range(cycles):
        i = Crop(NFert, True)
        irrigated.append(i)
    
    nonIrrigated = []
    for j in range(cycles):
        j = Crop(NFert, False)
        nonIrrigated.append(j)
        
    irrigatedProfits = []
    for field in irrigated:
        profit = field.profit()
        irrigatedProfits.append(profit)
    
    unIrrigatedProfits = []
    for field in nonIrrigated:
        profit = field.profit()
        unIrrigatedProfits.append(profit)
        
    sb.set()
    plt.subplot(221)
    plt.hist(irrigatedProfits, bins = 20)
    plt.xlabel("dollars per hectare with irrigation (avg ${:.2f})".format(np.mean(irrigatedProfits)))
    
    plt.subplot(222)
    plt.hist(unIrrigatedProfits, bins = 20)
    plt.xlabel("dollars per hectare with no irrigation (avg ${:.2f})".format(np.mean(unIrrigatedProfits)))
    
    plt.subplot(223)
    plt.boxplot(irrigatedProfits)
    plt.xlabel("dollars per hectare with irrigation")
    
    plt.subplot(224)
    plt.boxplot(unIrrigatedProfits)
    plt.xlabel("dollars per hectare with no irrigation")
    
    #plt.tight_layout()
    plt.show()
    plt.savefig("cropModelProfits_Weinmann.png", format='png', dpi=300)
    
    
modelProfit(200)

