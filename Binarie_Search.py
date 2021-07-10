def binarie_search(array,item, begin=0, end=None):
    if end is None:
        end= len(array)-1
    if begin<= end:
        m = (begin+end)//2
        if array[m]==item:
            return print('O elemento está na lista na posição',m)
        if item< array[m]:
            return binarie_search(array,item, begin, m-1)
        if item>array[m]:
            return binarie_search(array,item, m+1,end)
        return None
lista= [0,1,2,3,4,5,6,7]
binarie_search(lista, 5,)    

