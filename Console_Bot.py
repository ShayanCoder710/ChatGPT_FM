from openai import OpenAI
from colorama import init , Fore , Style

init()

api_key = "api_key"

client = OpenAI(base_url = 'https://api.gapgpt.app/v1' , api_key = api_key)


while True:

    user_text = input(f"{Fore.LIGHTBLUE_EX}User: {Style.RESET_ALL}")

    if user_text.lower().strip() in ["bye" , "by" , "exit" , "quit"]:
        print(Fore.LIGHTBLACK_EX + "AI: GoodBye" + Style.RESET_ALL)
        break
 
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "system", "content": "اسم تو 'shayan یا شایان ' هست و یک . همیشه با همه دوستانه حرف بزن"},
            {"role" : "user" , "content" : user_text}
        ]
    )
    print(f"{Fore.GREEN}AI : {response.choices[0].message.content}{Style.RESET_ALL}")
