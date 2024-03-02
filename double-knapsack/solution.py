from typing import List

class Solution:
    def double_knapsack(self, arr: List[int], W1: int, W2: int) -> int:
        dp = [ [ [0] * (W2+1) for _ in range(W1 + 1) ] for _ in range(len(arr)) ]
        print('XXX dp', len(dp), len(dp[0]), len(dp[0][0]))

        for p in range(W1+1):
            print('XXX', p)
            if p >= arr[0]:
                for q in range(W2+1):
                    dp[0][p][q] = arr[0]
                continue
            for q in range(W2 + 1):
                if q >= arr[0]:
                    dp[0][p][q] = arr[0]
        
        for i in range(1, len(arr)):
            for p in range(W1+1):
                if p >= arr[i]:
                    for q in range(W2+1):
                        if q < arr[i]:
                            dp[i][p][q] = max(dp[i-1][p-arr[i]][q] + arr[i], dp[i-1][p][q])
                        else:
                            dp[i][p][q] = max(dp[i-1][p-arr[i]][q] + arr[i], dp[i-1][p][q-arr[i]] + arr[i], dp[i-1][p][q])
                    continue
                for q in range(W2 + 1):
                    if q < arr[i]:
                        dp[i][p][q] = dp[i-1][p][q] 
                    else:
                        dp[i][p][q] = max(dp[i-1][p][q-arr[i]] + arr[i], dp[i-1][p][q])
        return dp[-1][-1][-1]



def main(arr, W1, W2):
    print(f'Input: arr = {arr}, W1={W1}, W2={W2}')
    ret = Solution().double_knapsack(arr, W1, W2)
    print(f'Output: {ret}')

if __name__ == "__main__":
    arr = [8, 3, 2]
    W1 = 10
    W2 = 3
   
    arr = [8, 5, 3]
    W1 = 10
    W2 = 3
    main(arr, W1, W2)
