from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs) -> None:
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

        self.fields['username'].label = "Username"
        self.fields['email'].label = "Email"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['username'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})
        self.fields['email'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'myfieldclass form-control'})

        for text in ['username', 'password1', 'password2']:
            self.fields[text].help_text = None