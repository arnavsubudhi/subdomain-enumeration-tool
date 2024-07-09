import requests

famous_extensions = [
    ".com", ".org", ".net", ".edu", ".gov", ".mil", ".co", ".io", ".info", ".biz",
    ".us", ".uk", ".ca", ".au", ".de", ".fr", ".jp", ".it", ".nl", ".es",
    ".in", ".cn", ".ru", ".br", ".mx", ".se", ".ch", ".at", ".dk", ".no",
    ".fi", ".be", ".pl", ".nz", ".gr", ".pt", ".cz", ".hu", ".ro", ".tr",
    ".ie", ".sg", ".hk", ".my", ".kr", ".vn", ".th", ".id", ".ph", ".ae",
    ".sa", ".il", ".eg", ".ng", ".za", ".ke", ".gh", ".ua", ".ar", ".cl",
    ".co.in", ".ltd", ".inc", ".cloud", ".app", ".store", ".online", ".website", ".blog",
    ".shop", ".tech", ".dev", ".space", ".club", ".xyz", ".site", ".live", ".media",
    ".digital", ".global", ".company", ".world", ".academy", ".center", ".education", ".network",
    ".studio", ".design", ".art", ".travel", ".money", ".law", ".health", ".music",
    ".game", ".htb", ".thm"
]

def banner():
    print(r"""
                    _                           
                   / \   _ __ _ __   __ ___   __
                  / _ \ | '__| '_ \ / _` \ \ / /
                 / ___ \| |  | | | | (_| |\ V / 
                /_/   \_\_|  |_| |_|\__,_| \_/  
                                
                # Coded By Arnav Subudhi @github.com
    """)

def select_wordlist():
    print("Select a wordlist to use:")
    print("1. Default wordlist")
    print("2. Custom wordlist")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        return "subdmainwordlist.txt"
    elif choice == '2':
        custom_path = input("Enter the path to your custom wordlist: ").strip()
        return custom_path
    else:
        print("Invalid choice. Using default wordlist.")
        return "subdmainwordlist.txt"

def request(url):
    try:
        result = requests.get("https://" + url, timeout=5)
        if result:
            print("[+] Subdomain discovered ----> " + url)
    except requests.RequestException:
        pass

def is_valid_extension(url):
    for ext in famous_extensions:
        if url.endswith(ext):
            return True
    return False

def main():
    banner()
    target_url = input("Please enter the target URL (e.g., example.com): ").strip()
    
    if not is_valid_extension(target_url):
        print("Invalid domain extension. Please use a famous domain extension.")
        return
    
    wordlist_path = select_wordlist()

    try:
        with open(wordlist_path, "r") as wordlist:
            for line in wordlist:
                word = line.strip()
                test_url = word + "." + target_url
                request(test_url)
    except FileNotFoundError:
        print(f"Error: The file {wordlist_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

try:
    main()
except KeyboardInterrupt:
    print("\nProcess interrupted by user. Exiting!!")
