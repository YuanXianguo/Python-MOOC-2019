favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah':['python', 'c'],
    }

for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are: ")
    for language in languages:
        print("\t" + language.title())
