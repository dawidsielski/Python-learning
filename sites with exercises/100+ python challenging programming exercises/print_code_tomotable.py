for i in range(1,52):
    filename = str(i) + '.txt'
    # print('matrix_{} = dlmread(\'{}\');'.format(i, filename))
    print('vect_data_{} = vectorize_data(matrix_{});'.format(i, i))