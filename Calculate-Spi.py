import numpy as np


def cal_spi(precipitation, month):
    all_spi = ['nill'] * len(precipitation)
    mean = np.mean(precipitation)
    std = np.std(precipitation)
    if month == 1:
        for i in range(len(precipitation)):
            all_spi[i] = round((precipitation[i] - mean) / std, 4)
    else:
        k = 0
        Sum = []
        for i in range(month-1, len(precipitation)):
            s = 0
            for j in range(k, month+k):
                s += precipitation[j]
            Sum.append(s)
            k += 1
            all_spi[i] = round((s - mean) / std, 4)
    return all_spi


def printlist(prep):
    for item in prep:
        print(item)


def traverse_file():
    prep = []
    file_name = input('Enter the file name to read data: ')+'.txt'
    with open(file_name, 'r') as file:
        spi = 0
        while True:
            line = file.readline()
            if line == '':
                break
            prep.append(float(line.split()[0]))
            spi += 1
    return prep


def store_in_file(prep, spi, spi_index):
    name = spi + '.txt'
    with open(name, 'w') as file:
        for k in range(len(spi_index)):
            file.write('SPI'+str(spi_index[k])+'\t|\t')
        file.write('\n'+'-'*(len(spi_index))*13+'\n')
        for j in range(len(prep[0])):
            for i in range(len(prep)):
                file.write(str(prep[i][j])+'\t|\t')
            file.write('\n')


def print_table(prep, spi_index):
    for k in range(len(prep)):
        print('SPI' + str(spi_index[k]) + '\t', end='\t')
    print('\n' + '-' * (len(spi_index)) * 13 + '\n')
    for i in range(len(prep[0])):
        for j in range(len(prep)):
            print(f"{prep[j][i]}\t", end='|\t')
        print()


if __name__ == '__main__':
    prep = traverse_file()
    indexes = int(input("How many indexes you want to calculate: "))
    lst = []
    spi_index = []
    for i in range(indexes):
        month = int(input('Enter the month to calculate SPI: '))
        prep1 = cal_spi(prep, month)
        lst.append(prep1)
        spi_index.append(month)
    print_table(lst, spi_index)
    var = input("Enter (y/n) for saving file: ")
    if var == 'y':
        store_in_file(lst, input('Enter the name of file to store data: '), spi_index)
