from django.shortcuts import render
from django.http import HttpResponse 




def index(n):

    movies_name = [ ]
    id = []
    name = [ ]
    hello = open('customer.txt','r') 
    mahi = hello.readlines()
    for i in range (len(mahi)):
        penny = mahi[i].split(',')
        id.append(penny[0])
        name.append(penny[1])
    movie_name = open('movies.txt','r')
    mo_name = movie_name.readlines()
    for i in range (len(mo_name)):
        nav = mo_name[i].split(',')
        movies_name.append(nav[1])
    return render(n,"movie_rental/index.html",{"id":id,"name":name, "movies_name": movies_name})
 
def customer(r):
    name = 'Adam'
    customer_details = open('customer.txt','r')
    values = customer_details.readlines()
    for i in values:
        single_customer = i.split(',')
        if single_customer[1] == name:
            break
    return render(r,"movie_rental/customer.html",{"single_customer":single_customer})


def movie(b):
    name = 'Avengers'
    movie_details = open('movies.txt','r')
    values = movie_details.readlines()
    for i in values:
        single_movie = i.split(',')
        if single_movie[1] == name:
            break
    return render(b,"movie_rental/movie.html",{"single_movie":single_movie})
    