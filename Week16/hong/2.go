package main

import (
	"fmt"
	"strings"

)

func solution(phone_book []string) bool {
	for i,val := range phone_book{
		for j,pref := range phone_book{
		if i==j{
		continue
		}
		if strings.HasPrefix(val, pref){
		return false
		}
	}
		
	}
	return true

}
func main() {
	cases := []string{"119", "97674223", "1195524421"}
	fmt.Println(solution(cases))
	
	cases = []string{"123","456","789"}
	fmt.Println(solution(cases))
	
	cases = []string{"12","123","1235","567","88"}
	fmt.Println(solution(cases))
	
}
