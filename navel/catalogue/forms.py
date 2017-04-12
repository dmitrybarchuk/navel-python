# -*- coding: utf-8 -*-
from django import forms

from catalogue.models import Conditioner, Brand, Type, BlockType


class CatalogueFilterForm(forms.Form):
    brand__in = forms.ModelMultipleChoiceField(queryset=Brand.objects.all().order_by('title'), required=False,
                                               widget=forms.CheckboxSelectMultiple(), label=u'Бренд')
    type__in = forms.ModelMultipleChoiceField(queryset=Type.objects.all().order_by('title'), required=False,
                                              widget=forms.CheckboxSelectMultiple(), label=u'Тип')

    block_type__in = forms.ModelMultipleChoiceField(queryset=BlockType.objects.all().order_by('title'), required=False,
                                                    widget=forms.CheckboxSelectMultiple(),
                                                    label=u'Тип внутреннего блока')

    inverter = forms.BooleanField(required=False, label=u'Инвертер')

    def clean(self):
        cleaned_data = super(CatalogueFilterForm, self).clean()

        for k in cleaned_data.keys():
            if not cleaned_data.get(k, False):
                del cleaned_data[k]

        return cleaned_data

    def as_selected(self):
        # "Returns this form rendered as HTML <p>s."
        output = ''
        for name, field in self.fields.items():
            bf = self[name]
            if bf.data:
                output += '%s ' % bf.label
        for key in self.data:
            # get values of each key
            values = self.data.getlist(key)
            # todo: parse it, get title of each value
        return output


class ConditionerAdminForm(forms.ModelForm):
    class Meta:
        model = Conditioner
        exclude = ()
