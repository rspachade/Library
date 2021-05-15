from django.shortcuts import render , redirect
from Book.models import Book
from django.http import HttpResponse
# Create your views here.

def homepage(request): # View -function based view(FBV)
    all_books = Book.objects.all().filter(is_deleted='N')
    #all_books = Book.objects.all()

    return render(request,template_name='home.html',context={"books": all_books})

def save_book(request):
    # print("In save book")
    # print(request.POST)#wsgi request
    b_name=request.POST.get("name")
    b_author=request.POST.get("auth")
    b_price=request.POST.get("price")
    b_qty=request.POST.get("qty")
    b_pub=request.POST.get("pub")
    if b_pub == "on":
            flag = True
    else:
            flag = False
    # b_lpe=request.POST.get("lpe")
    # if b_lpe == "on":
    #         flag1 = True
    # else:
    #         flag1 = False
    
    if request.POST.get("id"):#for editing data
        book_obj = Book.objects.get(id=request.POST.get("id"))
        
        book_obj.name = b_name
        book_obj.author = b_author
        book_obj.price = b_price
        book_obj.qty = b_qty
        #book_obj.lpe.= b_lpe
        book_obj.is_published = flag
        #book_obj.low_priced=flag1
        book_obj.save()
        return redirect('Welcome') 
    else:
    # print(b_name,b_author,b_price,b_qty,b_pub)
        b = Book(name = b_name, author = b_author, price = b_price, qty = b_qty, is_published = flag)
        b.save()
        return redirect('Welcome')#switch  on home page

def edit_book(request, id):
    try:
        book_obj = Book.objects.get(id=id)
    # print(type(book_obj))
    # return redirect('Welcome')
    except Exception:
        msg = f"No Book Found for id: {id}"
        return HttpResponse(msg)
    #all_books = Book.objects.all().filter(is_deleted='N')
    all_books = Book.objects.all()
    return render(request,template_name='home.html',context={"book": book_obj, "books" : all_books })

def delete_book(request, pk):
    book_obj= Book.objects.get(id=pk)
    # book_obj.delete()
    book_obj.is_deleted = 'Y'
    book_obj.save()
    return redirect('Welcome')

def permanant_delete_book(request, pk):
    book_obj= Book.objects.get(id=pk)
    # book_obj.delete()
    book_obj.delete()
    return redirect('Welcome')

def restore_book(request,id):
    book_obj= Book.objects.get(id=id)
    book_obj.is_deleted="N"
    book_obj.save()
    return redirect('Welcome')

def restore_all(request):
    book_obj= Book.objects.all()
    for i in range(len(book_obj)):
        book_obj[i].is_deleted="Y"
        book_obj[i].save()

    return redirect('Welcome')


def delete_all(request):
    book_obj= Book.objects.all()
    # book_obj.delete()
    book_obj.is_deleted="N"
    book_obj.delete()
    return redirect('Welcome')


def show_deleted_data(request):
    all_deleted_books= Book.inactive_objects.all()
    return render(request,template_name='home.html',context= { "books" : all_deleted_books })