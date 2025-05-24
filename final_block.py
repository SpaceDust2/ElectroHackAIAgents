from llm import list_available_models, generate_response, get_true_responses
from data import load_dataset, save_sorted_dataset_by_city, sort_by_street
from prompt import isCommercial_true, isCommercial_false, isCommercial_answer, ruAnswer, judge
from termcolor import colored;



if __name__ == "__main__":
    #print("Доступные модели:", list_available_models())

    dataset = load_dataset()
    save_sorted_dataset_by_city(dataset)
    sort_by_street()
    
    # user_input = input("Введите ваш запрос: ")
    # if user_input.lower() in ("exit", "quit"):
    #     exit()

    user_input = {
      "accountId": 4920,
      "address": "Краснодарский край, ст-ца Старокорсунская, ул Чонгарская, д. 276 1",
      "residentsCount": 1,
      "consumption": {
        "1": 2656,
        "2": 2961,
        "3": 2553,
        "4": 2890,
        "5": 3542,
        "6": 3954,
        "7": 3567,
        "8": 2971,
        "9": 6295,
        "10": 3330,
        "11": 3011,
        "12": 2701
      }
    }

    debug = True
    judge = False

    

    response_true = get_true_responses(user_input=user_input,
                                   isCommercial=isCommercial_true, 
                                   debug=debug,
                                   judge=judge,
                                   isCommercial_answer=isCommercial_answer,
                                   ruAnswer=ruAnswer)
   

    response_false = get_true_responses(user_input=str(user_input),
                                   isCommercial=isCommercial_false, 
                                   debug=debug,
                                   judge=judge,
                                   isCommercial_answer=isCommercial_answer,
                                   ruAnswer=ruAnswer)
    
    print(f'Аккаунт для изучения ID: {user_input["accountId"]}')
    print("---1---")
    print(colored('Вывод агентов ориентирующиеся на признаки коммерции (commercial):\n', 'red'))
    print(response_true)
    print("---2---")
    print(colored('Вывод агентов ориентирующиеся на признаки для выявления жилой недвижимости (non-commercial):\n', 'green'))
    print(response_false)
    print("---3---")
    judge = True
    response_judge=get_true_responses(user_input=judge,
                                   isCommercial=f'Вывод агентов ориентирующиеся на признаки коммерции (commercial):{response_true}\n\n Вывод агентов ориентирующиеся на признаки для выявления жилой недвижимости (non-commercial):{response_false}', 
                                   debug=True,
                                   judge=judge,
                                   isCommercial_answer=isCommercial_answer,
                                   ruAnswer=ruAnswer)
    
    print(colored(response_judge, 'blue'))

    response_judge_min=get_true_responses(user_input=judge,
                                   isCommercial=f'Вывод агентов ориентирующиеся на признаки коммерции (commercial):{response_true}\n\n Вывод агентов ориентирующиеся на признаки для выявления жилой недвижимости (non-commercial):{response_false}', 
                                   debug=False,
                                   judge=judge,
                                   isCommercial_answer=isCommercial_answer,
                                   ruAnswer=ruAnswer)
    
    print(colored(response_judge_min, 'yellow'))
