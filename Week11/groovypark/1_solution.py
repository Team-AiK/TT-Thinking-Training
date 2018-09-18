#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
class Solution:
    def producing(self, song, length, total):
        cd_song = total // length  # 한 장의 씨디에 들어갈 곡 수
        # 곡 수보다 들어갈 곡 수가 더 클 때
        if song < cd_song:
            cd_song = song
        # 다음곡으로 넘어갈 때 1초 시간간격
        if (length+1)*(cd_song-1)+length > total:
            cd_song = cd_song - 1
        # 13으로 나누어 떨어지지 않아야 함
        if cd_song % 13 is 0:
            cd_song = cd_song - 1
        # 씨디의 수
        if song % cd_song is 0:
            return song // cd_song
        else:
            return song // cd_song + 1
