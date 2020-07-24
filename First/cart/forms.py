from django import forms
from .models import Transaction

class TransactionRawForm(forms.ModelForm):
	class Meta:
		model=Transaction
		fields=[
		]
class TransactionRawForm1(forms.ModelForm):
	class Meta:
		model=Transaction
		fields=[
			'is_buyed'
		]

# class RawProductForm(forms.Form):
# 	title=forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Title Here"}))
# 	price=forms.CharField()
# 	summary=forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Summary here1"}))
# 	new=forms.BooleanField()
# 	def clean_title(self,**args):
# 		title=self.cleaned_data.get("title")
# 		if "@sggs.ac.in" not in title:
# 			raise forms.ValidationError("This isnt a valid title!!")
# 		else:
# 			return title
