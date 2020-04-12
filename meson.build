project('c_cpp_meson_gitlab_appveyor_travis_ci', ['c', 'cpp'], version: '0.1',
        default_options: [
            # Standard version to compile against.
            'c_std=c99', 'cpp_std=c++11',
            # Optimize by default.
            'buildtype=debugoptimized',
            # Extra diagnostic messages.
            'c_args=-Wextra', 'cpp_args=-Wextra',
            # Extra optimizations: Link Time Optimization and no exceptions. 
            'b_lto=true', 'cpp_eh=none',
            # Install options.
            'strip=true'
        ])

# Extra/Utilities
subdir('build-aux')

# Common compiler options.
common_args = []
common_args_checked = []
common_defs = []

# Always use UTF-8 encoding.
foreach c : compilers
    common_args_checked += c.first_supported_argument('-fexec-charset=UTF-8', '/utf-8')
endforeach

# Operating system options.
if os_name == 'windows'
    common_defs += ADD_DEFINE_TEMPLATE.format('_CRT_SECURE_NO_WARNINGS')
    common_defs += ADD_DEFINE_TEMPLATE.format('WIN32_LEAN_AND_MEAN')
    common_defs += ADD_DEFINE_TEMPLATE.format('UNICODE')
    common_defs += ADD_DEFINE_VALUE_TEMPLATE.format('_WIN32_WINNT', '0x0601')
    common_defs += ADD_DEFINE_VALUE_TEMPLATE.format('WINVER', '0x0601')
elif os_name == 'linux'
    common_defs += ADD_DEFINE_TEMPLATE.format('_GNU_SOURCE')
endif

# Check if common options are supported by the currently used compiler.
foreach arg : common_args
    foreach c : compilers
        c.has_argument(arg)
    endforeach
endforeach

common_args += common_args_checked

# Build library.
subdir('src')

# Define Tests.
subdir('test')

# Packager.
packaged_files = [greeter_lib, greeter_test, tests_logfile]
target_ci_artifact_package = run_target('ci_package', command: artifact_ci_common + artifact_ci_output + packaged_files)
target_ci_artifact_upload = run_target('ci_upload', command: artifact_ci_common + artifact_ci_ftp + packaged_files)