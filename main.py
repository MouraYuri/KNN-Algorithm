dataset = open('dataset.txt', 'r')
datasetlist = dataset.readlines()
query = '25 89'

def treatData(dataset):
    print("\/ dataset \/")
    for row in dataset:
        row = row.split(' ')
        print(row)

treatData(datasetlist)

def euclidianDistance(A, B):
    p = (int(A[1]) - int(B[1]))**2
    q = (int(A[0]) - int(B[0]))**2
    return (p+q)**0.5


def knn(dataset, query, k):
    distanceAndClasses = []
    query = query.split(' ')
    print("Query point => {}".format(query))
    for row in dataset:
        print(euclidianDistance(query, [row[0], row[1]]))

knn(datasetlist, query, 1)