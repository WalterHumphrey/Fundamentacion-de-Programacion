
"""
Write a function ``print_triangular_numbers(n)`` that prints out the first
n triangular numbers. A call to ``print_triangular_numbers(5)`` would
produce the following output::

    1       1
    2       3
    3       6
    4       10
    5       15

(*hint: use a web search to find out what a triangular number is.*)
"""

def print_triangular_numbers(n):
    # your code here
    T = (n*(n+1))/2
    print(T)
    
def main():
    num = int(input("Ingrese un numero entero:"))
    triangle = print_triangular_numbers(num)
    
if __name__ == "__main__": #Correr el programa principal
    main()    
