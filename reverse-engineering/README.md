# Reverse Engineering 

Reverse Engineering **examines an executable file** for information about implementation and design. 
Attackers use this technique to **find potential vulnerabilities** in a software project.

There are two ways of reverse engineering:
* The **static analysis** will examine the binary file without starting the program. 
  In addition to the stored data, the control flows of the implementation are particularly interesting.
  
* The **dynamic analysis** explores the running program. 
  Here, the interactions with its environment and the data flows inside the software system are in the foreground.

## Examples

* **Static Analysis**
  * [secret](https://github.com/teiniker/teiniker-lectures-securitytesting/tree/main/reverse-engineering/c-secret)  
  
* **Dynamic Analysis**
  * [file-access](https://github.com/teiniker/teiniker-lectures-securitytesting/tree/main/reverse-engineering/c-file-access)
  * [database-calls](https://github.com/teiniker/teiniker-lectures-securitytesting/tree/main/reverse-engineering/c-database-access)
  * [secret](https://github.com/teiniker/teiniker-lectures-securitytesting/tree/main/reverse-engineering/c-secret)
  * [secret-anti-debug](https://github.com/teiniker/teiniker-lectures-securitytesting/tree/main/reverse-engineering/c-secret-anti-debug)
  
## Tools Setup 
Many reverse engineering tools are supplied with regular Linux distributions, others have to be installed later.
* [Hopper](https://github.com/teiniker/teiniker-lectures-securitytesting/tree/main/reverse-engineering/setup/Hopper.md)
* [Ghidra](https://github.com/teiniker/teiniker-lectures-securitytesting/tree/main/reverse-engineering/setup/Ghidra.md)

                        
## References:
* Jon Erickson. **Hacking - The Art of Exploitation**. No Starch Press, 2nd Edition, 2008
* Daniel Regalado, Shon Harris, Allen Harper, Chris Eagle, Jonathan Ness, Branko Spasojevic, Ryan Linn, Stephen Sims. **Gray Hat Hacking**. McGraw Hill Education, 4th Edition, 2015
* Ryan O’Neill. **Learning Linux Binary Analysis**. Packt Publishing, 2016

*Egon Teiniker, 2020-2021, GPL v3.0*
