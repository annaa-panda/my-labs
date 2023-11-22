# TODO Напишите функцию для поиска индекса товара
def fruits_list_index (items_list,find_item):
    fruit_index = items_list.index(find_item)
    return  fruit_index
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    if find_item in items_list:
        index_item = fruits_list_index(items_list,find_item)
    else: # TODO Вызовите функцию, что получить индекс товара
        index_item = None
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
