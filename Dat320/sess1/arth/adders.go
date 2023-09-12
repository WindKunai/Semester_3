package arth

func add(x int, y int) int {
	return x + y
}
func Add(x int, y int) *int {
	r := add(x, y)
	return &r
}
