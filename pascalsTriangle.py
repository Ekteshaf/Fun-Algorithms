#returns value of a number on pascals triangle given its row and column position
def pascalValue(row,column):
    if row==0 or column==0 or column==row:
        return 1
    return pascalValue(row-1,column-1)+pascalValue(row-1,column)

print(pascalValue(3,3))
