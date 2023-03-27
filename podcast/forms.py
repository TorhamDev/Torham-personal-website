from django import forms


class SearchForm(forms.Form):
    search = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].error_messages = {
                'required': 'پر کردن این فیلد ضروری است!',
                'invalid': 'این فیلد رو به درستی وارد کن!',
            }
        # search
        search = self.fields['search']
        search.required = False
        search.widget.attrs['class'] = 'search-input rtl'
        search.widget.attrs['type'] = 'search'
        search.widget.attrs['dir'] = 'auto'
        search.widget.attrs['aria-label'] = 'Search'
        search.widget.attrs[
            'placeholder'
        ] = 'جستجو...'
        search.error_messages = {
            'required': 'پست ات حتما باید عنوان داشته باشه!',
            'max_length': 'توضیحات پست ات خیلی زیاد شد!',
        }
