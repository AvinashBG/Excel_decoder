from django.forms import ModelForm
from Excel_modify.models import Excel_details

class Excel_form(ModelForm):
    class Meta:
        model=Excel_details
        fields="__all__"

    def clean(self):
        all_clean_data=super(Excel_form,self).clean()
        name=str(all_clean_data['excel_record']).split(".")
        if not name[1]=="xlsx":
            self._errors['excel_record']=self.error_class(["please upload the excel file"])
        return all_clean_data
