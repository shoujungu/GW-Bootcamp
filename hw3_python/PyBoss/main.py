import us_state_abbrev as state
import datetime

input_file=r'/home/shoujun/Desktop/bootcamp/2017-11-03_Homework3/PyBoss_raw_data/employee_data1.csv'
output_file=r'/home/shoujun/Desktop/employee.csv'

lines=[]

with open(input_file, 'r') as file:
    #convert header
    line=next(file)
    line=line.split(',')
    line=list(line[0:1])+['First Name', 'Last Name']+list(line[2:])
    line=','.join(line)
    lines.append(line)

    #convert data
    for line in file:
        line=line.split(',')
        name=line[1].split(' ')
        date=[datetime.datetime.strptime(line[2], '%Y-%m-%d').\
              strftime('%m/%d/%y')]
        ssn=['***-**'+line[3][6:]]
        state_=[state.us_state_abbrev[line[-1].strip()]+'\n']
        line=line[0:1]+name+date+ssn+state_
        line=','.join(line)
        lines.append(line)

with open(output_file, 'w') as out:
    out.writelines(lines)
