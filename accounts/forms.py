from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Obligatoire. Entrez une adresse email valide.")
    first_name = forms.CharField(max_length=30, required=True, label='Prénom')
    last_name = forms.CharField(max_length=30, required=True, label='Nom')
    
    username = forms.CharField(
        label="Nom d'utilisateur", 
        max_length=150,
        help_text="Obligatoire. 150 caractères maximum. Lettres, chiffres et @/./+/-/_ uniquement.",
        error_messages={
            'unique': "Un utilisateur avec ce nom d'utilisateur existe déjà."
        }
    )

    error_messages = {
        'password_mismatch': "Les deux mots de passe ne correspondent pas.",
    }
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmation du mot de passe"
        
        self.fields['password1'].help_text = "Votre mot de passe doit contenir au moins 8 caractères et ne peut pas être trop courant."
        self.fields['password2'].help_text = "Entrez le même mot de passe que précédemment, pour vérification."
        self.fields['username'].help_text = "Requis. 150 caractères maximum. Lettres, chiffres et @/./+/-/_ uniquement."
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)