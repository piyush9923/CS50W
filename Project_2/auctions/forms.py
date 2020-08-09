from django import forms


class create_list(forms.Form):
    item_name = forms.CharField(max_length=255, label="Item Name    ")
    item_desc = forms.CharField(widget=forms.Textarea, label="Description")
    ini_bid = forms.IntegerField(label="Initial Bid")
    image = forms.URLField(label="Image URL")
    item_category = forms.ChoiceField(widget=forms.RadioSelect,
                                      choices=(('Fashion', 'Fashion'), ('Toys', 'Toys'), ('Electronics', 'Electronics')),
                                      label="Category")
