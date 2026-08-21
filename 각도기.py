def solution(angle):
    if angle < 90:
        return 1
    elif angle == 90:
        return 2
    return angle // 90 + 2