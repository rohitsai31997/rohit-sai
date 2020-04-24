from pymongo import MongoClient
democlient = MongoClient()

#Default parameters that have to be passed whenever you create a client
myclient = MongoClient('localhost', 27017)
print(myclient.list_database_names())

#Collections within Mongo are like tables within SQL
mydb = myclient["demo"] #db name - Can have multiple collections
my_col = mydb['dbtable']    #Collection name - Just like a table
mylist = [
    { "id" : 1, "name" : "John Doe", "Address" : "Highway 37"},
    { "id" : 2, "name" : "Jane Doe", "Address" : "LowStreet 27"}
]

my_col.insert_many(mylist)


"""Creating a new collection in the existing database.
We have to input some values in order for the new collection
to be visible in MongoDB Compass as empty collections aren't shown"""
test_col = mydb['Collection1']
mylist1 = [
    { "id" : 3, "name" : "Chris", "Address" : "High 37"},
    { "id" : 4, "name" : "Scarlett", "Address" : "Low 27"}
]
test_col.insert_many(mylist1)



#Giving the name of the database and input
# and this checks whether it already exists or not
dblist = myclient.list_database_names()
if input("Enter DB : ") in dblist:
    print("The database already exists.")
else:
    print("Not present")

#Prints the names of all the databases.
print(dblist)

"""Using find() and find_one() 
find_one() -Returns one document that satisfies the 
specified query criteria on the collection or view
find() finds all the occurrences"""
x = my_col.find_one()
print(x)

for x in my_col.find():
    print(x)


"""Custom Search Technique"""
my_query = {"name" : "John Doe"}

my_doc = my_col.find(my_query)
for x in my_doc:
    print(x)

#Sorting Technique
my_doc = my_col.find().sort("name", 1)  #Ascending Order
my_doc = my_col.find().sort("name", -1) #Descending Order
for x in my_doc:
    print(x)

#Delete Operations
"""We have 2 options. 
-delete_one() - Deleting specific single record
-delete_many() - Deleting multiple records using regex"""
my_query = {"name" : "John Doe"}
my_query1 = {"name" : {"$regex":"^J"}}

#Deletes all the records starting with the letter 'J'
my_doc = my_col.delete_many(my_query1)
my_doc = my_col.delete_one(my_query)
for y in my_col.find():
    print(y)

