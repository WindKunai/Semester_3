package main

import (
	"fmt"
	"session2/compsys"
)
func Increment(){
	fmt.Println("will increment something")
}
func main() {
	fmt.Printf("Hello, we will try to simulate a CPU\n")
	cpu := compsys.CPU{}
	cpu.RunCycle()

	ops:= compsys.Ops{Incr: Increment}
	ops.Incr()
	/*ops:= compsys.CPU{Funcs: make()} */

}
