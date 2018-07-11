# cropsModel

This Python class is designed to model simple crop yields.

**Methods:**

The Crop class is initialized with NFert for Nitrogen Fertilizer (int), irrigation (boolean) and 
rainAmt for the amount of rain received per month (float).

*rainfall*

Creates a single random float value from a gaussian distribution for rainfall amount centered at 50 cm with a standard deviation
of 20 cm. If a randomly generated number is below 0, the value is set to zero, because negative 
rainfall makes no sense. 
Does not return anything, only modifies the rainAmt variable initialized when the Crop object is created.

*Nloss*

Calls self.rainfall() to get the amount of rainfall.
Calculated the amount of nitrogen fertilizer left by subtracting the amount of nitrogen removed
by rainfall. The amount removed = rainAmt * 0.03.
Returns remaining nitrogen.

*cropYield* 

Call Nloss to find the amount of nitrogen fertilizer available.
Calculates the potential yield by adding rain amount to the nitrogen remained * 0.25. 
Returns yearYield as bushels per acre. 

*profit*

Assume $7 per bushel yield.  However, a loss of $10 for each cm below 
50 cm.  If irrigation is True, rainfall is supplemented up to 50 cm if it is 
below.  If rainfall is 50 cm or greater, no additional irrigation takes
place.
Returns grossProfit, not an object attribute

**Functions:**

*modelYield*

Takes NFert as an integer, Irrigation is set to False as default, cycles is set to 10,000.
Creates 10,000 crop objects and models the yield and profit for each.
It then creates a plot of the yield.

*modelProfit*

Models the profit for 10,000 iterations for both irrigated and non-irrigated.
Then, plots the predictions in four (2x2) subplot windows - histogram and boxplot for
each of the data sets.
