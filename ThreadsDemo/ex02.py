import threading


def extract_data(source_filename, column, output_file):
    print(f'Extracting column {column} from file {source_filename}')
    with open(source_filename, 'rt') as f:
        for line in f:
            columns = line.split(',')
            output_file.write(f'From {source_filename}: ')
            output_file.write(columns[column] )
            output_file.write('\n')
    print('Writing to consolidated_data.txt is done')


if __name__ == '__main__':
    file = open('consolidated_data.txt', 'wt')
    t1 = threading.Thread(target=extract_data, args=('dataset-1.csv', 1, file))
    t2 = threading.Thread(target=extract_data, args=('dataset-2.csv', 2, file))

    t1.start()
    t2.start()
    print('Threads have been given to scheduler for execution')
    t1.join()
    t2.join()
    file.close()
    print('Closing the file')
    print('The file consolidated_data.txt has been closed')