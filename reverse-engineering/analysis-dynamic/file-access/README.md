# Example: File Access - Tracing System Calls  

We try to guess the right password for the user `student`:
```
$ ./file_login 
username> student
password> student
Login rejected!
```

From the given source code we can see that file_login reads user 
credentials from a file.
```C
bool is_valid_user(char* username, char* password)
{
    char _username[256];
    char _password[256];
    FILE *fp;
    fp = fopen("application-users.config", "r");
    if (fp == NULL) 
    {
        fprintf(stderr, "Can't open passwords.txt file!\n");
        return false;
    }
    
    while(fscanf(fp, "%s %s", _username, _password) != EOF)
    {
        if(strcmp(username,_username) == 0
            && strcmp(password,_password) == 0)
        {
            fclose(fp);
            return true;
        }
    }
    fclose(fp);
    return false;
}
```

## Using strace

Note that **file access is based on system calls** (open, write, read, close)
so we can use **strace** to find out more.
```
$ ./file_login 
username> 
```

In parallel, open a terminal and check the running processes:
```
$ ps -a
  PID TTY          TIME CMD
 2580 pts/0    00:00:00 file_login   <== PID
 2589 pts/2    00:00:00 ps

$ strace -p 2580 -s 1024
```
 
Now let's continue with the login.
```
username> student
password> student
Login rejected!
```

Same result as before, but have a look on the strace output:
```
read(0, "student\n", 1024)              = 8
write(1, "password> ", 10)              = 10
read(0, "student\n", 1024)              = 8
brk(0)                                  = 0x89e5000
brk(0x8a06000)                          = 0x8a06000
brk(0)                                  = 0x8a06000
open("application-users.config", O_RDONLY) = 3
fstat64(3, {st_mode=S_IFREG|0664, st_size=39, ...}) = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7770000
read(3, "student de1d9228df\nteacher 96c2d1049a\n\n", 4096) = 39
read(3, "", 4096)                       = 0
write(1, "Login rejected!\n", 16)       = 16
exit_group(0)                           = ?
```

Here we can see the file access operations in detail:
```
open("application-users.config", O_RDONLY) = 3
read(3, "student de1d9228df\nteacher 96c2d1049a\n\n", 4096) = 39
```

So, let's try `de1d9228df` as the password:
```
$ ./file_login 
username> student
password> de1d9228df
Welcome, student!
```

And also use the following credentials `teacher/96c2d1049a`
```
$ ./file_login 
username> teacher
password> 96c2d1049a
Welcome, teacher!
```

_Exercise_: Make the same experiment but use **ltrace** instead of strace.


## Using gdb

We disassemble `main()` and set a breakpoint after the call to `is_valid_user()`.

```
(gdb) disass main
Dump of assembler code for function main:
   0x0000555555555291 <+0>:	    push   %rbp
   0x0000555555555292 <+1>:	    mov    %rsp,%rbp
    ...
   0x0000555555555302 <+113>:	mov    %rdx,%rsi
   0x0000555555555305 <+116>:	mov    %rax,%rdi
   0x0000555555555308 <+119>:	call   0x5555555551a5 <is_valid_user>
   0x000055555555530d <+124>:	test   %al,%al              # <= breakpoint!!!!!
   0x000055555555530f <+126>:	je     0x55555555532e <main+157>
   0x0000555555555311 <+128>:	lea    -0x100(%rbp),%rax
   0x0000555555555318 <+135>:	mov    %rax,%rsi
   0x000055555555531b <+138>:	lea    0xd50(%rip),%rdi        # 0x555555556072
   0x0000555555555322 <+145>:	mov    $0x0,%eax
   0x0000555555555327 <+150>:	call   0x555555555060 <printf@plt>
   0x000055555555532c <+155>:	jmp    0x55555555533a <main+169>
   0x000055555555532e <+157>:	lea    0xd4b(%rip),%rdi        # 0x555555556080
   0x0000555555555335 <+164>:	call   0x555555555040 <puts@plt>
   0x000055555555533a <+169>:	mov    $0x0,%eax
   0x000055555555533f <+174>:	leave  
   0x0000555555555340 <+175>:	ret    
End of assembler dump.
(gdb) break *0x000055555555530d
Breakpoint 1 at 0x55555555530d: file file_login.c, line 42.
```
Now, we run the program and hold at the breakpoint.

```
(gdb) run

Starting program: c-file-access/file_login 
username> student
password> student

Breakpoint 1, main () at file_login.c:42

(gdb) disass
Dump of assembler code for function main:
   0x0000555555555291 <+0>:	    push   %rbp
   0x0000555555555292 <+1>:	    mov    %rsp,%rbp
    ...
   0x0000555555555302 <+113>:	mov    %rdx,%rsi
   0x0000555555555305 <+116>:	mov    %rax,%rdi
   0x0000555555555308 <+119>:	call   0x5555555551a5 <is_valid_user>
=> 0x000055555555530d <+124>:	test   %al,%al
   0x000055555555530f <+126>:	je     0x55555555532e <main+157>
   0x0000555555555311 <+128>:	lea    -0x100(%rbp),%rax
    ...
End of assembler dump.

(gdb) p $al
$1 = 0

(gdb) set $al=1

(gdb) continue
Continuing.
Welcome, student!
```

We print the content of the of the `al` register and change it to `1`.
When we continue the execution, we are logged in!

Note that we did not know the password, we just changed the outcome of the 
`is_valid_user()` function which is used to check if an entered password is valid.


## References:
* [strace](https://strace.io/)

* [The strace Command in Linux](https://www.baeldung.com/linux/strace-command)

*Egon Teiniker, 2020-2021, GPL v3.0* 
