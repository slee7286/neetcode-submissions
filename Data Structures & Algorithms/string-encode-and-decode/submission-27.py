class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            char_loc = s.find("#", i)
            length = int(s[i:char_loc])
            decoded.append(s[char_loc+1:char_loc+1+length])
            i = char_loc+1+length
        return decoded