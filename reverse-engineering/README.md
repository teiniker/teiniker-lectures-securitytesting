# Reverse Engineering 

Reverse Engineering **examines an executable file** for information about implementation and design. 
Attackers use this technique to **find potential vulnerabilities** in a software project.

There are two ways of reverse engineering:
* The **static analysis** will examine the binary file without starting the program. 
  In addition to the stored data, the control flows of the implementation are particularly interesting.
  
* The **dynamic analysis** explores the running program. 
  Here, the interactions with its environment and the data flows inside the software system are in the foreground.

## Tools Setup 
Many reverse engineering tools are supplied with regular Linux distributions, others have to be installed later.
* [Ghidra](setup/Ghidra.md)
* [Hopper](setup/Hopper.md)

## Examples

* **Static Analysis**
  * [secret-static](analysis-static/secret-static)  
  * Exercise: [password-check](analysis-static/password-check-exercise) ([Model Solution:](analysis-static/password-check))
  * Exercise: [password-encryption](analysis-static/password-encryption-exercise) ([Model Solution:](analysis-static/password-encryption))
  * [secret-static-stripped](analysis-static/secret-static-stripped)
  
* **Dynamic Analysis**
  * [secret-dynamic](analysis-dynamic/secret-dynamic)
  * [database-calls](analysis-dynamic/database-access)
  * [file-access](analysis-dynamic/file-access)
  * [file-access-stripped](analysis-dynamic/file-access-stripped)
  * [secret-anti-debug](analysis-dynamic/c-secret-anti-debug)
 
                        
## References:
* Jon Erickson. **Hacking - The Art of Exploitation**. No Starch Press, 2nd Edition, 2008
* Daniel Regalado, Shon Harris, Allen Harper, Chris Eagle, Jonathan Ness, Branko Spasojevic, Ryan Linn, Stephen Sims. **Gray Hat Hacking**. McGraw Hill Education, 4th Edition, 2015
* Ryan O’Neill. **Learning Linux Binary Analysis**. Packt Publishing, 2016

*Egon Teiniker, 2020-2022, GPL v3.0*
