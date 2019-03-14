<h1>Analyzing Leading Causes of Death in the U.S.</h1>
by Brian Rhodes, Cassandra Nellis, and Darren Barreto
<br>
<br>
<i>(original repository located <a href="https://github.com/CaNellis/UNCC_Project1">here</a>)</i>
<br>
<h3>Part 1: Locating and defining our Dataset:</h3>
<ul>
<li>The dataset used in this analysis was located by searching Google's web search engine for "public data", then navigating to data.gov and viewing their most popular datasets that were geographically relevant. 
  <ul>
  <li> It describes Age-Adjusted Death Rates for the Top 10 Leading Causes of Death in the United States (by state) over 17 years.</li> 
  <li>The dataset is metadata created by the National Center for Health Statistics (updated on 08/20/18).</li>
  <li>It was created using combined sources from DC/NCHS, National Vital Statistics System, mortality data, and CDC WONDER.</li> 
  <li>We felt the data was reliable because it was created by a federal agency using various federal agencies' datasets.</li>
  </ul>
 </li>
<li>The main variables involved in our dataset:
<ul>
<li>Year: from 1999-2016</li>
<li>Cause of Death:classified by the the International Classification of Diseases, Tenth Revision (ICD–10) and ranked according to the number of deaths assigned to each cause. Note that our dataset only includes the 10 most common of the 113 possible underlying causes of deaths defined by the ICD-10.</li>
<li>State: 50 US states and the District of Columbia</li>
<li>Number of Deaths: based on the number of resident death certificates filed</li>
<li>Age-adjusted Death Rate:Rate that controls for the effects of differences in population age distributions
rates (per 100,000 people) are based on Census U.S. standard population</li>
</ul>
</li>
<br>
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

<h3> Part 2: Creating the project on Github </h3>
<ul>
<li>Created Github Repository</li>
<li>Uploaded Dataset</li>
<li>Created one jupyter notebook for data cleaning and another notebook for analysis</li>
<li>Created and updated issues in Github</li>
<li>Developed a plan for our general process and division of tasks in a google doc</li>
</ul>

<h3> Part 3: Cleaning the Data </h3>
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
<br>
We imported and utilized pandas, matplotlib, numpy, and scipy.stats for our analysis.
<br>
  
<h4> Analysis Part 1: Looking at NC vs. USA causes of death in 2016</h4>
<ul>
<li>We first created a dataframe for each cause of death's percentage of total deaths for the entire USA in 2016, then we created a pie chart to visualize the data.The pie chart emphasized that Heart Disease and Cancer made up more than half of all USA deaths in 2016.
It's important to note that most USA deaths in 2016 were due to chronic, long-term illnesses rather than causes related to communicable diseases (like HIV/AIDS), malnutrition, or neonatal death. This alone can lead us to postulate that the USA is a more developed, higher-income country.</li>
<li>After that, we created a new dataframe and pie chart to look at each cause of death's percentage of total deaths for North Carolina in 2016.The NC 2016 pie chart was extremely similar to the USA pie chart, specifically in that Cancer and Heart Disease are the main causes of death in both.This suggests that there are no major discrepencies in health between NC and the entire USA.</li>
</ul>
 
<h4>Analysis Part 2: Change in Death Rates Over Time</h4>
<ul>
<li> For this part of the analysis, we first created a connected scatter plot to visualize change in total death rates in NC vs. USA over 17 years. The plot showed that death rates in both NC and the entire USA decreased over time (as expected). It also suggested that the death rate in NC has been consistently a bit higher than the USA. Interestingly, there was a large decrease in the US between 2014-2016.Specifically, morality in the USA decreased 42.14% between 1999 and 2016 and morality in NC decreased 19.25% between 1999 and 2016. Thus, while both death rates decreased over time, the death rate for the entire USA decreased about 20% more than North Carolina.</li>
<li> Based on the top 3 leading casues of death shown in the initial pie charts (and an interest in change in suicide rates), we then created connected scatter plots for those specific causes of deaths over time. While Heart Disease and Cancer still accounted for more than half of the USA's causes of death in 2016, both appear to decrease over time. Unintentional injuries and suicide appear to slightly increase over time. Further analysis is needed determine if the increases or decreases are statistically significant, but it is apparent that unintentional injuries and suicide did not decrease in the same way that Cancer and Heart Disease did.</li>
</ul>

