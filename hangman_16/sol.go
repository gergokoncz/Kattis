package main

import (
	"bufio"
	"fmt"
	"strings"
	"os"
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	w, _ := reader.ReadString('\n')
	w = strings.Replace(w, "\n", "", -1)
	g, _ := reader.ReadString('\n')
	g = strings.Replace(g, "\n", "", -1)
	e := 0
	// now loop
	for i := range g {
		if strings.Contains(w, string(g[i])) {
			w = strings.Replace(w, string(g[i]), "", -1)
			if w == "" {
				fmt.Println("WIN")
				break
			}
		} else {
			if e +=1; e == 10 {
				fmt.Println("LOSE")
				break
			}
		}
	}
}
