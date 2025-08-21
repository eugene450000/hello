import argparse
import server
from version import __version__


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v",
                        "--version",
                        action='store_true',
                        help="Print version")
    parser.add_argument("-p",
                        "--port",
                        type=int,
                        help="Server port",
                        default=8080)
    parser.add_argument("-b",
                        "--bind-host",
                        type=str,
                        help="Bind host",
                        default="127.0.0.1")
    return parser


def main():
    params = get_parser().parse_args()

    if params.version:
        print(__version__)
        return 0

    server.run_web_app(host=params.bind_host, port=params.port)


if __name__ == "__main__":
    main()
