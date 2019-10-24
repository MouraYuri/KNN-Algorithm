dataset = open('dataset.txt', 'r')
datasetlist = dataset.readlines()
query = '34 78'

def euclidianDistance(A, B):
    p = (int(A[1]) - int(B[1]))**2
    q = (int(A[0]) - int(B[0]))**2
    return (p+q)**0.5

'''
            DATASET
TEMPERATURA     Umidade     Jogar?
34              78          N
32              65          N
26              89          S
22              56          S

'''

def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i][0] > nums[i + 1][0]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True
    return nums

def knn(dataset, query, k):
    distanceAndClasses = []
    query = query.split(' ')
    for x in range(len(dataset)):
        dataset[x] = dataset[x].split(' ')
        distanceAndClasses.append([euclidianDistance(query, dataset[x]), dataset[x][2]])
    distanceAndClasses = bubble_sort(distanceAndClasses)
    counter = 0
    for y in range(k):
        if (distanceAndClasses[y][1] == 'S\n'):
            counter = counter + 1
    if counter==k:
        return 'S\n'
    else:
        return 'N\n'



print("Jogar? => {}".format(knn(datasetlist, query, 3)))