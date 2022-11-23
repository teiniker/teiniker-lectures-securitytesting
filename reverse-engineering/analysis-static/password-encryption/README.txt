Example: Password check
-------------------------------------------------------------------------------

The original C code looks like:

bool check_password(char* password)
{
    if(strlen(password) >= 12 && password[0] == '#' && password[5] == password[9])
    {
        return true;    
    }    
    else
        return false;
}


we can find out how the password string will be checked:

i) Size of the password must be  >= 12

ii) The first character (index 0) of the password must be '#'

If we pick a password which satisfies all these constraints, it will be accepted.

Examples: "#12345000512", "#Hall!000!D00"  
