chapters = ["Ultramrines", "Dark Angels", "Lamenters", "Blood Angels", "Alpha Legion", "Black Legion", "Night Lords"]

# It turns the list into a string
# print(", ".join(chapters))

# Join() is an iterator by itself. It doesn't need a for loop to operate on a list.
# ALL ITEMS MUST BE STRINGS

nested_chapters = [["Ultramrines", "Dark Angels", "Lamenters", "Blood Angels"], ["Alpha Legion", "Black Legion", "Night Lords"]]
seperator = ' | '
for faction in nested_chapters:
    print(faction)
    output = seperator.join(faction)
    # for chapter in faction:
    #     print(chapter)
    #     string = string.join(chapter)

print(output)
