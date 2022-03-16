''' Create dictionary for name, age & years coding.
Get user's favorite programming languages & store as tuple.
Get user's 3 fav. programming language. Store as list.
Create set intersection of first programming lang. & fav. language.
Add all to dictionary as key:value pairs '''

programmer = {
    "name": input("Enter your name: "),
    "age": input("Enter your age: "),
    "years_coding": input("How many years of coding? ")
}
first = tuple(input("What were the 1st 3 prog. lang. you learned? Separate with comma. ").split(","))
favorite = input("Fav. 3 prog. language? Separate with comma: ").split(", ")
first_favorites = set(first).intersection(set(favorite))

programmer["first"] = first
programmer["favorite"] = favorite
programmer["first_favorites"] = first_favorites

print(programmer)