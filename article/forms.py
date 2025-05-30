from django import forms
from article.models import Category, BlogArticle

from django_ckeditor_5.widgets import CKEditor5Widget

class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'required' : True
                }
            )
        }

class ArticleForms(forms.ModelForm):
    class Meta:
        model = BlogArticle
        fields = ('category', 'title', 'content', 'image', 'status')
        widgets = {
            'category' : forms.Select(
                attrs={
                    'class' : 'form-control',
                    'id' : 'choices-multiple-remove-button',
                }
            ),
            'title' : forms.TextInput(
                attrs={
                    'class' : 'form-control border px-2',
                    'required' : True
                }
            ),
            'content' : CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              ),
            'status' : forms.CheckboxInput(
                attrs={
                    'class' : 'form-check-input mt-1',
                    'id' : 'flexSwitchCheckDefault',
                    'required' : True
                }
            ),
        }