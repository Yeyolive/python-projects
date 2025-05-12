
loop = list_items.count;

for i = 0 to loop-1 do:
    
swapped = false

for j = 0 to loop-1 do:

/* compare the adjacent elements */ 

if list_items[j] > list_items[j+1]  then swap( list_items[j], list_items[j+1] ) 

swapped = true

end if 

end for

if(not swapped) thenbreak

end if

end for

end procedure return list_items
