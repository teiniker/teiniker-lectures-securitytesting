Reverse Engineering - Hardcoded Password
-------------------------------------------------------------------------------

Given the executable named "password_check".

$ ./password_check 
password> student
Login rejected, invalid password!

A) Extract Password  
Use static reverse engineering techniques to extract the hardcoded password.
Try to login with the found password - only when you see the following message, 
you have extracted the right password:
    "Welcome, you have entered a valid password!"   

    TODO: "hjHGzu&56nm;"


B) Storage Algorithm 
Describe the algorithm which has been used to build the password:

    TODO: 
    i) iteral="hjHGzu&56nm;:mkhjghfg"
    ii) substring: literal[0] to length[6*2]
        => "hjHGzu&56nm;"
    iii) compare this substring with the entered password

