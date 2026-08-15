class Solution:

    


    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        for s in strs:
            n = len(s)
            res += str(n) + "#" + s 
        
        return res

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        res = []
        curr_idx = 0
        while(curr_idx < len(s)):
            idxDelim = s.index("#", curr_idx)
            lenStr = int(s[curr_idx:idxDelim])
            orig_str = s[idxDelim + 1 : idxDelim + 1 + lenStr]
            res.append(orig_str)
            curr_idx = idxDelim + 1 + lenStr
        
        return res






