#include "Greeter.hpp"

#include <cstddef>
#include <cstdlib>
#include <cstring>
#include <string>

namespace example {

std::string Greeter::getGreetings() {
  return "Hello " + this->who + "!";
}

}  // namespace example

char* get_greet(const char* who) {
  if (who == nullptr) {
    return nullptr;
  }
  std::string      whopp     = std::string(who);
  example::Greeter greeter   = example::Greeter(whopp);
  std::string      greetings = greeter.getGreetings();
  std::size_t      ret_len   = greetings.length() + 1;
  char*            ret       = (char*) malloc(ret_len);
  strncpy(ret, greetings.c_str(), ret_len);
  return ret;
}

char* get_hello_world() {
  example::Greeter greeter;
  std::string      greetings = greeter.getGreetings();
  std::size_t      ret_len   = greetings.length() + 1;
  char*            ret       = (char*) malloc(ret_len);
  strncpy(ret, greetings.c_str(), ret_len);
  return ret;
}