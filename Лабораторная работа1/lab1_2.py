# TODO Найдите количество книг, которое можно разместить на дискете
ch_in_book = 100*50*25
volume_book = (ch_in_book*4)/1024/1024
kol_book = 1.44//volume_book
book = int(kol_book)
print("Количество книг, помещающихся на дискету:", book)
