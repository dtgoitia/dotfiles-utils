import signal


def exit_gracefully(sigknum, frame):
    exit()


def override_sigint():
    signal.signal(signal.SIGINT, exit_gracefully)
