#ifndef MESON_TEST_RESULTS
#define MESON_TEST_RESULTS
/**
 * @file
 * @brief Definitions for executable return values recognized by meson.
 */

#include <stdlib.h>

/**
 * Test completed successfully.
 */
#define TEST_OK EXIT_SUCCESS

/**
 * Test failed.
 */
#define TEST_FAIL EXIT_FAILURE

/**
 * Test could not be setup.
 */
#define TEST_ERROR 99

/**
 * Test could not be run.
 */
#define TEST_SKIP 77

#endif /*MESON_TEST_RESULTS*/