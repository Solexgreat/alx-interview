def canUnlockAll(boxes): 
    row_num = 0
    n = 0
    for row in boxes:
        row_num += 1
        for column in row:
            if column == row_num or column == []:
                result = True
                break
            n = 1
            for i in boxes:
                if n == row_num:
                    break
                for j in i:
                    if j >= column:
                        result = True
                        n += 1
                        break
                    else:
                        result = False
                n += 1            
    return (result)                


         