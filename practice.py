# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# rainfall = np.array([50, 70, 90, 110, 130, 150, 170, 190, 210, 230]).reshape(-1, 1)  # in mm

# crop_yield = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
# model = LinearRegression()
# model.fit(rainfall, crop_yield)

# new_rainfall = np.array([[120], [180]])  
# predicted_yield = model.predict(new_rainfall)

# print("PredictedYields:", predicted_yield)


# plt.scatter(rainfall, crop_yield, color='blue', label='Actual Yield')
# plt.plot(rainfall, model.predict(rainfall), color='red', label='Regression Line')
# plt.scatter(new_rainfall, predicted_yield, color='green', label='Predicted Yield')
# plt.xlabel('Rainfall (mm)')
# plt.ylabel('Crop Yield (tons)')
# plt.title('Crop Yield Prediction based on Rainfall')
# plt.legend()
# plt.show()


# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LogisticRegression

# hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
# exam_result = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# model = LogisticRegression()
# model.fit(hours_studied, exam_result)

# new_hours = np.array([[3.5], [7.5]])
# predicted_results = model.predict(new_hours)
# print(predicted_results)
# plt.scatter(hours_studied, exam_result, color='blue')
# plt.plot(hours_studied, model.predict_proba(hours_studied)[:, 1], color='red')
# plt.scatter(new_hours, predicted_results, color='green')
# plt.xlabel('Hours Studied')
# plt.ylabel('Exam Result (1 for Pass, 0 for Fail)')
# plt.title('Pass/Fail Prediction based on Hours Studied')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans

# X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])

# kmeans = KMeans(n_clusters=2)
# kmeans.fit(X)

# cluster_centers = kmeans.cluster_centers_
# labels = kmeans.labels_

# colors = ['r', 'g']

# for i in range(len(X)):
#     plt.scatter(X[i][0], X[i][1], color=colors[labels[i]], marker='o')

# plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker='x', s=150, linewidths=5, zorder=10)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('K-Means Clustering')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.neighbors import KNeighborsClassifier

# X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
# y = np.array([0, 0, 1, 1, 0, 1])

# knn = KNeighborsClassifier(n_neighbors=3)
# knn.fit(X, y)

# plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('KNN classification')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.tree import DecisionTreeClassifier

# X = np.array([[1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]])
# y = np.array([0, 0, 1, 1, 0, 1])

# tree = DecisionTreeClassifier(max_depth=3)
# tree.fit(X, y)

# plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Decision Tre')
# plt.show()

# alpha=str(input("enter the alphabet:"))
# if(alpha=='a'or alpha=='e'or alpha=='i'or alpha=='o'or alpha=='u'):
#     print(alpha,"is a vowel")
# else:
#     print(alpha,"is a consonant")    


#dLinearRegression

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# rainfall in mm(X features)
rainfall = np.array([50, 70, 90, 110, 130, 150, 170, 190, 210, 230]).reshape(-1, 1)  # in mm

# crop yield in tons(our Y/ Target)
crop_yield = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
model = LinearRegression()
model.fit(rainfall, crop_yield)

# predict ofn new rainfal values
new_rainfall = np.array([[120], [180]])  
predicted_yield = model.predict(new_rainfall)

print("PredictedYields:", predicted_yield)

# Visualize 
plt.scatter(rainfall, crop_yield, color='blue', label='Actual Yield')
plt.plot(rainfall, model.predict(rainfall), color='red', label='Regression Line')
plt.scatter(new_rainfall, predicted_yield, color='green', label='Predicted Yield')
plt.xlabel('Rainfall (mm)')
plt.ylabel('Crop Yield (tons)')
plt.title('Crop Yield Prediction based on Rainfall')
plt.legend()
plt.show()

#LogisticRegression

# import numpy as np 
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LogisticRegression

# hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)d
# exam_result = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# model = LogisticRegression()
# model.fit(hours_studied, exam_result)

# new_hours = np.array([[3.5], [7.5]])
# predicted_results = model.predict(new_hours)
# print(predicted_results)
# plt.scatter(hours_studied, exam_result, color='blue')
# plt.plot(hours_studied, model.predict_proba(hours_studied)[:, 1], color='red')
# plt.scatter(new_hours, predicted_results, color='green')
# plt.xlabel('Hours Studied')
# plt.ylabel('Exam Result (1 for Pass, 0 for Fail)')
# plt.title('Pass/Fail Prediction based on Hours Studied')
# plt.show()

