# Find files.
gmv_src = files('GccMultiVersioning.c')

multidispatch_headers = include_directories('.')

# Generate extra compiler arguments.
multidispatch_definitions = []
multidispatch_definitions_internal = []
multidispatch_definitions_external = []

multidispatch_limit_export = true

if compilers[0].has_function_attribute('visibility')
    multidispatch_definitions += ADD_DEFINE_VALUE_TEMPLATE.format('MULTIDISPATCH_EXPORT', '__attribute__((visibility("default")))')
    multidispatch_definitions_external += ADD_DEFINE_VALUE_TEMPLATE.format('MULTIDISPATCH_EXPORT', '')
elif compilers[0].has_function_attribute('dllexport') and meson.get_compiler('cpp').has_function_attribute('dllimport')
    multidispatch_definitions_internal += ADD_DEFINE_VALUE_TEMPLATE.format('MULTIDISPATCH_EXPORT', '__declspec(dllexport)')
    multidispatch_definitions_external += ADD_DEFINE_VALUE_TEMPLATE.format('MULTIDISPATCH_EXPORT', '__declspec(dllimport)')
else
    warning('Compiler does not support selecting exported symbols!')
    multidispatch_limit_export = false
endif

gmv_lib = library('gmv', gmv_src,
              include_directories: multidispatch_headers,
              c_args: common_args + common_defs + multidispatch_definitions + multidispatch_definitions_internal,
              cpp_args: common_args + common_defs + multidispatch_definitions + multidispatch_definitions_internal,
              install: true,
              gnu_symbol_visibility: multidispatch_limit_export ? 'inlineshidden' : 'default')