<h4>Analysis Part 3: Compare Regional Death for 2016</h4>
<ul>
<li>To visualize regional comparisons of all Death Rates, we created a bar chart and a boxplot. We used the U.S. Census Bureau's regional classifications (source 3). The bar chart showed that the South had the highest regional average death rate in 2016, followed by the Midwest, the Northeast, and the West with the lowest average death rate of the four regions.The boxplot revealed that the Midwest has the closest average AADR to the entire USA, and that the South is the least similar in 2016.</li>
<li>Then, to visualize regional comparisons of Average Death Rates due to suicide in 2016, we created another bar chart and another boxplot using the same regional classifications.The bar chart showed that the West had the highest AADR due to suicide, followed by Midwest, South, and the Northeast with the lowest AADR due to suicide. The boxplot revealed that the Midwest has the closest average suicide AADR to the entire USA, and that the West is the least similar in 2016.</li>
</ul> 
</ul>

<h3>Part 5: Observations and Conclusions from Initial Inquiry</h3>
  <h4> 1. How do North Carolina's death rates compare to the entire US? </h4>
  <ul>
  <li> Hypothesis: North Carolina has higher death rates than the US.</li>
  <li>Conclusion: Overall, NC is similar to US in death rates (with both having more than half of deaths due to heart disease and cancer)</li>
  </ul>
  <h4>2. How do death rates change over time?</h4>
  <ul>
  <li>Hypothesis: All death rates decrease over time.</li>
  <li>Conclusion: Overall, death rates appeared to decrease. However, certain causes like unintentional injuries and suicide appeared to have slightly increased. Overall death rates in the US appeared to decrease at a higher rate than NC since 1999, as well as remain lower than NC's overall death rate every year.</li>
  </ul>
  <h4>3. Are there regional differences in death rates?</h4>
  <ul>
  <li>Hypothesis: The South has a higher average death rate than other USA regions.</li>
  <li>Conclusion: The South does have a slightly higher death rate. However, the West has a higher rate of suicides than other regions.</li>
  </ul>

<h3>Part 6: Implications of our Analysis<h3>
  <h4>Why does measuring death rates and death causes matter?</h4>
  <ul>
  <li> It helps to evaluate the effectiveness of the United States’s health system.</li>
  <li>It helps to inform us where to focus public health policies, programs, and budgets. For example: Because heart disease and cancer constitute over half of the leading causes of death in America and North Carolina, programs and policies that promote healthy lifestyles might be most beneficial in decreasing overall death rates (source 2). Furthermore, the increase in death rates due to unintentional injuries and suicide, while constituting a smaller percentage of deaths, suggest the value of increased emphasis on safety policies and mental health services.</li>
  </ul>
    
 <h4>What could we do for future analysis?</h4>
 <ul>
 <li> Analyze death rates by other demographic areas such as age group, gender, race/ethnicity </li>
 <li> Analyze cause of death rates of all countries (not just US) </li>
 <li> Use current data to predict future death rates </li>
 <li> Calculate if the changes seen over time are statistically significant </li>
 </ul>

<h3>Sources:</h3>
<ul> 
<li>National Center for Health Statistics. (2018). NCHS - Leading Causes of Death: United States [data file]. Available from Data.CDC.gov website: https://data.cdc.gov/NCHS/NCHS-Leading-Causes-of-Death-United-States/bi63-dtpu</li>
<li>Holland, K. (2017, August 24). What Are the 12 Leading Causes of Death in the United States? Retrieved October 14, 2018, from https://www.healthline.com/health/leading-causes-of-death#2</li>
<li>United States Census Bureau. (2015, July 28). Geography Atlas - Regions. Retrieved October 13, 2018, from https://www.census.gov/geo/reference/webatlas/regions.html</li>
</ul>
