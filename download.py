import bs4
import requests
link_list = []
file = 'file.txt'
with open(file) as f:
    for line in f:
        line = line.strip('\n')
        link_list.append(line)
print(link_list)
  