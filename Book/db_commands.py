from Book.models import Book

'''# All Data
all_data = Book.objects.all()
print(all_data)

# single data
sid=1
b1=Book.objects.get(id=sid)
print(b1)
print("*" * 40)

#create data--insert into table
b2=Book.objects.create(name="Java Programming",author="Mid ken joy",qty=12,price=750)
print(b2)
print(b2.id)

print("*" * 40)

#update
sid=5
b3=Book.objects.get(id=sid)
b3.name="AI for You"
b3.author="Rahul"
b3.qty=23
b3.save()
print()
print("*" * 40)
print("Multiple feilds update in one attempt")
sid1=7
b4=Book.objects.get(id=sid)
b4=Book(name="Advance computing",author="Manomay ")
print("Added into database",b4)
print("*" * 40)

#Delete
sid=4
b5=Book.objects.get(id=sid)
b5.delete()
print("Record deleted ",b5)


# to run this  file in db shell
# exec(open("Filepath").read())
#exec(open('D:\\Python Data\\Django\\Library\\Book\\db_commands.py').read())

all_data = Book.objects.all()
#print(all_data)
#showing data from database
print(type(all_data))
for book in all_data:
    print(f"-------Book Details for Book ID  {book.id}---------") #book is an object  not record 
    print(f"Book Name  : {book.name}")
    print(f"Author     : {book.author}")
    print(f"Quantity   : {book.qty}")
    print(f"Book Price : {book.price}")

#updating data
for book in all_data:
    book.qty=18
    book.save()
    book.delete() #for deleting 
#showing/retriving data
for book in all_data:
    print(f"-------Book Details for Book ID  {book.id}---------") #book is an object  not record 
    print(f"Book Name  : {book.name}")
    print(f"Author     : {book.author}")
    print(f"Quantity   : {book.qty}")
    print(f"Book Price : {book.price}")
'''

# all_data = Book.objects.all().values('id','name','price')
# print(all_data)#list of dict

# all_data1=Book.objects.values_list()
# print(all_data1)#list of tuples


#create data--insert into table
import random
'''for i in range(1,37):
    sb2=Book.objects.create(name=chr(random.randint(65, 90))*3 +" for you ",author="Maxwell princ "+ chr(random.randint(65,90))*5,qty =random.randint(13,35),price=random.randint(550,899))
    print(list(all_data))
'''
#django cookbook refer

# '''print(f" single element {all_data[0]}")
# for i in all_data:
#     #print(all_data)
#     print(i)
# '''
# books=Book.objects.filter(id__gte=55).values("id","name")
# books=Book.objects.all().order_by(".name")
# print(books)
# for i in books:
#     print(i)

'''b = Book.objects.all().count()
print(b)
d=Book.objects.bulk_create([
Book(name="Javac",author="Abc",qty=17,price=567),
Book(name="AJava",author="Abc",qty=17,price=567),
Book(name="JavaA",author="Abc",qty=17,price=567),
Book(name="JavBa",author="Abc",qty=17,price=567),
Book(name="lang",author="Abc",qty=17,price=567),
Book(name="dynamic",author="Abc",qty=17,price=567)
])
print(type(d))
'''


