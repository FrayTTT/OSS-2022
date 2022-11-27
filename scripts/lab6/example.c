#include <stdio.h>

int main(int argc,          /* кол-во аргументов */
         char const *argv[] /* сам массив аргументов*/)
{
  for(int j = 0; j < argc; j++)
    printf("argv[%d] = %s\n", j, argv[j]);
}
