Path-Traversal Attack
---------------------------------------------------------------------

A path traversal attack, also known as directory traversal, is a type 
of security vulnerability that occurs when an application allows input 
to influence file paths used by the system. In such an attack, the 
attacker exploits inadequate security controls to access or manipulate 
files located outside of the intended directory. 

This can lead to unauthorized access, information disclosure, or even 
system compromise.

Here's how it works:

> Vulnerability in Handling User Input: The attack becomes possible when 
    an application takes input from the user (like a filename or path) and 
    uses it to access file system resources without properly sanitizing 
    or validating this input.

> Exploiting Relative File Paths: Attackers exploit this by using special 
    characters like ".." (dot-dot) to navigate up the directory tree 
    (relative path traversal). For instance, by replacing an expected 
    filename in a URL or input field with something like ../../etc/passwd, 
    they might access files in directories the application should not have 
    access to.

> Impact of the Attack: Depending on the system's configuration and the 
    application's privileges, this could allow the attacker to read 
    sensitive files, modify system configurations, execute commands, or 
    even gain control over the server.

> Prevention and Mitigation: To prevent path traversal attacks, developers 
    should avoid using user input to directly access the file system. 
    If this is unavoidable, strict input validation and sanitization should 
    be implemented. 
    Additionally, using secure coding practices, maintaining a strong security 
    posture, and implementing principle of least privilege can also help 
    mitigate such attacks.





