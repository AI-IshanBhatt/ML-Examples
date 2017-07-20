import numpy as np


def prime_getter(ran):
    is_prime = np.ones((ran,), dtype=bool)
    is_prime[:2] = 0
    N_max = int(np.sqrt(len(is_prime)))

    for j in range(2, N_max):
        is_prime[2*j::j] = False

    print(np.nonzero(is_prime)) #nonzero returns index of all the elements in the array which are non zero
    # print(is_prime[np.nonzero(is_prime)]) #And this is how you get the values at those index


def fancy_indexing():
    """
    Numpy arrays can be indexed with slices, but also with boolean or integer arrays (masks). This method is
    called fancy indexing. It creates copies not views.
    """
    np.random.seed(3)
    a = np.random.random_integers(0,20,15) #0 to 20 ,15 integers
    mask = (a%3 == 0)
    extracted_from_mask = a[mask] #It's a copy not a view
    print(a)
    print(extracted_from_mask)
    print(np.may_share_memory(a, extracted_from_mask))
    a[a%3 == 0] = -1
    print(a) #Setting -1 for elements which were divisible by 3
    print("INDEXING BY ARRAY")
    print(a[[3,4,2,0]])
    a[[3,4,2,0]] = -55
    print(a)


def ele_comparison():
    a = np.array([4,3,2,6])
    b = np.array([3,3,4,6])
    print(a==b)
    print(a<b)
    print("LOGICAL OPERATIONS")
    c = np.array([1,0,1,0])
    d = np.array([1,0,1,1])
    print(np.logical_and(c,d))
    print(np.sin(a))
    print(np.log(a))


def sum_row_column():
    x = np.array([[3,4],[6,7]])
    print(x.sum()) #all elements
    print(x.sum(axis=0)) #It is column, first dimension
    print(x.sum(axis=1)) #It is row, second dimension (FUCKING CONFUSING but REMEMEBR) Revenrse of the index we use
    print("ALL ANY also works for it")
    print(np.any(x == 3))
    print(np.all(x != 15))


def broadcast():
    a = np.tile(np.arange(0, 40, 10), (3, 1)).T
    print(a)
    b = np.array([0,1,2])
    print(a+b) #b is broadcasted and 0,1,2 are added to each elements of the row
    """
    row matrix(single row) gets broadcast as same row N times
    column matrix(single column) gets broadcast as same column N times
    """
    """
    a = np.arange(0, 40, 10)
    a.shape -> (4,)
    a = a[:, np.newaxis]
    a.shape
    (4, 1),now this is the matrix you were wishing to get after a.T
    But not possible as T can't add new axis as now rows are needed.
    a = [[0],
    [10],
    [20],
    [30]]
    """


def broadcast_adv():
    x, y = np.ogrid[0:5, 0:5] #Creates the row and column matrix also adds in dimensions as well
    print(x)
    print(x.shape)
    print(y)
    print(y.shape)
    distance = np.sqrt(x**2 + y**2)
    print(distance)

def lexi_sort():
    surnames =    ('Hertz',    'Galilei', 'Hertz')
    first_names = ('Heinrich', 'Galileo', 'Gustav')
    ind = np.lexsort((first_names, surnames))
    """
    First it will sort surnames - Resulting is Galilei, Hertz, Hertz then fnames is used to resolve the Hertz,Hertz
    As, Gustav < Heinrich, the order would be 1 - Galilei 2 Hertz-Gustav 0 Hertz-Heinrich
    """
    return ind #This will b array([1, 2, 0]) 
# prime_getter(100)
# fancy_indexing()
# ele_comparison()
# sum_row_column()
# broadcast()
broadcast_adv()
