package main

import (
	"fmt"
)

func main() {
	var objetivo int

	fmt.Scan(&objetivo)

	fmt.Println(control(objetivo))
}

func control(objetivo int) string {
	resultado := ""

	quatros := 0
	setes := 0

	resto := objetivo

	for {
		if resto >= 4 {
			break
		}

		if resto%7 == 0 {
			setes += resto / 7
			resto -= +7 * (resto / 7)
		}

		if resto >= 4 {
			resto -= 4
			quatros += 1
		}

		resultado += stringGenerator(quatros, "4")
		resultado += stringGenerator(setes, "7")

		if resultado == "" || 0 < resto {
			return "-1"
		} else {
			return resultado
		}
	}
}

func stringGenerator(qtd int, letra string) string {
	result := ""

	for i := 0; i < qtd; i++ {
		result += letra
	}

	return result
}
