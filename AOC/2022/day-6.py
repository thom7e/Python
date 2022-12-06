
# Parsing
with open("day-6.in") as d:
    letters = d.read().splitlines()

def part_1():

    for index in range(len(letters)):
        marker = []
        for indexx, marker_search in enumerate(letters[index]): # we do enumerate to get the index of the duplicates

            if marker_search in marker[:indexx]: # we slice the search-field to the index
                for indexy, search in enumerate(marker[:indexx]): # we enumerate again to geht the index of the duplicate in the main-string
                    if search == marker_search: #loop to get the right index
                        marker = marker[indexy+1:] #slice the marker-list to the index of the duplicate

                marker.append(marker_search) # add the sliced letter again


            else:
                marker.append(marker_search) # add the normal letter

            if len(marker) == 4: # check, if the marker has 4 positions
                print(f"Der Marker ist {marker}")
                return indexx+1 #return the index +1 to get the position

def part_2():
    for index in range(len(letters)):
        marker = []
        for indexx, marker_search in enumerate(letters[index]):

            if marker_search in marker[:indexx]:
                for indexy, search in enumerate(marker[:indexx]):
                    if search == marker_search:
                        marker = marker[indexy+1:]
                marker.append(marker_search)

            else:
                marker.append(marker_search)

            if len(marker) == 14:
                print(f"Der Marker ist {marker}")
                return indexx+1


print(f"PART I {part_1()}")
print(f"PART II {part_2()}")