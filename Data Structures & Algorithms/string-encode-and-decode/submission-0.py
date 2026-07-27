class Solution:
    def encode(self, strs: List[str]) -> str:
      encoded_string = ""
      for s in strs:
        encoded_string += str(len(s)) + "#" + s
      return encoded_string
      

    def decode(self, s: str) -> List[str]:
      decoded_string = []
      i = 0
      while i < len(s):
        j = i
        while s[j]!= "#":
          j += 1
        length = s[i:j]

        string = s[j+1: j+1+int(length)]
        decoded_string.append(string)
        
        i = j + 1 + int(length)
      return decoded_string 