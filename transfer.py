import pandas as pd

file1 = 'transfer.xlsx'
sheet = pd.read_excel(file1)
df = pd.DataFrame(sheet)

file2 = open('result_new.txt')
line = 0
content = file2.readline()
while content is not None and content != '':
    valueList = content.split(' ')
    if len(valueList) != 2 and len(valueList) != 7:
        pass
    elif len(valueList) == 2:
        df.loc[line] = [valueList[0], '', '', '', '', '']
        line = line + 1
        pass
    elif len(valueList) == 7:
        df.loc[line] = [valueList[0], valueList[1], valueList[2], valueList[3], valueList[4], valueList[5]]
        line = line + 1
        pass
    else:
        pass
    content = file2.readline()
df.to_csv('result.csv')
