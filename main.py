import openai

# Устанавливаем ваш ключ API
openai.api_key = 'your_key'

# Функция для отправки запроса на получение ответа от GPT-3.5
def ask_gpt3(context, prompt):
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-0125",  # Выбираем нужную модель GPT-3.5
        prompt=context + "Вопрос: " + prompt,  # Передаем контекст и запрос
        max_tokens=100  # Максимальное количество токенов в ответе
    )
    return response.choices[0].text.strip()

# Основной код для обмена сообщениями с GPT-3.5
def main():
    # Начальный контекст
    context = "Ты должен определить вопрос позитивный или негативный. Если позитивный, то ты отвечаешь как Бетмен. Если негативный, то как Джокер.\n"

    while True:
        # Запрашиваем ввод пользователя
        user_input = input("Ваш вопрос: ")

        # Запрашиваем ответ от GPT-3.5 на основе текущего контекста и ввода пользователя
        response = ask_gpt3(context, user_input)

        # Выводим ответ AI
        print("AI:", response)

if __name__ == "__main__":
    main()
