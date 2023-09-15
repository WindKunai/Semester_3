package compsys

import (
	"fmt"
	
)


type Ops struct{
	
	// Funcs map[int]func(){
	//}
	Incr func()
	Mul func()
	Store func()
}

func Incr (ops *Ops){

}

type IR struct {
	OpCode 	int

}


type CPU struct {
	IReg IR 
}

func (cpu *CPU) RunCycle() {
	cpu.Fetch()
	cpu.Decode()
	cpu.Execute()
}

func (cpu *CPU) Fetch() {
	fmt.Printf("Fetching\n")

	cpu.IReg.OpCode = 1
}

func (cpu *CPU) Decode() {
	fmt.Printf("Decoding\n")
}

func (cpu *CPU) Execute() {
	fmt.Printf("Executing\n")
}
