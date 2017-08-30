from django.contrib import admin
from .models import Question, Answer, Task, Aspiration, Notification

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'type', 'category','created_at')
    
admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('Question', 'answer', 'preference')
    
    def Question(self, obj):
        return obj.question.text
    
admin.site.register(Answer, AnswerAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','Question')
    
    def Question(self, obj):
        return obj.question.all()
      
    def Task(self, obj):
        return obj.task.name
        
    class Meta:
        verbose_name = 'TaskQuestionMapping'
    
admin.site.register(Task, TaskAdmin)


class AspirationAdmin(admin.ModelAdmin):
    pass
    #list_display = ('onet_code', 'soc_code')
    #def Task(self, obj):
    #    return obj.question.text
admin.site.register(Aspiration, AspirationAdmin)


class Notificationdmin(admin.ModelAdmin):
    list_display = ('heading','description', 'url', 'task', 'created_at')
    #def Task(self, obj):
    #    return obj.question.text
admin.site.register(Notification, Notificationdmin)

