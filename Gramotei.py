print("""
Gramotei v1.0
Автор: Данил Пистолетов
Сайт: danil-pistoletov.org
""")
text = str()
while text != "стоп" or text != "Стоп":
    text = input("Для завершения введите \"Стоп\". Для исправления - введите текст\n")
    text = text.replace(" .", ".")
    text = text.replace(" ,", ",")
    text = text.replace(" :", ":")
    text = text.replace(" !", "!")
    text = text.replace(" ?", "?")
    text = text.replace(" ;", ";")

    print(text)