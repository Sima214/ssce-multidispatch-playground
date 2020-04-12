# Find files.
greeter_src = files('Greeter.cpp')

greeter_headers = include_directories('.')

# Generate extra compiler arguments.
greeter_definitions = []
greeter_definitions_internal = []
greeter_definitions_external = []

greeter_limit_export = true

if compilers[0].has_function_attribute('visibility')
    greeter_definitions += ADD_DEFINE_VALUE_TEMPLATE.format('GREETER_EXPORT', '__attribute__((visibility("default")))')
    greeter_definitions_external += ADD_DEFINE_VALUE_TEMPLATE.format('GREETER_EXPORT', '')
elif compilers[0].has_function_attribute('dllexport') and meson.get_compiler('cpp').has_function_attribute('dllimport')
    greeter_definitions_internal += ADD_DEFINE_VALUE_TEMPLATE.format('GREETER_EXPORT', '__declspec(dllexport)')
    greeter_definitions_external += ADD_DEFINE_VALUE_TEMPLATE.format('GREETER_EXPORT', '__declspec(dllimport)')
else
    warning('Compiler does not support selecting exported symbols!')
    greeter_limit_export = false
endif

greeter_lib = library('greeter', greeter_src,
              include_directories: greeter_headers,
              c_args: common_args + common_defs + greeter_definitions + greeter_definitions_internal,
              cpp_args: common_args + common_defs + greeter_definitions + greeter_definitions_internal,
              install: true,
              gnu_symbol_visibility: greeter_limit_export ? 'inlineshidden' : 'default')