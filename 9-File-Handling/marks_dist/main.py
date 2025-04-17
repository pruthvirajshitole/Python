f = open('9-File-Handling/marks_dist/marks.txt','w')
f.write("23,323,42\n43,54,43\n43,34")
f.close()


with open('9-File-Handling/marks_dist/marks.txt','r') as f:
    i = 0
    while True:
        i+=1
        line = f.readline()
        if not line:
            break
        m1 = line.split(',')[0]
        m2 = line.split(',')[1]
        try:
            m3 = line.split(',')[2]
        except:
            pass

        print(f'Marks of student{i} in AI: {m1}')
        print(f'Marks of student{i} in ML: {m2}')
        print(f'Marks of student{i} in DS: {m3}')