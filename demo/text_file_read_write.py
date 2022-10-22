from lessline.text_file import read, write

file = './demo/demo.txt'
text = 'Hello word!\nThis is lessline!'
write(text, file)

text_new = read(file)
print(len(text_new), text_new)
