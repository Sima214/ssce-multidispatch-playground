tests_logfile = meson.build_root() + '/meson-logs/testlog.json'

greeter_test = executable('greeter_test', 'greeter.c',
                          include_directories: greeter_headers,
                          c_args: common_args + common_defs + greeter_definitions_external,
                          cpp_args: common_args + common_defs + greeter_definitions_external,
                          build_by_default: false,
                          link_with: greeter_lib,
                          override_options: ['b_lto=false'])

test('greeter', greeter_test)
