with open('Clustering/Hierarchical Clustering/Hiring/hiring.csv', 'r+') as f:
    data_to_change = []
    for line in f.readlines():
        data_to_change.append(line)
    f.close()

with open('Clustering/Hierarchical Clustering/Hiring/hiring.csv', 'w') as f:
    for line in data_to_change:
        line = line.replace('\t', ',')
        f.write(line)

