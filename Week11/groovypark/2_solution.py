#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def divide(self, width, height, target):
        divisor_pairs = []
        for i in range(1, int(target**(1/2))+1):
            if target % i == 0:
                divisor_pairs.append([i, target//i])
        if width*height == target:
            return 0
        if target % width == 0:
            if target // width < height:
                return 1
        if target % height == 0:
            if target // height < width:
                return 1
        for divisor_pair in divisor_pairs:
            if (divisor_pair[0] < width) and (divisor_pair[1] < height):
                return 2
            if (divisor_pair[1] < width) and (divisor_pair[0] < height):
                return 2
        return -1
