import pandas as pd
import numpy as np

#Set variables
budget1=r'/home/shoujun/Desktop/bootcamp/2017-11-03_Homework3/PyBank_raw_data/budget_data_1.csv'
output_file=r'/home/shoujun/Desktop/bootcamp/budget_report.txt'

#Read data
bd1=pd.read_csv(budget1)

#The total number of months included in the dataset
total_month=bd1.shape[0]

#The total amount of revenue gained over the entire period
total_revenue=bd1.ix[:,1].sum()

#The average change in revenue between months over the entire period
rev_change_list=[(bd1.ix[i+1,1]-bd1.ix[i,1]) for i in range(total_month-1)]
rev_change_array=np.array(rev_change_list)    
avg_rev_change=rev_change_array.sum()/len(rev_change_array)

#The greatest increase in revenue (date and amount) over the entire period
max_inc_index=np.argmax(rev_change_array)
max_inc_month=bd1.ix[max_inc_index+1,0]
max_inc_amount=rev_change_array[max_inc_index]

#The greatest decrease in revenue (date and amount) over the entire period
max_dec_index=np.argmin(rev_change_array)
max_dec_month=bd1.ix[max_dec_index+1,0]
max_dec_amount=rev_change_array[max_dec_index]

#Output results on screen
line1='Financial Analysis'
line2='-'*30
line3='Total Months: {}'.format(total_month)
line4='Total Revenue: ${}'.format(total_revenue)
line5='Average Revenue Change: ${}'.format(avg_rev_change)
line6='Greatest Increase in Revenue: {} (${})'.\
      format(max_inc_month, max_inc_amount)
line7='Greatest Decrease in Revenue: {} (${})'.\
      format(max_dec_month, max_dec_amount)

line='\n'.join([line1, line2, line3, line4, line5, line6, line7])
print(line)

#Write output results to file
with open(output_file, 'w') as file:
    file.write(line)
    
