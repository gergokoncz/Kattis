package main

import (
	"bufio"
	"fmt"
	"os"
	"math"
	"strings"
	"strconv"
)

func med(arr []int, s int) int {
	if (s % 2 == 1) {
		return arr[int((s - 1) / 2)]
	} else {
		return int(math.Floor(float64((arr[int(s / 2)] + arr[int(s / 2 - 1)]) / 2)))
	}
} 

func main() {
	reader := bufio.NewReader(os.Stdin)
	n, _ := reader.ReadString('\n')
	n = strings.Replace(n, "\n", "", -1)
	n_int, _ := strconv.Atoi(n)
	
	// start the actual fun
	for i := 0; i < n_int; i++ {
		// handle m
		m, _ := reader.ReadString('\n')
		m = strings.Replace(m, "\n", "", -1)
		m_int, _ := strconv.Atoi(m)

		// handle numbers
		numbers, _ := reader.ReadString('\n')
		numbers_slice := strings.Fields(numbers)
		nums := make([]int, len(numbers_slice))

		for idx, number := range numbers_slice {
			nums[idx], _ = strconv.Atoi(number)
		}

		// do the actual work
		sum := nums[0]
		sorted := make([]int, 1, len(nums))
		sorted[0] = nums[0]

		for j := 1; j < m_int; j++ {
			is_last := true
			for idx, el := range sorted {
				if (el >= nums[j]) {
					sorted = append(sorted, sorted[len(sorted) - 1])
					for k := len(sorted) - 1; idx <= k; k-- {
						sorted[k] = sorted[k - 1]
					}
					sorted[idx] = nums[j]
					is_last = false
					break
				}
			}
			if (is_last) {
				sorted = append(sorted, nums[j])
			}
			sum += med(sorted, len(sorted))
		}

		fmt.Println(sum)
	}
}