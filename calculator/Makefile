objects = main.o addition.o subtraction.o multiplication.o division.o 
op = operations.h

calculator: $(objects)
	cc -o calculator $(objects) $(op) 

$(objects): %.o:%.c
	cc -c $< -o $@

clean:
	rm -f $(objects)

.PHONY: all
