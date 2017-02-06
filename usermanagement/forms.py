from django import forms

class UserForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        error_messages = {'required':'Please enter username'},
        widget = forms.TextInput(
            attrs={
            'placeholder':'Username',
            }
        ),
    )

    password = forms.CharField(
        required = True,
        label = 'Password',
        error_messages = {'required':'Please enter initial password'},
        widget = forms.PasswordInput(
            attrs={
            'placeholder':'Password',
            }
        ),
    )

    email = forms.CharField(
        required = False,
        label = 'Email',
        error_messages = {'required':'Please enter email'},
        widget = forms.EmailInput(
            attrs={
            'placeholder':'Email',
            }
        ),
    )

    phone = forms.CharField(
        required = False,
        label = 'Phone',
        error_messages = {'required':'Please enter phone number'},
        widget = forms.TextInput(
            attrs={
            'placeholder':'Phone Number',
            }
        ),
    )

    is_active = forms.BooleanField(
        required = False,
        label = 'Is_active',
        widget = forms.CheckboxInput(),
    )

    is_superuser = forms.BooleanField(
        required = False,
        label = 'Is_superuser',
        widget = forms.CheckboxInput(),
    )

    is_staff = forms.BooleanField(
        required = False,
        label = 'Is_staff',
        widget = forms.CheckboxInput(),
    )

    def clean(self):
        if not self.is_valid:
            raise forms.ValidationError(u"Please enter all items")
        else:
             cleaned_data = super(UserForm, self).clean()
        return cleaned_data

class GroupForm(forms.Form):
	name = forms.CharField(
        required = True,
        label = 'Groupname',
        error_messages = {'required':'Please enter name'},
        widget = forms.TextInput(
            attrs={
            'placeholder':'Group',
            }
        ),
    )

	def clean(self):
		if not self.is_valid:
			raise forms.ValidationError(u"Please enter all items")
		else:
			cleaned_data = super(GroupForm, self).clean()
		return cleaned_data

class ChangepwdForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"Old Password",
        error_messages={'required': u'Please enter old password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"Old Password",
            }
        ),
    )
    newpassword1 = forms.CharField(
        required=True,
        label=u"New Password",
        error_messages={'required': u'Please enter new password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"New Password",
            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label=u"Confirm Password",
        error_messages={'required': u'Please enter new password again'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"Confirm Password",
            }
        ),
     )
    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"Please enter all items")
        elif self.cleaned_data['newpassword1'] <> self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"The new and confirmed passwords do not match. Please type them again")
        else:
            cleaned_data = super(ChangepwdForm, self).clean()
        return cleaned_data

		
