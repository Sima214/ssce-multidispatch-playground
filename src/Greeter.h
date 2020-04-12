#ifndef TEMPLATE_GREETER
#define TEMPLATE_GREETER
/**
 * @file
 * @brief Constructs greet strings.
 */

/**
 * Greeter interface for C.
 *
 * @param who Who to greet.
 * @return dynamically allocated Greetings.
 */
GREETER_EXPORT char* get_greet(const char* who);

/**
 * Returns a dynamically allocated hello world string.
 */
GREETER_EXPORT char* get_hello_world();

#endif /*TEMPLATE_GREETER*/