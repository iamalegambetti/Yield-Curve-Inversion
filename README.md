# yield_curve_inversion

<h1>!!! DISCLAIMER !!! 
In analyze_etfs.py change the path of data_directory with your own absolute/relative path. 
</h1>

<h1>
<bold>GOAL OF THE RESEARCH</bold>
</h1>

The goal of the research is to point out which stock sectors perform the best during and after an inversion of the yield curve, this curve showing the relationship between the interest rate and the time to maturity, known as the "term", of the debt for a given borrower in a given currency. 
A not superficial point to stress is that the yield curve is considered by most asset managers as a good predictor for recession. 

<h1> HOW IT WORKS </h1>
I selected the spread between 10 years treasury constant maturity bonds and the 2 year US Treasury constant maturity bonds to track the yield curve performance. To track the various sectors’ performances I selected the top 3 ETFs for market capitalization for each sector analysed after the 2000 comprised (when possible).
After downloading the Time Series for 33 ETFs for 11 industries: Materials, Financials, Consumer Discretionary, Consumer Staples, Energy, Healthcare, Utilities, Telecommunications, Industrials, Technology and Real Estate, I studied how the etfs linked to those industries performed during:
<ul>
  <li>The period during the yield curve inversion,</li>
  <li>The period after the yield curve inversion.</li>
</ul>

From 2000 to 2019 the yield curve inverted two times: the first one from February 2000 to December 2000 and the second one from March 2006 to May 2007.
For each inversion I try to point out which sectors performed the best.

<h3>
2000 Yield Curve Inversion Analysis  
</h3>

In the 2000 yield curve inversion 3 ETFs performed quite well both during (for the whole period of the inversion) and after 3 years of the inversion. I decided to select 3 years as a time span because it represents a sufficient amount of time to start formulating opinions, i.e the short-run converiging to the long-run.
The ETFs that performed with positive returns (Buy and Hold) at the start of each period analysed were: XLV (Healthcare), XLY (Consumer Discretionary), XLB (Materials). The returns (DURING, AFTER) where (15%, 10%), (30%, 23%) and (48%, 24%) respectively for each ETF. 

<h3>
2006/2007 Yield Curve Inversion Analysis
</h3>
During this yield curve inversion the 3 most remarkable ETFs that performed well both during and after the inversion were: VDE, XLE (Energy) and VAW (Materials). Their returns were (32%, 13%), (30%, 12%) and (35%, 3%) respectively.
After the inversion also these ETFs performed well: GDX (Materials) with a return of 48%, IBB and VHF (both Healthcare) with a return of 34% and 4% respectively.

  

During After Inversion.ipynb reflects the summary statistics of the research, pointing out the results of the goal of the project.

TO BE CONTINUED
