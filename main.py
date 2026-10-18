import random

BANNER = r"""
----------------------------------------------------------
########  ########  ########  ########  #######   ########
##           ##        ##     ####  ##  ##    ##  ##
########     ##        ##     ## ## ##  ######    ########
##           ##        ##     ##  ####  ##  ###   ##
########     ##        ##     ########  ##   ###  ########
----------------------------------------------------------
"""

CREDITS = """
Intelligent Wordlist Generator
Created by: Um41r 4n$ar1
"""


def generate_admin_wordlist(iterations):
    base_words = ["admin", "administrator", "root", "user"]
    numbers = [str(i) for i in range(10)]
    specials = ["!", "@", "#", "$", "%"]

    results = set()
    while len(results) < iterations:
        word = random.choice(base_words)
        num = random.choice(numbers)
        char = random.choice(specials)
        
        # Variations: word+num, word+char+num, capitalized, etc.
        patterns = [
            f"{word}{num}",
            f"{word.capitalize()}{num}",
            f"{word}{char}{num}",
            f"{num}{word}",
        ]
        results.add(random.choice(patterns))

    return results


def generate_profile_wordlist(iterations, profile):
    words = [profile["fname"], profile["lname"]]
    if profile.get("nickname"):
        words.append(profile["nickname"])
    if profile.get("pet_name"):
        words.append(profile["pet_name"])

    # Filter out empty entries
    words = [w for w in words if w]
    specials = ["!", "@", "#", "$", "%", "&", "*", ""]
    digits = [str(profile["age"]), str(profile["month"]), "123", "1", "2024", ""]

    results = set()
    attempts = 0
    max_attempts = iterations * 50

    while len(results) < iterations and attempts < max_attempts:
        attempts += 1
        base = random.choice(words) if words else "pass"
        sep = random.choice(specials)
        num = random.choice(digits)

        patterns = [
            f"{base}{num}",
            f"{base.capitalize()}{num}",
            f"{base}{sep}{num}",
            f"{base.lower()}{sep}",
            f"{num}{base}",
        ]
        results.add(random.choice(patterns))

    return results


def main():
    print(BANNER)
    print(CREDITS)

    try:
        n = int(input("Enter the number of Iterations: ").strip())
    except ValueError:
        print("Invalid number. Defaulting to 10.")
        n = 10

    print("\nSelect the profile type:")
    print("1. Standard / Admin wordlist")
    print("2. Targeted profile wordlist")
    choice = input("Enter choice (1/2): ").strip()

    if choice == "1":
        wordlist = generate_admin_wordlist(n)
        print("\n--- Generated Words ---")
        for word in wordlist:
            print(word)

    elif choice == "2":
        print("\nEnter profile details (leave blank to skip):")
        fname = input("First name: ").strip()
        lname = input("Last name: ").strip()

        age_input = input("Age: ").strip()
        age = age_input if age_input.isdigit() else ""

        pet_name = input("Pet name: ").strip()

        has_nick = input("Has a nickname? (y/n): ").strip().lower()
        nickname = input("Nickname: ").strip() if has_nick in ["y", "yes"] else ""

        month = input("Month of birth (name or number): ").strip()

        profile = {
            "fname": fname,
            "lname": lname,
            "age": age,
            "pet_name": pet_name,
            "nickname": nickname,
            "month": month,
        }

        wordlist = generate_profile_wordlist(n, profile)
        print("\n--- Generated Words ---")
        for word in wordlist:
            print(word)
    else:
        print("Invalid selection.")


if __name__ == "__main__":
    main()
