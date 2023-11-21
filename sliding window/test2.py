import unittest

def soulution(s,t):
    

    list_of_character = [*t]
    copy_t = set(list_of_character)
    min_len = len(s)
    min_len_substring = [0]*len(s)
    substring = set()
    R=0
    min_r=0
    while(R< len(s)):
            
        if(s[R] in copy_t):
            copy_t.remove(s[R])
        if(len(copy_t)<len(list_of_character)):
            substring.add(s[R])

        if(len(copy_t)==0):
            min_len = min(min_len,len(substring))
            if(len(substring)<len(min_len_substring)):
                min_len_substring = substring
                min_r = R
            copy_t = set(list_of_character)
            substring = set()
                #R = R-1

        R = R+1
            
    return s[min_r - len(min_len_substring)+1:]


class Test(unittest.TestCase):
    def test1(self):
        s='ab'
        t='a'
        expected = 'a'
        result = soulution(s,t)
        self.assertEquals(expected,result)

if __name__ == '__main__':
    unittest.main()