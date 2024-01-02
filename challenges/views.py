# challenges/views.py
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Quiz, UserAnswer, LabScore
from .forms import QuizForm

from labs.models import VideoModel


@login_required
def quiz_detail(request, quiz_id):
    print(f"Attempting to retrieve quiz with ID: {quiz_id}")
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()

    if request.method == 'POST':
        print("POST")
        score = 0

        for question in questions:
            submitted_answer_id = request.POST.get(f'question_{question.id}')
            correct_answer = question.answer_set.filter(is_correct=True).first()

            if submitted_answer_id:
                # Get the selected answer object
                selected_answer = question.answer_set.get(pk=submitted_answer_id)

                # Create a new UserAnswer instance
                user_answer = UserAnswer.objects.create(
                    user=request.user,
                    question=question,
                    selected_answer=selected_answer
                )

                if selected_answer == correct_answer:
                    score += 1
        
        lab_score, created = LabScore.objects.get_or_create(
            user=request.user,
            quiz=quiz,
        )

        # Increment the quiz attempt counter
        lab_score.attempts += 1
        lab_score.save()

        if score > lab_score.score:
            lab_score.score = score
            lab_score.save()

        print(f"Score: {score} out of {len(questions)}")

        return render(request, 'challenges/result.html', {
            'score': score,
            'total_questions': len(questions),
        })

    else:
        form = QuizForm()

    return render(request, 'challenges/detail.html', {'quiz': quiz, 'questions': questions, 'form': form})




# @login_required
# def quiz_detail(request, quiz_id):
#     print(f"Attempting to retrieve quiz with ID: {quiz_id}")
#     quiz = get_object_or_404(Quiz, pk=quiz_id)
#     questions = quiz.question_set.all()

#     if request.method == 'POST':
#         print("POST")
#         score = 0

#         for question in questions:
#             form = QuizForm(request.POST)

#             # Set the user field to the current user
#             form.instance.user = request.user

#             # Set the question field to the current question
#             form.instance.question = question

#             if form.is_valid():
#                 print("Form is valid")

#                 submitted_answer_id = form.cleaned_data.get(f'question_{question.id}')
#                 correct_answer = question.answer_set.filter(is_correct=True).first()

#                 # Get the selected answer object
#                 selected_answer = question.answer_set.get(pk=submitted_answer_id)

#                 # Save the form instance
#                 user_answer = form.save(commit=False)
#                 user_answer.selected_answer = selected_answer  # Store the actual answer object

#                 # Re-set user and question fields
#                 user_answer.user = request.user
#                 user_answer.question = question

#                 user_answer.save()

#                 if submitted_answer_id == correct_answer.id:
#                     score += 1
#             else:
#                 print(form.errors)

#         print(f"Score: {score} out of {len(questions)}")
#         return render(request, 'challenges/result.html', {'score': score, 'total_questions': len(questions)})

#     else:
#         form = QuizForm()

#     return render(request, 'challenges/detail.html', {'quiz': quiz, 'questions': questions, 'form': form})