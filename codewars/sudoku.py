def valid_solution(arr):
    def check(l1):
        for i in range(8):
            if i + 1 not in l1: return False
        return True
    
    for a in range(3):
        for x in range(3):
            temp = []
            for i in range(3):
                for l in range(3):
                    temp.append(arr[i + 3 * a][x * 3 + l])
            if(check(temp)) == False: return False
            
    for a in range(9):
        if check(arr[a]) == False: return False
        
    for a in range(9):
        temp = []
        for x in range(9):
            temp.append(arr[x][a])
        if check(temp) == False: return False
    return True
