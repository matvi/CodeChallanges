
import unittest


def solution(a):
    valid = True
    stack = []
    for i in a:
        if i == "{" or i == "[" or i =="(":
            stack.append(i)
        elif i == "}":
            valid = False if not stack or stack.pop() != "{" else True 
            
        elif i == "]":
            valid = False if not stack or stack.pop() != "[" else True
        elif i == ")":
            valid = False if not stack or stack.pop() != "(" else True
        #check if valid has change 
        if valid == False :
            return 0
    return 1 if not stack and valid else 0


class TestStack(unittest.TestCase):
    
    def test1(self):
        a = ['{','[',']','}','(',')']
        res = solution(a)
        self.assertEqual(res, 1, "Should be 1")

    def test2(self):
        a = ['{',')',']','}','(',')']
        res = solution(a)
        self.assertEqual(res, 0, "Should be 0")

    def test3(self):
        a = ['{','{','{','{','{','{']
        res = solution(a)
        self.assertEqual(res, 0, "Should be 0")

if __name__ == "__main__":
    print("testing")
    unittest.main()
    #a = ['{',')',']','}','(',')']
    #res = solution(a)
    

            