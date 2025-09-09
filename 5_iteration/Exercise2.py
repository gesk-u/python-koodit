# Empty list
items = []
# Ask for items
item_buy = input("Add to my list: ")
while item_buy != "":
    items.append(item_buy)  #Append the list of items
    item_buy = input("Add another item to your list: ")

# Print written list
print("Your list:", items)

# Ask to remove bought item from the list
item = input("Remove: ")

while item != "":
    if item in items:
        items.remove(item)  # Remove 'item' from 'items'
        # if list is empty: break the list
        if len(items) < 1:
            print("You’ve bought everything you wanted!")
            break
        # print items that remaining items
        else:
            print(items)
            item = input("Remove another item to your grocery list: ")
    else:
        print("You do not have this item in your list")

    item = input("Remove another item from your grocery list (or press Enter to finish): ")

