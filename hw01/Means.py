from Stream import *
        
import numpy as np

def median(array):
    r = sorted(array)
    return [r[0], r[len(array) // 2], r[-1]]

def Mean_stream_easy(stream, k):
    "This method is aplied for easy"
    """Yield mean of K numbers from stream"""
    numbers = []
    numbers2 = []
    sums = 0.0
    sums2 = 0.0
    for i in stream:
        numbers.append(i)
        numbers2.append(i**2)
        sums += i
        sums2 += i**2
        if len(numbers) >= k:
            m = float(sums) / k
            m2 = float(sums2) / k                
            yield (m, m2 - m**2, numbers[-1], 
                   numbers[0], float(numbers[k // 2]))
            sums -= numbers[0]
            numbers.pop(0)
            sums2 -= numbers2[0]
            numbers2.pop(0)


from collections import deque

def Mean_stream_easy_deq(stream, k):
    "This method is aplied for easy"
    """Yield mean of K numbers from stream"""
    numbers = deque()   
    numbers2 = deque()   
    sums = 0.0
    sums2 = 0.0
    for i in stream:
        numbers.append(i)
        numbers2.append(i**2)
        sums += i
        sums2 += i**2
        if len(numbers) >= k:
            m = float(sums) / k
            m2 = float(sums2) / k                
            yield (m, m2 - m**2, numbers[-1], 
                   numbers[0], float(numbers[k // 2]))
            sums -= numbers.popleft()
            sums2 -= numbers2.popleft()
            
      
def Mean_stream(stream, k):
    "This method is aplied for med and night"
    """Yield mean of K numbers from stream"""
    numbers = deque()
    sums = 0.0 
    for i in stream:
        numbers.append(i)
        sums += i
        if len(numbers) >= k:
            yield (np.mean(numbers), np.std(numbers)**2, np.amax(numbers), 
                   np.amin(numbers), np.median(numbers))
#            print "   ", np.median(numbers)
            sums -= numbers.popleft()

def Mean_stream_med(stream, k):
    "This method is aplied for med"
    """Yield mean of K numbers from stream"""
    numbers = deque()
    sums = 0.
    numbers2 = deque()   
    sums2 = 0.
    for i in stream:
        numbers.append(i)
        numbers2.append(i**2)
        sums += i
        sums2 += i**2
        if len(numbers) >= k:
            m = sums / k
            m2 = sums2/ k
            yield (m, m2 - m**2, np.amax(numbers), 
                   np.amin(numbers), np.median(numbers))
            sums -= numbers.popleft()
            sums2 -= numbers2.popleft()


from decimal import Decimal

def Mean_stream_c(stream, k):
    "This method is aplied for night"
    """Yield mean of K numbers from stream"""
    numbers = deque()
    sums = 0.
    numbers2 = deque()   
    sums2 = 0.
    for i in stream:
        numbers.append(i)
        numbers2.append(i**2)
        sums += i
        sums2 += i**2
        if len(numbers) >= k:
            m = Decimal(sums / k)
            m2 = Decimal(sums2/ k)
            yield (m, m2 - m**2, np.amax(numbers), 
                   np.amin(numbers), np.median(numbers))
            sums -= numbers.popleft()
            sums2 -= numbers2.popleft()

def Mean_stream_night(stream, k):
    "This method is aplied for night"
    """Yield mean of K numbers from stream"""
    numbers = deque()
    sums = 0.
    numbers2 = deque()
    sums2 = 0.
    for i in stream:
        numbers.append(i)
        numbers2.append(i**2)
        sums += i
        sums2 += i**2
        if len(numbers) >= k:
            m = Decimal(sums / k)
            m2 = Decimal(sums2/ k)
            res = median(numbers)
            yield (m, m2 - m**2, res[2], 
                   res[0], res[1])
            sums -= numbers.popleft()
            sums2 -= numbers2.popleft()

def Mean_stream_medium(stream, k):
    "This method is aplied for night"
    """Yield mean of K numbers from stream"""
    numbers = deque()
    sums = 0.
    numbers2 = deque()
    sums2 = 0.
    for i in stream:
        numbers.append(i)
        numbers2.append(i**2)
        sums += i
        sums2 += i**2
        if len(numbers) >= k:
            m = sums / k
            m2 = sums2/ k
            res = median(numbers)
            yield (m, m2 - m**2, res[2], 
                   res[0], res[1])
            sums -= numbers.popleft()
            sums2 -= numbers2.popleft()
            
def Mean_stream_night3(stream, k):
    "This method is aplied for night without sorting"
    """Yield mean of K numbers from stream"""
    m_bool = True
    numbers = deque()
    sums = 0.
    numbers2 = deque()
    sums2 = 0.
    for i in stream:
        numbers.append(i)
        numbers2.append(i**2)
        sums += i
        sums2 += i**2
        if len(numbers) >= k:
            m = Decimal(sums / k)
            m2 = Decimal(sums2/ k)
            if m_bool == True:
                number_sort = sorted(numbers)
                m_bool = False
            else:
                index = 0
                for j in range(1, len(number_sort)):
                    if (i <= number_sort[0]):
                        index = 0
                    elif (i >= number_sort[-1]):
                        index = 0
                    elif (i >= number_sort[j-1] and i <= number_sort[j]):
                        index = j
                number_sort.insert(index, i)
                   
            yield (m, m2 - m**2, number_sort[-1], 
                   number_sort[0], number_sort[k // 2])
            number_sort.remove(numbers[0]) 
            sums -= numbers.popleft()
            sums2 -= numbers2.popleft()

def get_tuple_stream_mean(stream, number_of_values):
    result = np.zeros(number_of_values, dtype='object')
    count = 0.
    for streamed_tuple in stream:
        result += streamed_tuple
        count += 1
    return ['{:0.2f}'.format(x) for x in result / count]

def get_tuple_stream_mean_night(stream, number_of_values):
    result = np.zeros(number_of_values, dtype='object')
    count = 0.
    for streamed_tuple in stream:
        result += streamed_tuple
        count += 1
        
    res = []
    res.append(result[0] / Decimal(count))
    res.append(result[1] / Decimal(count))
    res.append(result[2] / count)
    res.append(result[3] / count)
    res.append(result[4] / count)
    return ['{:0.2f}'.format(x) for x in res]