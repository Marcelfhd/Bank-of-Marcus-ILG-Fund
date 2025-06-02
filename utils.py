import random
from datetime import datetime

def account_number_creator() -> str:
    random_account_number = [random.randint(0, 9) for num in range(5)]
    random_account_number = ("".join(map(str, random_account_number)))
    return random_account_number


def get_current_time() -> str:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def bad_number_catcher(number: str) -> bool:
    if not number.isdigit():
        print("Please enter a valid amount.")
        return False

    elif float(number) <= 0:
        print("Your amount must be greater than zero.")
        return False

    else:
        return True


def bad_name_catcher(name: str) -> bool:
    if not name.isalpha() or len(name) < 3:
        return False
    else:
        return True


def bad_account_number_catcher(account_number: str) -> bool:
    if not account_number.isdigit() or not len(account_number) == 5:
        return False
    else:
        return True


def business_top_g() -> str:

    quote1 = ("'I don’t hire a lot of number-crunchers, and I don’t trust fancy marketing surveys.'",
                "'I do my own surveys and draw my own conclusions.' - Donald Trump: The Art of the Deal")
    quote2 = ("'I’ve read hundreds of books about China over the decades. I know the Chinese.",
"I’ve made a lot of money with the Chinese. I understand the Chinese mind.' - Donald Trump: The Art of the Deal")
    quote3 = "'Play by the rules, but be ferocious.' – Phil Knight"
    quote4 = "'Business opportunities are like buses, there’s always another one coming.' – Richard Branson"
    quote5 = "'If you don't build your dream someone else will hire you to help build theirs.' - Tony Gaskins"
    quote6 = "'Some people dream of success, while other people get up every morning and make it happen.' - Wayne Huizenga"

    return random.choice([quote1, quote2, quote3, quote4, quote5, quote6])


def alpha_male_top_g() -> str:

    alpha_quote1 = "'Silence speaks louder than words, but an alpha male speaks even louder.' - Unknown"
    alpha_quote2 = "'I haven’t lost my virginity because I never lose' - Sigma grindset"
    alpha_quote3 = "'Be the reason why women carry pepper spray' - deleted_user"
    alpha_quote4 = "'A true sigma male roams through life as a lone wolf, thriving in solitude.' - Unknown"
    alpha_quote5 = "'I don’t suffer from insanity. I enjoy every minute of it.' - Unknown"
    alpha_quote6 = "'Damaged people are the most destructive one' - neerajchoithwani6975"

    return random.choice([alpha_quote1, alpha_quote2, alpha_quote3, alpha_quote4, alpha_quote5, alpha_quote6])