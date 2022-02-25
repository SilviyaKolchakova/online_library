from django import forms

from online_library.web.models import Profile, Book
import os


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image_url': 'Image URL',
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last name',
            'image_url': 'Image URL',
        }


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'type': 'Type',
        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Image',
            'type': 'Type',
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        image_path = self.instance.image.path
        self.instance.delete()
        Book.objects.all().delete()   # Delete all expenses when deleting the Profile
        os.remove(image_path)
        return self.instance

    class Meta:
        model = Profile
        fields = ()