import re

with open('posts.csv') as f:
    for line in f:
        line_list = line.split(',')
        if '2 szob' in line:
            if int(re.sub('\D', '', line_list[2][:-3])) < 200000:
                print(line)
