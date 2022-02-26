from django import forms
 
class TaskForm(forms.Form):
    name = forms.CharField(max_length=250) #Имя
    email = forms.EmailField(max_length = 254) #Почта
    text = forms.CharField() #Текст
    status = forms.IntegerField(min_value=1, max_value=5) #Статус(1-5)

    