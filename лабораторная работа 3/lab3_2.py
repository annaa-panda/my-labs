# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, c='|'):
    gr1=set(participants_first_group.split(c))
    gr2=set(participants_second_group.split(c))

    com=gr1.intersection(gr2)
    com=sorted(list(com))
    print(com)
    return com

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group,participants_second_group)