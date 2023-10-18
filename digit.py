def solution(S):

    max_sum = 0

     #Iterate all possible starting positions if the two digit fragment
    for i in range(len(S) - 1):

        #Iterate over possible starting positions of the second fragment
        for j in range(i + 2, len(S)):
            #Get the first fragment and convert it to an integer
            fragment1 = int(S[i : i + 2])

            #Check if the second fragment starting position is within the bound
            if j < len(S):
                #Get the second fragment and covert it to an integer
                fragment2 = int(S[j : j + 2])

                #Check if the fragments dont overlap
                if i + 2 <= j:
                    max_sum = max(max_sum, fragment1 + fragment2)

    return max_sum

print(solution("43798"))  # Output: 141
print(solution("00101"))  # Output: 10
print(solution("0332331"))  # Output: 66
print(solution("00331"))  # Output: 34