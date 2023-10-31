import random

men = [input() for _ in range(int(input()))]
partner = men.copy()

for man in men:
    friend = random.choice(partner)
    while friend == man:
        friend = random.choice(partner)
    print(f"{man} - {friend}")
    partner.remove(friend)
