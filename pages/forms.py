from django.forms import ModelForm

from .models import FullEnquiry, SimpleEnquiry


class SimpleEnquiryForm(ModelForm):
    class Meta:
        model = SimpleEnquiry
        fields = ("name", "email", "phone", "message")

    def __init__(self, *args, **kwargs):
        super(SimpleEnquiryForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["placeholder"] = "Name"
        self.fields["email"].widget.attrs["placeholder"] = "Email"
        self.fields["phone"].widget.attrs["placeholder"] = "Phone"
        self.fields["message"].widget.attrs["placeholder"] = "Message"

        for field in self.fields.values():
            field.widget.attrs['class'] = ('appearance-none border rounded w-full'
            ' mb-2 px-3 text-gray-700 leading-tight focus:outline-none'
            ' focus:shadow-outline hover:bg-blue-100 hover:shadow-lg'
            )

class FullEnquiryForm(ModelForm):
    class Meta:
        model = FullEnquiry
        fields = "__all__"