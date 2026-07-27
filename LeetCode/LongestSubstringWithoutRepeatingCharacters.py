def primeira(s):
        memo = []
        contagem = 1

        if s == "":
            return 0

        for i in range(len(s)):
            for j in range(i,len(s)):
                if s[j] in memo:
                    if len(memo) > contagem:
                        contagem = len(memo)
                    memo = []
                    break
                else:
                    memo.append(s[j])
        return contagem

def lengthOfLongestSubstring(s):
    memo = []
    
    return 0
   
                  
print(lengthOfLongestSubstring(" ")) # 0