import re

input_file=r'/home/shoujun/Desktop/bootcamp/2017-11-03_Homework3/PyParagraph_raw_data/paragraph_1.txt'
output_file=r'/home/shoujun/Desktop/report.txt'

regex=re.compile(r'\b\w+\b')
sen = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)

def word_c(sentence):
    l=re.findall(regex, sentence)
    return len(l)

with open(input_file, 'r', encoding='utf-8') as file:
    data=file.read()

    #Word count
    wc=word_c(data) 

    #Sentence count
    sen_list=sen.findall(data)
    sc=len(sen_list)
    
    #Average Letter Count
    word_list=re.findall(regex, data)
    word_letter_list=[len(i) for i in word_list]
    avg_letter=sum(word_letter_list)/wc 

    #Average Sentence Length
    avg_sent_len=sum([word_c(i) for i in sen_list])/sc
    

line1='Paragraph Analysis'
line2='-'*30
line3='Approximate Word Count: {}'.format(wc)
line4='Approximate Sentence Count: {}'.format(sc)
line5='Average Letter Count: {}'.format(avg_letter)
line6='Average Sentence Length: {}'.format(avg_sent_len)
line='\n'.join([line1, line2, line3, line4, line5, line6])

print(line)

with open(output_file, 'w') as out:
    out.write(line)

