import pandas as pd

input_file=r'/home/shoujun/Desktop/bootcamp/2017-11-03_Homework3/PyPoll_raw_data/election_data_2.csv' 
output_file=r'/home/shoujun/Desktop/poll.txt'

data=pd.read_csv(input_file)
total_votes=data.ix[:,'Voter ID'].count()

data_grp=data.groupby('Candidate').count().reset_index()
data_grp['percent']=[data_grp.ix[i,'Voter ID']/total_votes \
                     for i in data_grp.index]
winner=data_grp.ix[:,'Voter ID'].argmax()

line1='Election Results'
line2='-'*30
line3='Total Votes: {}'.format(total_votes)
line4='-'*30

line5=[]
for i in data_grp.index:
    temp='{}:{:.1%} ({})'.format(data_grp.ix[i,'Candidate'], \
                               data_grp.ix[i,'percent'],\
                               data_grp.ix[i,'Voter ID'])
    line5.append(temp)
    
line6='-'*30
line7='Winner: {}'.format(data_grp.ix[winner,'Candidate'])
line8='-'*30

line='\n'.join([line1, line2, line3, line4, *line5, line6, line7, line8])

print(line)

with open(output_file, 'w') as out:
    out.write(line)
