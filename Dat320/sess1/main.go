package main

import (
	"fmt"
	"main.com/arth"
	"time"
)

func main() {
	fmt.Printf("This is my first print \n")
	fmt.Printf("The time is", time.Now(),"\n")
	fmt.Printf("---- Lets call a package ------\n")
	}

	var x int = 10
	var p *int = &x

	y := 2
	d := arth.Add(x,y)
	fmt.Printf("result &d", *d)