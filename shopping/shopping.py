import csv
import sys
import pandas as pd
#import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv(sys.argv[1]) # or w/o pandas with open('shopping.csv', newline='') as csvfile:\n    data = csv.reader(csvfile)

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data") # where data = shopping.csv

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(data)
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    # Dictionary for months
    d = { 'Jan':0, 'Feb':1, 'Mar':2, 'Apr':3, 'May':4, 'June':5, 'Jul':6, 'Aug':7, 'Sep':8, 'Oct':9, 'Nov':10, 'Dec':11 }

    # Month should be 0 for January, 1 for February, 2 for March, etc. up to 11 for December
    filename.Month = filename.Month.map(d)

    # VisitorType should be 1 for returning visitors and 0 for non-returning visitors
    filename.VisitorType = filename.VisitorType.map(lambda x: 1 if x == 'Returning_Visitor' else 0)

    # Weekend should be 1 if the user visited on a weekend and 0 otherwise
    filename.Weekend = filename.Weekend.map(lambda x: 1 if x == True else 0)

    # Revenue should be 1 if revenue is true, and 0 otherwise
    filename.Revenue = filename.Revenue.map(lambda x: 1 if x == True else 0)

    # 2 lists for 2 values accordingly
    ints = ['Administrative', 'Informational', 'ProductRelated', 'Month', 'OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType', 'Weekend']
    floats = ['Administrative_Duration', 'Informational_Duration', 'ProductRelated_Duration', 'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay']

    # Check and convert to appropriate data types
    for value in ints:
      if filename[value].dtype != 'int64':
        filename = filename.astype({value: 'int64'})
      else:
        continue

    for value in floats:
      if filename[value].dtype != 'float64':
        filename = filename.astype({value: 'float64'})
      else:
        continue

    evidence = filename.iloc[:,:-1].values.tolist() # exclude last column 'Revenue'
    labels = filename.iloc[:,-1].values.tolist() # last column 'Revenue'

    if len(evidence) != len(labels):
      print('Evidence and labels lists not of the same length')
    if len(filename.iloc[:,:-1].columns) != 17:
      print('Each element in the evidence list should itself be a list. The list should be of length 17')
    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    neighbors = KNeighborsClassifier(n_neighbors=1) # different metrics, k-numbers of neighbors and other parameters shows us different results
    neighbors.fit(evidence, labels) # fit(X_train, y_train)
    return neighbors


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    positive = labels.count(1)
    negative = labels.count(0)

    # Initial values
    sen = 0 # TP
    sp = 0 # TN

    for label, prediction in zip(labels, predictions):
      if label == 1:
        if label == prediction:
          sen += 1
      elif label == 0:
        if label == prediction:
          sp += 1
      else:
        print("Something wrong with data values in Revenue's column")

    sensitivity = sen / positive # TP rate
    specificity = sp / negative # TN rate
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()