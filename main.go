package main 

import (
    "fmt"
    "C"
    "github.com/v1xingyue/goso/info"
)

//export BoxHello
func BoxHello(message *C.char) *C.char {
    fmt.Println("Hello Box World !")
    info.Hello()
    fmt.Println("this is message ",C.GoString(message))
    return C.CString("this is message from golang !")
}

func main(){}
