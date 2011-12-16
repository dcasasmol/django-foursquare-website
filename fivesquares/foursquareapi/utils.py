import urllib2
import json

def get_data(url):
    open = urllib2.urlopen(url)
    line = open.readlines()[0]
    data = json.loads(line)
    return data['response']['venues']

def show_data(mylist, indent=1, level=0):
    for item in mylist:
        if isinstance(item,list):
            show_data(item,indent,level+1)
        else:
            if indent:
                for tab in range(level):
                    print "\t"
            print item

def order_data(lista):
  ordena_quicksort(lista,0,len(lista)-1)
  return lista

def ordena_quicksort(lista,izdo,dcho):
  if izdo<dcho:
    pivote=lista[(izdo+dcho)/2]['location']['distance']
    i,d=izdo,dcho
    while i<=d :
      while lista[i]['location']['distance']<pivote : i+=1
      while lista[d]['location']['distance']>pivote : d-=1
      if i<=d :
        lista[i]['location']['distance'],lista[d]['location']['distance']=lista[d]['location']['distance'],lista[i]['location']['distance']
        i+=1
        d-=1
    if izdo<d : ordena_quicksort(lista,izdo,d)
    if i<dcho : ordena_quicksort(lista,i,dcho)
  return lista