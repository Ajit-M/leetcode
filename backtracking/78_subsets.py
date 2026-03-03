#!/usr/bin/python3

"""
    In subset answers lies at the each node of the tree,
    as there is no lenght requirement to satisfy

"""


def subsets(case):
    answer = []


    def backtracking(curr, idx):
        if idx > len(case):
            return 
        
        answer.append(curr[:])
        
        for i in range(idx, len(case)):
            curr.append(case[i])
            backtracking(curr, i+1)
            curr.pop()

    backtracking([], 0)
    return tuple(answer)



def process_case_answer(nums):
    output = set()
    
    for i in nums:
        i = tuple(i)
        if i not in output:
            output.add(i)
    
    return output




def main():
    test_cases = {tuple([1,2,3]): tuple([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
                  
                  }

    for case, result in test_cases.items():
        
        output = subsets(case)
        print(f"Your Answer : {output}\n" 
              f"Correct Answer : {result} \n"
              f"Result : {('Pass' if process_case_answer(result) == process_case_answer(output) else 'Fail')} \n"
              f"===================================== \n")
        
        
    return 


if __name__ == '__main__':
    main()