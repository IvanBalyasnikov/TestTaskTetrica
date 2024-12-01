import requests
import csv
import time


def main():
    api_url = "https://ru.wikipedia.org/w/api.php"


    animal_counts = {chr(i): 0 for i in range(ord('А'), ord('Я') + 1)}

    cmcontinue = None  
    while True:
        params = {
            "action": "query",
            "list": "categorymembers",
            "cmtitle": "Категория:Животные_по_алфавиту",
            "cmlimit": "500", 
            "cmcontinue": cmcontinue,
            "format": "json"
        }
        response = requests.get(api_url, params=params)
        data = response.json()


        for member in data.get("query", {}).get("categorymembers", []):
            title = member["title"]
            first_letter = title[0].upper()
            if first_letter in animal_counts:
                animal_counts[first_letter] += 1


        cmcontinue = data.get("continue", {}).get("cmcontinue")
        if not cmcontinue:
            break

        time.sleep(1)

    with open("beasts.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Буква", "Количество животных"])
        for letter, count in animal_counts.items():
            writer.writerow([letter, count])


if __name__ == "__main__":
    main()
