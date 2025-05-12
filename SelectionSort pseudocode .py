

for i = 1 to n - 1

min = i 

for j = i+1 to n

if list_items[j] < list_items[min]

then min = j;

end if

end for

if indexMin != i then

swap list_items[min] and list_items[i]

end if

end for

end procedure

























