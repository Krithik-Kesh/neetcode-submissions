class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for i in strs:
            encode.append(str(len(i)) + "#" + i)
        return "".join(encode)
    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            decode.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return decode
