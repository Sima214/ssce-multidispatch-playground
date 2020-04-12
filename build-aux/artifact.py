import argparse
import ftplib
import io
import os
import random
import sys
import ssl
import tarfile
import time

ARGS_DESC = 'CI Artifact generator and uploader for meson projects.'
FTP_ROOT_FOLDER = 'meson_ci_artifacts'
FTP_RETRIES = 10
FTP_RETRIES_TIMEOUT_MIN = 15
FTP_RETRIES_TIMEOUT_MAX = 60

os.chdir(os.environ['MESON_BUILD_ROOT'])

parser = argparse.ArgumentParser(description=ARGS_DESC)
parser.add_argument('inputs', type=str, nargs='+',
                    help='List of files to include in the artifact.')
parser.add_argument('--project-name', '-n', dest='name', required=True,
                    help='Project name.')
parser.add_argument('--operating-system', '-os', dest='os', required=True,
                    help='Operating system.')
parser.add_argument('--arch', '-cpu', dest='arch', required=True,
                    help='Processor architecture.')
parser.add_argument('--build-id', '-id', dest='id', required=True,
                    help='Build ID. Used to generate output filename.')
parser.add_argument('--compiler', '-c', dest='compiler',
                    help='Compiler name.')
parser.add_argument('--build-type', '-t', dest='type', choices=['debug', 'release'],
                    help='Build type.')
parser.add_argument('--output', '-o', dest='output',
                    help='Store generated artifact inside this directory.')
parser.add_argument('--ftp-server', dest='ftp_server',
                    help='Upload artifact to a ftp server.')
parser.add_argument('--ftp-username', dest='ftp_username',
                    help='Username of the ftp server.')
parser.add_argument('--ftp-password', dest='ftp_password',
                    help='Password of the ftp server.')
parser.add_argument('--ftp-password-env', dest='ftp_password_env', action='store_true',
                    help='Instead of using the value of ftp_password as the password, use the value of the environment variable with the name the value of ftp_password.')

options = parser.parse_args()

# Create in memory archive.
artifact_buffer = io.BytesIO()
artifact_tar = tarfile.open(fileobj=artifact_buffer, mode='w:xz')
for input_filename in options.inputs:
    artifact_tar.add(input_filename, arcname=os.path.basename(input_filename))
artifact_tar.close()
artifact = artifact_buffer.getbuffer()

# File output
if options.output is not None:
    output_filename = "%s-%s-%s-%s-%s-%s.tar.xz" % (
        options.name, options.id, options.os, options.arch, options.compiler, options.type)
    output_path = os.path.join(options.output, output_filename)
    with open(output_path, 'wb') as f:
        f.write(artifact)

# FTP Output
path_structure = [FTP_ROOT_FOLDER, options.name, options.os, options.arch,
                  "%s-%s-%s.tar.xz" % (options.id, options.compiler, options.type)]
if options.ftp_server is not None:
    ftp_success = False
    try_count = 1
    while not ftp_success and try_count <= FTP_RETRIES:
        ftp = ftplib.FTP_TLS(context=ssl.create_default_context())
        # ftp.set_debuglevel(1)
        try:
            ftp.connect(options.ftp_server)
            if options.ftp_username is not None:
                passwd = options.ftp_password
                if options.ftp_password_env:
                    passwd = os.environ[passwd]
                ftp.login(options.ftp_username, passwd)
                ftp.prot_p()
            else:
                print("Warning: FTP anonymous sign in.", flush=True)
                ftp.login()
            for comp in path_structure:
                if comp == path_structure[-1]:
                    artifact_buffer.seek(0, io.SEEK_SET)
                    ftp.storbinary("STOR " + comp, artifact_buffer)
                    ftp_success = True
                else:
                    structure = dict(ftp.mlsd())
                    if comp not in structure or structure[comp]['type'] != 'dir':
                        print("Creating `%s`!" % (comp), flush=True)
                        ftp.mkd(comp)
                    ftp.cwd(comp)
        except ftplib.all_errors as e:
            print(e, flush=True)
        try:
            ftp.quit()
        except ftplib.all_errors as e:
            print(e, flush=True)
        if not ftp_success:
            timeout = random.randint(FTP_RETRIES_TIMEOUT_MIN, FTP_RETRIES_TIMEOUT_MAX)
            print("Waiting %d seconds.\nRetry count: %d" % (timeout, try_count), flush=True)
            try_count += 1
            time.sleep(timeout)
