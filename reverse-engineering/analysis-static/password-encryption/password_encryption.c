#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

void encrypt_password(char password[], int key)
{
    for(int i=0; i< strlen(password); i++)
    {
        password[i] = password[i] + key;
    }
}

bool check_password(char* password, int key)
{
    encrypt_password(password, key);
    printf("password = %s\n", password);
    if(strcmp("xywjslljmjnr", password) == 0)
    {
        return true;    
    }    
    else
        return false;
}

int main()
{
    char password[256]; 
    int key = 5;
    // strenggeheim

    printf("password> ");
    scanf("%s", password);

    if(check_password(password,5))
    {
        printf("Welcome, you have entered a valid password!\n");
    }
    else
    {
        printf("Login rejected, invalid password!\n");
    }

	return 0;
}
