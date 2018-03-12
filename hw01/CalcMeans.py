from Means import *

N = 500

S = 1000

import time
'''
start_time = time.time()
print( "Mean     Std      Max       Min      Median" )
print( '---'*20    )
print( get_tuple_stream_mean(Mean_stream(easy_stream(S), N), 5))
print("Common EASY--- %s seconds ---" % (time.time() - start_time))
'''
start_time = time.time()
print( "Mean     Std      Max       Min      Median" )
print( '---'*20    )
print( get_tuple_stream_mean(Mean_stream_easy_deq(easy_stream(S), N), 5))
print("Fast Deque EASY--- %s seconds ---" % (time.time() - start_time))
''''
start_time = time.time()
print ("Mean     Std      Max       Min      Median" )
print ('---'*20 )
print (get_tuple_stream_mean(Mean_stream(medium_stream(S), N), 5))
print("Common MEDIUM--- %s seconds ---" % (time.time() - start_time))
'''
start_time = time.time()
print("Mean     Std      Max       Min      Median" )
print ('---'*20 )
print (get_tuple_stream_mean(Mean_stream_medium(medium_stream(S), N), 5))
print("Fast MEDIUM--- %s seconds ---" % (time.time() - start_time))
'''
start_time = time.time()
print("Mean     Std      Max       Min      Median") 
print('---'*20)
print(get_tuple_stream_mean(Mean_stream(nightmare_stream(S), N), 5))
print("Common NIGHT--- %s seconds ---" % (time.time() - start_time))
'''
start_time = time.time()
print("Mean     Std      Max       Min      Median")
print('---'*20)
print(get_tuple_stream_mean_night(Mean_stream_night(nightmare_stream(S), N), 5))
print("Decimal Fast NIGHT--- %s seconds ---" % (time.time() - start_time))
