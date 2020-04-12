#ifndef TEMPLATE_GREETER_HPP
#define TEMPLATE_GREETER_HPP
/**
 * @file
 * @brief Says hello to someone of your choosing.
 */

#include <string>

extern "C" {
#include "Greeter.h"
}

namespace example {

const std::string WORLD = "World";

class Greeter {
 protected:
  /**
   * Who to greete.
   */
  const std::string& who;

 public:
  /**
   * Constructs a new Greeter who greets w.
   */
  constexpr Greeter(const std::string& w) : who(w){};

  /**
   * Constructs a new Greeter who greets the world.
   */
  constexpr Greeter() : Greeter(WORLD){};

  /**
   * Generates the greetings.
   *
   * @return the greetings.
   */
  std::string getGreetings();

  // virtual ~Greeter(){};
};

}  // namespace example

#endif /*TEMPLATE_GREETER_HPP*/