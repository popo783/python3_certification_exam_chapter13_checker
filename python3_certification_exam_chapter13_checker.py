# 徹底攻略 Python3 エンジニア認定 [基礎試験] 問題集 第13章 総仕上げ問題の正誤結果表示プログラムです。
# Perplexityを使ってコーディングを行いました。プロンプト履歴は下記の通りです。
# https://www.perplexity.ai/search/pythonte-she-wen-shu-ha40wen-a-tj2Dqz8PQOCz_WqLUQs68g

def quiz_program():
    # 指定された正解
    correct_answers = [
        'C', 'B', 'C', 'D', 'C', 'D', 'D', 'D', 'B', 'C',
        'B', 'B', 'C', 'D', 'B', 'B', 'D', 'C', 'D', 'B',
        'B', 'D', 'A', 'D', 'B', 'C', 'B', 'A', 'C', 'B',
        'A', 'C', 'C', 'C', 'D', 'D', 'B', 'A', 'C', 'B'
    ]

    user_answers = []
    for i, correct_answer in enumerate(correct_answers, start=1):
        print(f'質問 {i}: 正しい答えは何ですか？')
        print("選択肢: A, B, C, D")
        while True:
            user_answer = input("あなたの回答を入力してください (A/B/C/D): ").upper()
            if user_answer in ['A', 'B', 'C', 'D']:
                break
            else:
                print("無効な入力です。A, B, C, D のいずれかを入力してください。")
        user_answers.append({'question': f'質問 {i}', 'user_answer': user_answer, 'correct_answer': correct_answer})

    correct_count = sum(1 for answer in user_answers if answer['user_answer'] == answer['correct_answer'])
    total_questions = len(user_answers)

    print(f"\n結果: {total_questions}問中{correct_count}問正解しました。")
    print(f"正答率: {(correct_count / total_questions) * 100:.2f}%")

    print("\n詳細:")
    for answer in user_answers:
        if answer['user_answer'] == answer['correct_answer']:
            print(f"{answer['question']}: 正解")
        else:
            print(f"{answer['question']}: 不正解 (あなたの回答: {answer['user_answer']}, 正解: {answer['correct_answer']})")

# クイズプログラムを実行
quiz_program()