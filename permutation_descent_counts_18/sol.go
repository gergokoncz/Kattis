package main

import(
	"bufio"
	"fmt"
	"os"
	s "strings"
	"strconv"
)

var ans int;

func perm(a []int, i int, req int) {
	if i > len(a) {
		if desc_n(a, req){
			ans++
			ans = ans % 1001113
		}
		return
	}
	perm(a, i+1, req)
	for j := i+1; j < len(a); j++ {
		a[i], a[j] = a[j], a[i]
		perm(a, i+1, req)
		a[i], a[j] = a[j], a[i]
	}
}

func desc_n(a []int, req int) bool {
	d := 0
	for i := 0; i < len(a) - 1; i++ {
		if a[i] > a[i+1] {
			d++
			if d > req {
				return false
			}
		}
	}
	return d == req
}

func main() {
	var n int
	reader := bufio.NewReader(os.Stdin)
	_,_ = fmt.Scanf("%d\n", &n)
	// for cases do this
	for i := 0; i < n - 1; i++ {
		// read line process vars
		l, _ := reader.ReadString('\n')
		l = s.Replace(l, "\n", "", -1)
		nums := s.Split(l, " ")
		clen, _ := strconv.Atoi(nums[1])
		des_req, _ := strconv.Atoi(nums[2])
		ans = 0
		// create array to permutate
		arr := make([]int, clen)
		for i, _ := range arr {
			arr[i] = i+1
		}
		perm(arr, 0, des_req)
		fmt.Printf("%s %d\n", nums[0], ans)
	}
}
