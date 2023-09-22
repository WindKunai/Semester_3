// Golang program to illustrate the usage of
// io.MultiWriter() function

// Including main package
package main

// Importing fmt, io, bytes, and strings
import (
	"bytes"
	"fmt"
	"io"
	"strings"
)

// Calling main
func main() {

	// Defining reader using NewReader method
	reader := strings.NewReader("GeeksforGeeks\nis\na\nCS-Portal!")

	// Defining two buffers
	var buffer1, buffer2 bytes.Buffer

	// Calling MultiWriter method with its parameters
	writer := io.MultiWriter(&buffer1, &buffer2)

	// Calling Copy method with its parameters
	n, err := io.Copy(writer, reader)

	// If error is not nil then panics
	if err != nil {
		panic(err)
	}

	// Prints output
	fmt.Printf("Number of bytes in the buffer: %v\n", n)
	fmt.Printf("Buffer1: %v\n", buffer1.String())
	fmt.Printf("Buffer2: %v\n", buffer2.String())
}
