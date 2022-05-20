from django import forms
from movies.models import MovieComment

class MovieCommentForm(forms.ModelForm):
    rank = forms.IntegerField(
        widget=forms.Textarea(
            attrs={
                'rows' : 1,
                'cols' : 1
            }
            
        )
    )
    content = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'rows' : 1,
                'placeholder': '한줄평을 작성해주세용!'
            }
        ),
        required=True
    )
    class Meta:
        model = MovieComment
        fields = ('content', 'rank')
        # exclude = ('movie', 'user',)