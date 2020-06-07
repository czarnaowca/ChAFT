import requests
import argparse
from termcolor import colored


def check_url(url):
    """
    Check URL if it is accessible from TOR network
    :param url: URL to check
    """
    session = requests.session()
    session.proxies = {"http": "socks5h://localhost:9050", "https": "socks5h://localhost:9050"}

    headers = {"User-agent": "Mozilla 2.0"}

    session.cookies.clear()

    try:
        r = session.get(url, headers=headers, timeout=10)

        if r.status_code == 200:
            print(f"[+] {url} \t {colored('ACCESSIBLE', 'green')}")
        else:
            print(f"[-] {url} \t {colored('NOT ACCESSIBLE', 'red')}")
    except requests.exceptions.ConnectionError as con_exc:
        print(f"[-] {url} \t {colored('NOT ACCESSIBLE', 'red')}")
    except requests.exceptions.Timeout as tim_exc:
        print(f"[-] {url} \t {colored('Timeout error.', 'yellow')}")
    except requests.exceptions.RequestException as req_exc:
        print(f"[-] {url} \t {colored('Error during requesting this URL.', 'yellow')}")



def check_from_file(urls_file):
    """
    Parse file with URLs and check each of them
    :param urls_file: File with URLs
    """
    with open(urls_file) as fp:
        for url in fp:
            check_url(url.replace("\n", ""))


if __name__ in "__main__":
    print("Author: Czarna Owca")
    print("Source: https://github.com/czarnaowca/ChAFT")
    print("Contact: czarna.owca.mail@gmail.com")

    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="Check if URL is accessible from the TOR network")
    parser.add_argument("-f", "--file",
                        help="Parse file with URLs and check if each URL is accessible from the TOR network")
    args = parser.parse_args()

    if args.url:
        check_url(args.url)
    elif args.file:
        check_from_file(args.file)
    else:
        parser.print_help()
