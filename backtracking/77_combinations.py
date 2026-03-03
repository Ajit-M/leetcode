#!/usr/bin/python3



def combination(nums):
    n = nums[0]
    k = nums[1]
    answer = []


    def backtracking(curr, idx):
        if len(curr) == k:
            answer.append(curr[:])

        
        for i in range(idx, n+1):
            curr.append(i)
            backtracking(curr, i+1)
            curr.pop()
        
    backtracking([], 1)

    return answer


def process_case_answer(nums):
    output = set()
    
    for i in nums:
        i = tuple(i)
        if i not in output:
            output.add(i)
    
    return output



def main():
    n, k = 4,2
    test_cases = {tuple([n,k]): tuple([[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]),
                  
                  }

    for case, result in test_cases.items():
        
        output = combination(case)
        print(f"Your Answer : {output}\n" 
              f"Correct Answer : {result} \n"
              f"Result : {('Pass' if process_case_answer(result) == process_case_answer(output) else 'Fail')} \n"
              f"===================================== \n")
        
        
    return 


if __name__ == '__main__':
    main()