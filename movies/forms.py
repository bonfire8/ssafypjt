from django import forms
from movies.models import MovieComment

class MovieCommentForm(forms.ModelForm):
    # rank = forms.IntegerField(
    #     widget=forms.Textarea(
    #         attrs={
    #             'rows' : 1,
    #             'cols' : 1
    #         }
            
    #     )
    # )

    rank_one = 1
    rank_two = 2
    rank_three = 3
    rank_four =  4
    rank_five = 5

    rank_choice = [
        (rank_one, '1'),
        (rank_two, '2'),
        (rank_three, '3'),
        (rank_four, '4'),
        (rank_five, '5'),
    ]

    rank = forms.ChoiceField(choices=rank_choice, widget=forms.Select())

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