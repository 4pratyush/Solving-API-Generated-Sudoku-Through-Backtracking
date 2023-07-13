import requests
import numpy as np


parameter = {"difficulty": "easy"}

response = requests.get("https://sugoku.onrender.com/board", params=parameter)
data = response.text
temp = []
for i in data:
    if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        temp.append(i)

for n in range(0, len(temp)):
    temp[n] = int(temp[n])

grid = np.array(temp).reshape(9, 9)
