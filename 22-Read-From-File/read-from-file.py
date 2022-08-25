text_line = []
with open('Training_01.txt', 'r') as open_file:
    for line in open_file:
        text_line.append(line.split("/sun")[0][3:])

categories = {}
for i in text_line:
    categories[i] = text_line.count(i)

print(categories)

