def common_friends(list1, list2):
    common = []
    for i in list1:
        for j in list2:
            if i == j:
                common.append(i)

    common.sort()

    return common

def only_first(list1,list2):
    only1 = list1
    for i in list1:
        for j in list2:
            if i == j:
                only1.remove(i)

    only1.sort()

    return only1


ali = ["Aysel", "Murad", "Leyla", "Elvin"]
vali = ["Leyla", "Nigar", "Aysel", "Kamal"]

print(common_friends(ali, vali))
print(only_first(ali, vali))