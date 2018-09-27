package main

import (
	f "fmt"
)

func solution_2(msg string) {
	dict := []string{"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"}
	var msgLength = len(msg)
	answer := ""
	msgfor := 0
	msgback := msgLength
	for {
		for index, val := range dict {
			if val == msg[msgfor:msgback] {
				f.Print(index+1, " ")
				answer = answer + val
				if len(answer) == msgLength {
					return
				}
				dict = append(dict, string(val)+string(msg[msgback]))
				msgfor = msgfor + len(val)
				msgback = msgLength + 1
				break
			}
		}
		msgback--
	}

}

func main() {
	solution_2("KAKAO")
	solution_2("TOBEORNOTTOBEORTOBEORNOT")
	solution_2("ABABABABABABABAB")
}
