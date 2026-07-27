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
    pE = 0
    r = 0
    m = {}

    for pD in range(len(s)):
        if s[pD] not in m:
            m[s[pD]] = pD
        else:
            pE = min(max(pE, m[s[pD]] + 1),pD) 
            m[s[pD]] = pD
        r = max(r, pD - pE + 1)

    return r
                  
print(lengthOfLongestSubstring("abba")) # 0
