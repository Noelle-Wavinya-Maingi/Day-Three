def solution(S):

    #Check if S only contains lowercases
    if not S.islower():
        return "String S must only contian lowercase letters!"
    
    #Initialize an empty dictionary
    frequency = {}

    #Iterates of N characters to get its occurence in S and stores it in the frequency dictionary.
    for N in S:
        frequency[N] = frequency.get(N, 0) + 1

    count = 0

    #Iterates through the values in the dictionary and checks if its odd or even. If odd it increments the count to know how many values have odd numbers.
    for f in frequency.values():
        if f % 2 != 0:
            count += 1
    return count

#Test cases
print(solution("acbcbba"))
print(solution("aaaa"))
print (solution("axxaxa"))
print(solution("AAVVSA"))