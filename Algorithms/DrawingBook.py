def minPages(n_pages, page):
    start = page//2
    final = n_pages//2 - page//2
    return min([start, final])



n_pages = int(input())
page = int(input())
result = minPages(n_pages, page)
print(result)