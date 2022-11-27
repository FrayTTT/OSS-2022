#include <stdio.h>

extern char **environ;
int main(int argc, char *argv[])
{
  char **p;
  for (p = environ; *p != NULL; p++) /* перебор всех элементов массива */
    printf("%s\n", *p); /* разыменование указателя */
}
