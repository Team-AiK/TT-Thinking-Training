package main

import (
	"fmt"
	"strconv"
	"strings"
)

func decimalToTarget(num int, target int) []string {
	var slice []string

	if num == 0 {
		slice = append(slice, "0")
		return slice
	}
	for i := 0; num > 0; i++ {
		mod := strconv.Itoa(num % target)
		mod = str_mod(mod)
		slice = append(slice, mod)
		num = num / target
	}
	return reverseSlice(slice)
}
func reverseSlice(input []string) []string {
	for i, j := 0, len(input)-1; i < j; i, j = i+1, j-1 {
		input[i], input[j] = input[j], input[i]
	}
	return input
}
func str_mod(input string) string {
	switch input {
	case "10":
		return "A"
	case "11":
		return "B"
	case "12":
		return "C"
	case "13":
		return "D"
	case "14":
		return "E"
	case "15":
		return "F"
	}
	return input
}

func solution(format int, time int, player int, order int) {
	var answer []string
	num := 0
	t := time * player
	for len(answer) < time*player {
		convertVal := decimalToTarget(num, format)
		resJoin := strings.Join(convertVal, "")
		answer = append(answer, resJoin)
		num++

	}
	answersJoin := strings.Join(answer, "")
	answersSplit := strings.Split(answersJoin, "")
	for i := 0; i < t; i++ {
		if i%player == order-1 {
			fmt.Print(answersSplit[i])
		}
	}
	fmt.Println()
}

func main() {
	solution(2, 4, 2, 1)
	solution(16, 16, 2, 1)
	solution(16, 16, 2, 2)

}
