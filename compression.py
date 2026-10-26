text = input("Enter text: ")
compressed = ""
i = 0
while i < len(text):
 count = 1
 while i + count < len(text) and text[i] == text[i + count]:
  count += 1
 compressed += text[i] + str(count)
 i += count
print("Original text:", text)
print("Compressed text:", compressed)