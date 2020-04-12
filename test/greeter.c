#include "results.h"

#include <Greeter.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
  char* str = get_hello_world();
  puts(str);
  free(str);
  return TEST_OK;
}