<h1>Analyzing Leading Causes of Death in the U.S.</h1>
by Brian Rhodes, Cassandra Nellis, and Darren Barreto

<h3>Part 1: Locating and defining our Dataset:<h3>
<ul>
<li>The dataset used in this analysis was located by searching Google's web search engine for "public data", then navigating to data.gov and viewing their most popular datasets that were geographically relevant.</li>
<li>The dataset describes Age-Adjusted Death Rates for the Top 10 Leading Causes of Death in the United States (by state) over 17 years.</li>
<li>The dataset is metadata created by the National Center for Health Statistics (updated on 08/20/18). It was created using combined sources from DC/NCHS, National Vital Statistics System, mortality data, and CDC WONDER. We felt the data was reliable because it was created by a federal agency using various federal agencies' datasets.</li>
<li>The main variables involved in our dataset:
<ul>
<li>Year: from 1999-2016</li>
<li>Cause of Death:classified by the the International Classification of Diseases, Tenth Revision (ICD–10) and ranked according to the number of deaths assigned to each cause. Note that our dataset only includes the 10 most common of the 113 possible underlying causes of deaths defined by the ICD-10.</li>
<li>State: 50 US states and the District of Columbia</li>
<li>Number of Deaths: based on the number of resident death certificates filed</li>
<li>Age-adjusted Death Rate:Rate that controls for the effects of differences in population age distributions
rates (per 100,000 people) are based on Census U.S. standard population</li>
<ul>
</li>
<li>Our Questions and Hypotheses for analysis:
<ul>
<li> Question 1: How do North Carolina's death rates compare to the entire US?</li>
<li> Hypothesis 1: North Carolina has higher death rates than the US.</li>
<li> Question 2: How do death rates change over time?</li>
<li> Hypothesis 2: All death rates decrease over time.</li>
<li> Question 3: Are there regional differences in death rates?</li>
<li> Hypothesis 3: The South has a higher average death rate than other regions.</li>
</ul>
</li>

<h3> Part 2: Creating the project on Github <h3>
<ul>
<li>Created Github Repository</li>
<li>Uploaded Dataset</li>
<li>Created one jupyter notebook for data cleaning and another notebook for analysis</li>
<li>Created and updated issues in Github</li>
<li>Developed a plan for our general process and division of tasks in a google doc</li>
</ul>

<h3> Part 3: Cleaning the Data <h3>
<ul>
<li>1. import dependencies and read file</li>
<li>2. Ensure that "Deaths" and "age-adjusted rates" are numerical data types</li>
<li>3. Delete Detailed column about Cause of Death</li>
<li>4. Fourth, seperate the aggregate from non-aggregate Data</li>
<li>4a. Create dataframe for individual causes and individual states (across all 17 years)</li>
<li>4b. Create dataframe for individual causes and entire US (across all 17 years)</li>
<li>4c. Create dataframe for "all causes" and individual states (across all 17 years)</li>
<li>4d. Create dataframe for "all causes" and entire US (across all 17 years)</li>
</ul>

<h3>Part 4: Data Analysis</h3>
<ul>
<li>We imported the following modules for our analysis: using pandas, matplotlib, numpy and scipy.stats </li>
</ul>

Analysis Part 1: Looking at NC vs. USA causes of death in 2016
We first created a dataframe for each cause of death's percentage of total deaths for the entire USA, then we created a pie chart to visualize the data.
In [103]:
# calculate percentages for causes of death in USA in 2016
# Create and plot pie Chart for causes of death in USA in 2016

The pie chart emphasizes that Heart Disease and Cancer made up more than half of all USA deaths in 2016.
It's important to note that most USA deaths in 2016 were due to chronic, long-term illnesses rather than causes related to communicable diseases (like HIV/AIDS), malnutrition, or neonatal death. This alone can lead us to postulate that the USA is a more developed, higher-income country.
After that, we created a new dataframe and pie chart to look at each cause of death's percentage of total deaths for North Carolina.
In [104]:
# calculate percentages for causes of death in NC in 2016​
# Create and plot pie Chart to display causes of death in NC in 2016

The NC 2016 pie chart was extremely similar to the USA pie chart, specifically in that Cancer and Heart Disease are the main causes of death in both.
This suggests that there are no major discrepencies in health between NC and the entire USA.

Analysis Part 2: Change in Death Rates Over Time
For this part of the analysis, we created a connected scatter plot to Visualize Change in Total Death Rates in NC vs. USA over 17 Years
In [105]:
# create line graph to display change in NC and US total death rates over 17 years
 

The plot shows that death rates in both NC and the entire USA decreased over time (as expected). It also shows that the death rate in NC has been consistently a bit higher than the USA. Interestingly, there was a large decrease in the US between 2014-2016.

Specifically, morality in the USA decreased 42.14% between 1999 and 2016 and morality in NC decreased 19.25% between 1999 and 2016

Thus, while both death rates decreased over time, the death rate for the entire USA decreased about 20% more than North Carolina.

Based on the top 3 leading casues of death shown in the initial pie charts (and an interest in change in suicide rates), we created connected scatter plots for those specific causes of deaths over time





