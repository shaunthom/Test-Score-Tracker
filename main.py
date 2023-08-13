ave_marks = []
full_line = []
ave = 0
low = 10000
lowest_marks = []
with open(filename, 'r') as fl:

    for line in fl:
        if line.strip():
            line = line.strip()
            full_line.append(line)

            '''line = line.split(',')
            #line11 = line.split(',')
            ave = 0
            line_list = line[1:]
            for number in line[1:]:
                ave += int(number)
            ave_marks.append(ave)
            if ave<low:
                low = ave
                lowest_marks = line'''

    
                
    f = lambda line: list(map(int, line.split(',')[1:]))
    required_value = min(full_line, key=f)         
    return f, required_value
