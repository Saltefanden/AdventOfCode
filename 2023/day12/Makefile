
CFLAGS=-fsanitize=address

all: a.out


a.out: sol.c
	$(CC) $(CFLAGS) $?

.PHONY: clean test run
test: a.out
	@./a.out testinput

run: a.out
	@./a.out input
clean: 
	rm ./a.out
