text = "Hello, World!"
target = "l"
modified_text = ""
for char in text:
    if char != target:
        modified_text += char
print("Modified text: ", modified_text)