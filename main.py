from src.functions.funct import *  # * means wildcard, it imports everything defined in the new file
from src.constants.const import *
# if you don't want to import the whole thing, you can import only one variable for example positives.
# everything that goes into a different file has to a define thing (methods or defined variables)


def main():
    """
     Calling the methods
    """
    csvlist = open_csv(csv_file)

    list_positives = positives(csvlist, upper)
    list_negatives = negatives(csvlist, lower)
    list_out_positives = outliers_positives(csvlist, upper)
    list_out_negatives = outliers_negatives(csvlist, lower)

    # When you call the method, in brackets  you define the parameters you are using.
    create_csv(csv_file2, list_positives)
    create_csv(csv_file3, list_negatives)
    create_csv(csv_file4, list_out_positives)
    create_csv(csv_file5, list_out_negatives)


# As I have created a new list above that returns the positives method, I want the create_csv method the
# one I call in main, to pass both, the csv that I am going to create (in this case csv_file2, variable defined
# above with the path and the name), and the list with the positive values that I created above (list returned by the
# positives method).

main()
