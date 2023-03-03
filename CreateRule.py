with open('C:/Users/Lin/Desktop/A.txt', 'r') as file_a, open('C:/Users/Lin/Desktop/B.txt', 'w') as file_b:
    file_b.write('ip host not ')
    for line in file_a:
        file_b.write('{} and not '.format(line.strip()))
    file_b.seek(file_b.tell() - len(' and not '), 0)
    file_b.truncate() 
