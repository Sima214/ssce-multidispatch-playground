# Extra globals.
compilers = [meson.get_compiler('c'), meson.get_compiler('cpp')]
os_name = target_machine.system()
cpu_name = target_machine.cpu()

# Define Utilities.
ADD_DEFINE_TEMPLATE = '-D@0@'
ADD_DEFINE_VALUE_TEMPLATE = '-D@0@=@1@'

# Required for all auxiliary scripts.
Python = import('python')
python = Python.find_installation()

artifact_script = 'build-aux/artifact.py'
artifact_ci_common = [python, artifact_script,
                      '-n', meson.project_name(),
                      '-os', os_name,
                      '-cpu', cpu_name,
                      '-c', compilers[0].get_id(),
                      '-id', get_option('build_tag'),
                      '-t', get_option('debug') ? 'debug' : 'release']
artifact_ci_output = ['--output', meson.current_build_dir()]
artifact_ci_ftp = ['--ftp-server', get_option('artifact_address'),
                   '--ftp-username', get_option('artifact_username'),
                   '--ftp-password', get_option('artifact_password')]
if get_option('artifact_password_env')
    artifact_ci_ftp += '--ftp-password-env'
endif

# Build debug
summary('Operating System', os_name)
summary('Python Path', python.path())
summary('Python Version', python.language_version())