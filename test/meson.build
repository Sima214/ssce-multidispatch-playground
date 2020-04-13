tests_logfile = meson.build_root() + '/meson-logs/testlog.json'

gmv_test = executable('gmv_test', 'generic.c',
                          include_directories: multidispatch_headers,
                          c_args: common_args + common_defs + multidispatch_definitions_external,
                          cpp_args: common_args + common_defs + multidispatch_definitions_external,
                          build_by_default: false,
                          link_with: gmv_lib,
                          override_options: ['b_lto=false'])

test('gmv', gmv_test)
