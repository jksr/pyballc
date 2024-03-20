ballcools_installed = False
ballcools_path = ''
ballcools_version = None

def set_ballcools_path(path):
    global ballcools_path
    ballcools_path = path

def get_ballcools_path():
    global ballcools_path
    return ballcools_path


def check_for_ballcools(force_check=False):
    global ballcools_path
    global ballcools_installed
    global ballcools_version
    if ballcools_installed and not force_check:
        return True
    if ballcools_version is None or force_check:
        import subprocess
        import os
        try:
            ballcools_version = subprocess.check_output([os.path.join(ballcools_path, "ballcools"), "--version"]).decode("utf-8")
            ballcools_installed = True

        except subprocess.CalledProcessError:
            if ballcools_path!='':
                add_msg = f'(tried path {ballcools_path})'
            else:
                add_msg = ''
            raise OSError(
                f"Please make sure you have installed BAllCools"
                f"(https://github.com/jksr/ballcools) and that "
                f"the path is correctly set with `_set_ballcools_path`. {add_msg}"
            )


