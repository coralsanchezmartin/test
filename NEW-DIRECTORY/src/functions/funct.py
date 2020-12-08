import csv


def positives(list_post, upper_post):
    """
    # TODO Explain the method
    :param list_post: positives(csvlist) = open_csv(csv_file), open the file with all the numbers
    :param upper_post: positives (upper), variable define as 1000
    :return:a list that it creates with the positive values
    """
    list_post_complete = []  # Creating a list
    for linea_i in list_post:  # Iterates each line of the list (starting with the first one)
        if 0 < int(linea_i[1]) < upper_post:  # If the value 1 of the line is between 0 and 1000, go to the next line
            list_post_complete.append(linea_i)  # Add each value to the list above

    return list_post_complete  # return the list


def negatives(list_post, lower_post):
    list_neg_complete = []
    for linea_i in list_post:
        # print("I´m comparing" + str(linea_i) + "with" + str(lower))
        if 0 > int(linea_i[1]) > lower_post:
            list_neg_complete.append(linea_i)

    return list_neg_complete


def outliers_positives(list_post, upper_post):
    list_outpost_complete = []
    for linea_i in list_post:
        if int(linea_i[1]) > upper_post:
            list_outpost_complete.append(linea_i)

    return list_outpost_complete


def outliers_negatives(list_post, lower_post):
    list_out_negative_complete = []
    for linea_i in list_post:
        if int(linea_i[1]) < lower_post:
            list_out_negative_complete.append(linea_i)

    return list_out_negative_complete


def open_csv(new_file):
    """

    :param new_file: csvlist = open_csv(csv_file), csv_file is a variable define in constant, which has the path and the
     name of the csv file we want to open containing all our data.
    :return: list_i (the list of numbers in the csv file)
    """
    with open(new_file) as data:  # Open file from path
        entry = csv.reader(data, delimiter=',')
        list_i = list(entry)
    return list_i


def create_csv(create_new_csv, csvlist1):  # The method receives a number of parameters or arguments (two variables).
    output_f = open(create_new_csv, "w+")
    csv_str = ""

    for linea_i in csvlist1:  # it iterates each line of the list it receives as an argument.
        # if 0 < int(linea_i[1]) < 1000:
        csv_str += str(linea_i[0]) + ',' + str(
            linea_i[1]) + '\n'  # Format in which I want the csv data to be display.

    output_f.write(csv_str)
    output_f.close()
