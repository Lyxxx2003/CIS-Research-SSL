import random
train = []
test = []
count = 2
with open('ourdataset.data') as f:
    for line in f:
        if count > 0:
          count = count - 1
          continue

        items = line.strip().split('	')
        if int(items[-2])<3:
            items[-2] = '0'
        else:
            items[-2] = '1'
        new_line = ' '.join(items[:-1])+'\n'
        if random.random() > 0.2:
            train.append(new_line)
        else:
            test.append(new_line)

with open('train.txt','w') as f:
    f.writelines(train)

with open('test.txt','w') as f:
    f.writelines(test)