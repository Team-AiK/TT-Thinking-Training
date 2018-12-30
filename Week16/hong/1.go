package main

import (
	"fmt"
)

func solution(participant []string, completion []string) {
	mapParticipant := make(map[string]int)
	for _, val := range participant {
		mapParticipant[val]++
	}

	for _, val := range completion{
		mapParticipant[val]--
	}
	for key, val := range mapParticipant{
		if val > 0{
		fmt.Println(key)
		return 
		}
	}
}
func main() {
	participant := []string{"leo", "kiki", "eden"}
	completion := []string{"eden", "kiki"}
	solution(participant, completion)
	
	participant = []string{"marina", "josipa", "nikola", "vinko", "filipa"}
	completion = []string{"josipa", "filipa", "marina", "nikola"}
	solution(participant, completion)
	
	participant = []string{"mislav", "stanko", "mislav", "ana"}
	completion = []string{"stanko", "ana", "mislav"}
	solution(participant, completion)
	
}
