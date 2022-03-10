def solution(inputArray):
    
    strings, matches = {}, {}
    
    for string in inputArray:
        
        if string not in strings:
                strings[string] = [0]
        strings[string][0] += 1
                
        for i in range(len(string)):
            
            new_string = string[:i] + '.' + string[i+1:]
            
            if new_string not in matches:
                matches[new_string] = []

            matches[new_string].append(string)
            strings[string].append(new_string)

    def rearrangement(strings, matches, string, count, total):
        
        possible_matchs = strings[string][1:]
        
        for match in possible_matchs:
            possible_strings = matches[match]
            
            for s in possible_strings:

                if string != s and strings[s][0] > 0:
                    strings[string][0] -= 1
                    rearrange = rearrangement(strings, matches, s, count+1, total)
                    print(rearrange)
                    if rearrange[0] == True:
                        return rearrange
                    else:
                        strings[string][0] += 1
        
        if count == total:
            return [True, count]  
            
        return [False, count-1]
    
    for string in inputArray:
        count, total = 1, len(inputArray)
        rearrange = rearrangement(strings, matches, string, count, total)
        if rearrange[0] == True:
            return True
    
    return False