While Heart Disease and Cancer still accounted for more than half of the USA's causes of death in 2016, both appear to decrease over time. Unintentional injuries and suicide appear to slightly increase over time.
Further analysis is needed determine if the increases or decreases are statistically significant, but it is apparent that unintentional injuries and suicide did decrease in the same way that Cancer and Heart Disease did.

Analysis Part 3: Compare Regional Death for 2016
To visualize regional comparisons of all Death Rates, we created a bar chart and a boxplot.
We used the U.S. Census Bureau's regional classifications (source 3).
 


In [108]:
stats.f_oneway(group4, group4)
Out[108]:
F_onewayResult(statistic=0.0, pvalue=1.0)
In [109]:
stats.f_oneway(group1, group4)
Out[109]:
F_onewayResult(statistic=0.06216734699181595, pvalue=0.803940256239512)
In [110]:
stats.f_oneway(group2, group4)
Out[110]:
F_onewayResult(statistic=3.171595574428924, pvalue=0.08016611540091793)
In [111]:
stats.f_oneway(group3, group4)
Out[111]:
F_onewayResult(statistic=8.890991325889177, pvalue=0.004011235026270102)
In [112]:
stats.f_oneway(group5, group4)
Out[112]:
F_onewayResult(statistic=4.387165929330076, pvalue=0.040303790198210225)

The bar chart shows that the South had the highest regional average death rate in 2016, followed by the Midwest, the Northeast, and the West with the lowest average death rate of the four regions.

The boxplot reveals that the Midwest has the closest average AADR to the entire USA, and that the South is the least similar in 2016.
To visualize regional comparisons of Average Death Rates due to suicide in 2016, we created a bar chart and a boxplot.


To visualize regional comparisons of Suicide Death Rates, we created a bar chart and a boxplot.
We used the U.S. Census Bureau's regional classifications (source 3).



In [114]:
stats.f_oneway(group10, group40)
Out[114]:
F_onewayResult(statistic=0.018437992705091527, pvalue=0.892437121344818)
In [115]:
stats.f_oneway(group20, group40)
Out[115]:
F_onewayResult(statistic=3.937596483484301, pvalue=0.05195636841508142)
In [116]:
stats.f_oneway(group30, group40)
Out[116]:
F_onewayResult(statistic=1.1451781071385145, pvalue=0.2884588441692934)
In [117]:
stats.f_oneway(group50, group40)
Out[117]:
F_onewayResult(statistic=8.184393763227844, pvalue=0.005752079483635979)

The bar chart shows that the West had the highest AADR due to suicide, followed by Midwest, South, and the Northeast with the lowest AADR due to suicide.
The boxplot reveals that the Midwest has the closest average suicide AADR to the entire USA, and that the West is the least similar in 2016.


Part 5: Observations and Conclusions
Reflecting on initial Questions and Hypotheses:
1. How do North Carolina's death rates compare to the entire US?
Hypothesis: North Carolina has higher death rates than the US.
Conclusion: Overall, NC is similar to US in death rates (with both having more than half of deaths due to heart disease and cancer)
2. How do death rates change over time?
Hypothesis: All death rates decrease over time.
Conclusion: Overall, death rates appeared to decrease. However, certain causes like unintentional injuries and suicide appeared to have slightly increased. Overall death rates in the US appeared to decrease at a higher rate than NC since 1999, as well as remain lower than NC's overall death rate every year.
3. Are there regional differences in death rates?
Hypothesis: The South has a higher average death rate than other USA regions.
Conclusion: The South does have a slightly higher death rate. However, the West has a higher rate of suicides than other regions.


Part 6: Implications of our Analysis
Why does measuring death rates and death causes matter?
It helps to evaluate the effectiveness of the United States’s health system.
It helps to inform us where to focus public health policies, programs, and budgets.
For example: Because heart disease and cancer constitute over half of the leading causes of death in America and North Carolina, programs and policies that promote healthy lifestyles might be most beneficial in decreasing overall death rates (source 2).
Furthermore, the increase in death rates due to unintentional injuries and suicide, while constituting a smaller percentage of deaths, suggest the value of increased emphasis on safety policies and mental health services.
What could we do for future analysis?
Analyze death rates by other demographic areas such as age group, gender, race/ethnicity
Analyze cause of death rates of all countries (not just US)
Use current data to predict future death rates
Calculate if the changes seen over time are statistically significant


Sources:
National Center for Health Statistics. (2018). NCHS - Leading Causes of Death: United States [data file]. Available from Data.CDC.gov website: https://data.cdc.gov/NCHS/NCHS-Leading-Causes-of-Death-United-States/bi63-dtpu
Holland, K. (2017, August 24). What Are the 12 Leading Causes of Death in the United States? Retrieved October 14, 2018, from https://www.healthline.com/health/leading-causes-of-death#2
United States Census Bureau. (2015, July 28). Geography Atlas - Regions. Retrieved October 13, 2018, from https://www.census.gov/geo/reference/webatlas/regions.html
