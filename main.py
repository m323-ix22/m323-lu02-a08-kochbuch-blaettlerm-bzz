import json


# Funktion zur Anpassung eines Rezepts an eine neue Anzahl von Personen
def adjust_recipe(recipe, num_people):
    # Verhältnis zwischen der aktuellen Anzahl der Portionen und der neuen Anzahl
    factor = num_people / recipe['servings']

    # Neue Zutatenmenge berechnen, basierend auf dem Faktor
    adjusted_ingredients = {ingredient: int(amount * factor) for ingredient, amount in recipe['ingredients'].items()}

    # Neues Rezept erstellen
    adjusted_recipe = {
        "title": recipe["title"],
        "ingredients": adjusted_ingredients,
        "servings": num_people
    }

    return adjusted_recipe


# Funktion zum Laden eines Rezepts aus einem JSON-String
def load_recipe(json_string):
    # JSON-String in ein Python-Dictionary umwandeln
    recipe = json.loads(json_string)
    return recipe


# Beispielverwendung der Funktionen
if __name__ == '__main__':
    # Ursprüngliches Rezept im JSON-Format
    recipe_json = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}'

    # Rezept laden
    recipe = load_recipe(recipe_json)

    # Rezept für 2 Personen anpassen
    adjusted_recipe = adjust_recipe(recipe, 2)

    # Angepasstes Rezept ausgeben
    print(adjusted_recipe)
