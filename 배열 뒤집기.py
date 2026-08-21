def solution(num_list):
    list = []
    for i in range(len(num_list),0,-1):
        list.append(num_list[i-1])
    return list