#time taken per row is roughly 6 minutes
#number of rows in total=52*4
import numpy as np

#6 mins per row, 14 hours for 72 rows, 3 rows= 19min 19 sec, 4 rows=25 min 07 sec,5 rows= 31 min 39 sec,6: 37 min 31 sec, 7 rows= 43 min 32 sec,8 rows 50 min 10 sec, p r= 55 min 55 s, 

rows=np.array([1, 3, 4, 5, 6, 7, 8])
time_taken=np.array([6.0, 19.32, 25.12, 31.65, 37.52, 43.53, 55.92])

avg_time_arr=np.array(time_taken/rows)
mean_time=np.mean(avg_time_arr)
print(avg_time_arr)

print("The mean crochet time is: ",mean_time)

Total_time=mean_time*52*4

print("Total crochet time in hours is: ",Total_time/60)

import matplotlib.pyplot as plt

plt.plot(rows, time_taken, marker='.')
plt.title('Graph of time taken per row of crochet', loc='center')
plt.xlabel('No. of rows')
plt.ylabel('Time taken')

plt.show()

