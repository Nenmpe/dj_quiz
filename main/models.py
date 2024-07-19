from django.db import models
import uuid, random


# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Question(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    question = models.CharField(max_length=500)
    marks = models.IntegerField(default=5)

    def __str__(self):
        return self.question

    def get_answers(self):
        ans_obj = list(Answer.objects.filter(question=self))
        ans_context = []
        random.shuffle(ans_obj)

        for ans in ans_obj:
            ans_context.append({
                'ans': ans.answer,
                'is_correct': ans.is_correct,
            })

        return ans_context


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_ans')
    answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer
