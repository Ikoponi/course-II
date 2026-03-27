# TODO Найдите количество книг, которое можно разместить на дискете
disket = 1.44
pages = 100
stroke = 50
symbols = 25
symbols1 = 4
book = pages * stroke * symbols * symbols1
books = disket*1024*1024//book

print(f"Количество книг, помещающихся на дискету: {books:.0f}")
