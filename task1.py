from data import dataset

#   Написати функцію, що зберігає інформацію про покупку користувачем товару у словник
#   Викликати функцію


def addUserProduct(user_name, product_name, product_price):


    if user_name not in  dataset:
        dataset[user_name]= dict()


    if product_name not in  dataset[user_name]:
        dataset[user_name][product_name] = dict()

    dataset[user_name][product_name]["sell"] = product_price


print("Task 1")

''''#Додати нового користувача та нову покупку
addUserProduct(?,?,?)

#Додати існуючому користувачу нову покупку нового продукту
addUserProduct(?,?,?)

#Додати існуючому користувачу нову покупку існуючого продукту
addUserProduct(?,?,?)'''
nname="vak"
nphone="asdf34"
nsell=450.00
addUserProduct(nname,nphone,nsell)
print(dataset)


print("\n\n")