

class ClientDetailsForm(ModelForm):
    ddata_inicio = DateField(input_formats=settings.DATE_INPUT_FORMATS)
    class Meta:
        model = ClientDetails
