def designerPdfViewer(h, word):
    A_ANSI_CODE = 97
    word_size = len(word)
    max_h = 0

    for letter in word:
        index = ord(letter) - 97
        height = h[index]
        if height > max_h:
            max_h = height
    
    return word_size*max_h


h = list(map(int, input().rstrip().split()))
word = input()
result = designerPdfViewer(h, word)
print(result)