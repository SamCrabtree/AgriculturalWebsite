from django import forms 
from .models import Post, Products

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'tag', 'header_image', 'author', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('product_name', 'product_order', 'product_image', 'product_details', 'product_cost', 'product_available')


