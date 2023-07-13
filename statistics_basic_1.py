QUESTION:-1. What is Statistics?
Statistics is the science of collecting, organizing, and analyzing data.



QUESTION:-2. Define the different types of statistics and give an example of when each type might be used.
There are two types of statistics :- 
(1) Descriptive statistics.
(2) Inferential statistics.
 
(1) Descriptive statistics :- It consists of organizing and summarizing the data.
Example :- 
height = [178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5]
import numpy as np 
np.mean(height)
np.median(height)

height = [178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5]
from scipy import stats 
stats.mode(height)

(2) Inferential statistics :- It consists of using data you have measured to from conclusion.
Example :- 
import scipy.stats as stats 
speed = [15,20,10,8,7,10,8,11,12,11]
stats.ttest_1samp(speed, popmean=10)



QUESTION:-3. What are the different types of data and how do they differ from each other? Provide an example of each type of data.

(1) Quantitative Data :- Quantitative data is data that can be counted or measured in numerical values. The two main types of quantitative data are discrete data and continuous data. Height in feet, age in years, and weight in pounds are examples of quantitative data.
Example :- 
height = [178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5]
from scipy import stats 
stats.mode(height)

(2) Qualitative Data :- Qualitative data is descriptive, expressed in terms of feelings rather than numerical values. Qualitative data analysis cannot be counted or measured because it describes the data. It refers to the words or labels used to describe certain characteristics or traits.
Example :- 
import seaborn as sns 
df = sns.load_dataset('tips')
df.head()



QUESTION:-4. Categories the following datasets with respect to quantitative and qualitative data types:
(i) Grading in exam: A+, A, B+, B, C+, C, D, E
(ii) Colour of mangoes: yellow, green, orange, red
(iii) Height data of a class: [178.9, 179, 179.5, 176, 177.2, 178.3, 175.8,.....]
(iv) Number of mangoes exported by a farm: [500, 600, 478, 672,......]

(i) :- Qualitative Data Types.
(ii) :- Qualitative Data Types.
(iii) :- Quantitative Data Types.
(iv) :- Quantitative Data Types.



QUESTION:-5. Explain the concept of levels of measurement and give an example of a variable for each level.
Levels of measurement, also called scales of measurement, tell you how precisely variables are recorded.
Example :- 
There are four main levels of measurement: nominal, ordinal, interval, and ratio
Nominal :– Latin for name only (Republican, Democrat, Green, Libertarian)
Ordinal :– Think ordered levels or ranks (small–8oz, medium–12oz, large–32oz)
Interval :– Equal intervals among levels (1 dollar to 2 dollars is the same interval as 88 dollars to 89 dollars)
Ratio :– Let the “o” in ratio remind you of a zero in the scale (Day 0, day 1, day 2, day 3, …)



QUESTION:-6. Why is it important to understand the level of measurement when analyzing data? Provide an example to illustrate your answer.
It is important to understand the level of measurement of variables in research, because the level of measurement determines the type of statistical analysis that can be conducted, and, therefore, the type of conclusions that can be drawn from the research.
Nominal Level :-

Examples of Nominal Level of Measurement :-
Religion (Muslim, Hindu, Christian, Buddhist)
Race (Hispanic, African, Asian)
Language (Urdu, English, French, Punjabi, Arabic)
Gender (Male, Female)
Marital Status (Married, Single, Divorced)
Number plates on Cars/ Models of Cars (Toyota, Mehran)
Parts of Speech (Noun, Verb, Article, Pronoun)

Examples of Ordinal Level of Measurement :-
Rankings (1st, 2nd, 3rd)
Marks Grades (A, B, C, D)
Evaluation such as High, Medium, Low
Educational level (Elementary School, High School, College, University)
Movie Ratings (1 star, 2 stars, 3 stars, 4 stars, 5 stars)
Pain Ratings (more, less, no)
Cancer Stages (Stage 1, Stage 2, Stage 3)
Hypertension Categories (Mild, Moderate, Severe)

Examples of Interval Level of Measurement :-
Temperature with Celsius scale/ Fahrenheit scale
Level of happiness rated from 1 to 10
Education (in years)
Standardized tests of psychological, sociological, and educational discipline use interval scales.
SAT scores

Examples of Ratio Level of Measurement :-
Height
Weight
Age
Length
Volume
Number of home computers
Salary



QUESTION:-7. How nominal data type is different from ordinal data type.
Nominal Data is classified without any intrinsic ordering or rank, Ordinal Data has some predetermined or natural order. Nominal data is qualitative or categorical data, while Ordinal data is considered “in-between” qualitative and quantitative data.



QUESTION:-8. Which type of plot can be used to display data in terms of range?
Histogram type of plot can be used to display data in terms of range.



QUESTION:-9. Describe the difference between descriptive and inferential statistics. Give an example of each type of statistics and explain how they are used.
Descriptive statistics:
Describe the features of populations and/or samples.
Organize and present data in a purely factual way.
Present final results visually, using tables, charts, or graphs.
Draw conclusions based on known data.
Use measures like central tendency, distribution, and variance.
Example :- 
height = [178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5]
import numpy as np 
np.mean(height)
np.median(height)

height = [178, 177, 176, 177, 178.2, 178, 175, 179, 180, 175, 178.9, 176.2, 177, 172.5, 178, 176.5]
from scipy import stats 
stats.mode(height)



Inferential statistics:
Use samples to make generalizations about larger populations.
Help us to make estimates and predict future outcomes.
Present final results in the form of probabilities.
Draw conclusions that go beyond the available data.
Use techniques like hypothesis testing, confidence intervals, and regression and correlation analysis.
Example :- 
import scipy.stats as stats 
speed = [15,20,10,8,7,10,8,11,12,11]
stats.ttest_1samp(speed, popmean=10)



QUESTION:-10. What are some common measures of central tendency and variability used in statistics? Explain how each measure can be used to describe to dataset. 
Examples of these measures include the mean, median, and mode. These statistics indicate where most values in a distribution fall and are also referred to as the central location of a distribution. You can think of central tendency as the propensity for data points to cluster around a middle value.

Mean :- Mean is the average of the given numbers and is calculated by dividing the sum of given numbers by the total number of numbers. 
Median :- The median is the middle number in a sorted, ascending or descending list of numbers and can be more descriptive of that data set than the average.
Mode :- A mode is defined as the value that has a higher frequency in a given set of values. It is the value that appears the most number of times. 





