import numpy as np

marks = [10, 20, 30, 40, 50, 60, 70, 100]

Average_marks_max = max(marks)
Average_marks_min = min(marks)
Average_marks_mean = np.mean(marks)

print(Average_marks_max)
print(Average_marks_min)
print(Average_marks_mean)

# three commonly used functions when working with Data Science: max(), min(), and mean()
# We use underscore (_) to separate strings because Python cannot read space as separator.
# We write np. in front of mean to let Python know that we want to activate the mean function from the Numpy library.