from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Council

COUNCIL_OPTION = [
        ('Albury', 'Albury'),
        ('Armidale Regional', 'Armidale Regional'),
        ('Ballina', 'Ballina'),
        ('Balranald', 'Balranald'),
        ('Bathurst Regional', 'Bathurst Regional'),
        ('Bega Valley', 'Bega Valley'),
        ('Bellingen', 'Bellingen'),
        ('Blacktown', 'Blacktown'),
        ('Bland', 'Bland'),
        ('Blue Mountains', 'Blue Mountains'),
        ('Broken Hill', 'Broken Hill'),
        ('Byron', 'Byron'),
        ('Cabonne', 'Cabonne'),
        ('Campbelltown', 'Campbelltown'),
        ('Canada Bay', 'Canada Bay'),
        ('Canterbury-Blacktown', 'Canterbury-Blacktown'),
        ('Carrathool', 'Carrathool'),
        ('Central Coast', 'Central Coast'),
        ('Cessnock', 'Cessnock'),
        ('Cobar', 'Cobar'),
        ('Coffs Harbour', 'Coffs Harbour'),
        ('Cumberland', 'Cumberland'),
        ('Eurobodalla', 'Eurobodalla'),
        ('Fairfield', 'Fairfield'),
        ('Gunnedah', 'Gunnedah'),
        ('Gwydir', 'Gwydir'),
        ('Inner West', 'Inner West'),
        ('Kyogle', 'Kyogle'),
        ('Lachlan', 'Lachlan'),
        ('Lithgow', 'Lithgow'),
        ('Liverpool', 'Liverpool'),
        ('Moore Plains', 'Moore Plains'),
        ('Mosman', 'Mosman'),
        ('Murray River', 'Murray River'),
        ('North Sydney', 'North Sydney'),
        ('Northern Beaches', 'Northern Beaches'),
        ('Parramatta', 'Parramatta'),
        ('Snowy Monaro Regional', 'Snowy Monaro Regional'),
        ('Strathfield', 'Strathfield'),
        ('Sydney', 'Sydney'),
        ('Tamworth Regional', 'Tamworth Regional'),
        ('Weddin', 'Weddin'),
        ('Wollondilly', 'Wollondilly'),
        ('Wollongong', 'Wollongong'),
        ('Woollahra', 'Woollahra'),
        ('Yass Valley', 'Yass Valley'),
    ]


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']

class CouncilForm(forms.ModelForm):

    class Meta:
        model = Council
        fields = ['council']

class UpdateCouncilForm(forms.ModelForm):

    class Meta:
        model = Council
        fields = ['council']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']
