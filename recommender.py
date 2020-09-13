import mysql.connector as mysql
from sklearn import tree

cnx = mysql.connect(user="root", password="",host="127.0.0.1", database="digikala")
cursor = cnx.cursor()
cursor.execute("select title, memory, ram, network, android from mobile")
data = cursor.fetchall()

x = []
y = []

for title, memory, ram, network, android in data:
    # print(title, memory, ram, network, android)
    x.append([memory, ram, network, android])
    y.append(title)

cnf = tree.DecisionTreeClassifier()
cnf.fit(x,y)

newdata = [[512,12,5,10]]
result = cnf.predict(newdata)
print(result)





