def encrypt(org, key):
  result = ''
  for c in org:
    if 'A' <= c <= 'Z':
      ascii = ord(c)
      base = ord('A')
      ascii = (ascii - base + key) % 26 + base
      c = chr(ascii)
    elif 'a' <= c <= 'z':
      ascii = ord(c)
      base = ord('a')
      ascii = (ascii - base + key) % 26 + base
      c = chr(ascii)
    result += c
  return result
def decrypt(org, key):
  return encrypt(org, key * -1)

print(decrypt('Clguba', 1))
for key in range(26):
    print(decrypt('Clguba',key))
