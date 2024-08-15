def bankSolution(char, arr, N):
    bankA = 0
    bankB = 0
    initialBankA = 0
    initialBankB = 0

    for i in range(N):
        if char[i] == "A":
            if bankB >= arr[i]:
                bankB -= arr[i]
            else:
              
                shortfall = arr[i] - bankB
                initialBankB += shortfall
                bankB = 0
            bankA += arr[i]

        elif char[i] == "B":
            if bankA >= arr[i]:
                bankA -= arr[i]
            else:
               
                shortfall = arr[i] - bankA
                initialBankA += shortfall
                bankA = 0
            bankB += arr[i]

       

    return [initialBankA, initialBankB]


print(bankSolution("ABAB", [10,5,10,5], 4))
