import os
os.system("cls")

# Title
print("\u001b[32;1m~~Cheems Wormd Tramslator~~")
print("--------------------------\n\n")
print("Gib ONE Wormd to Tramslate (● ω ●)\n\n")


# 3rd Letter replacer
def cheems(word):
    string_list = list(word)
    string_list[2] = "m"
    new_string = "".join(string_list)
    print("\n\n" + new_string)


# Cheems Function Call
cheems(input("\u001b[33;1mGive phrase to translate: "))

# Exit Prompt
input("\n\nPremss EMTER to emxit...")
