#!/usr/bin/python3

"""
    In Permutation the answers lies at the leaf of the tree,
    as we have the lenght requirement

"""


def permute(case):
    answer = []
    
    def backtracking(curr):
        if len(curr) == len(case):
            answer.append(curr[:])
            return

        for i in case:
            if i not in curr:
                curr.append(i)
                backtracking(curr)
                curr.pop()

    for i in case:
        curr = []
        curr.append(i)
        backtracking(curr)
        curr.pop()
    
    return tuple(answer)

    



def main():
    test_cases = {tuple([1,2,3]): tuple([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
                  
                  }

    for case, result in test_cases.items():
        
        output = permute(case)
        print(f"Your Answer : {output}\n" 
              f"Correct Answer : {result} \n"
              f"Result : {('Pass' if result == output else 'Fail')} \n"
              f"===================================== \n")
        
        
    return 


if __name__ == '__main__':
    main()