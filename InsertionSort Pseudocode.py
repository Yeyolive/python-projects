procedure insertionSort( list_items : array of items )

int holePosition

int valueToInsert

for i = 1 to length(list_items) inclusive do:
    
valueToInsert = list_items[i]
holePosition = i

while holePosition > 0 and list_items[holePosition-1] > valueToInsert do:
    
list_items[holePosition] = list_items[holePosition-1]
holePosition = holePosition -1

end while

list_items[holePosition] = valueToInsert

end for
end procedure
