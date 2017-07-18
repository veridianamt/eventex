from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscrptionFormTest(TestCase):


    def test_form_has_fields(self):
        """form must have for fields"""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """Cpf must only accept digits"""
        form = self.make_validated_form(cpf = 'ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')


    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf = '1234')
        self.assertFormErrorCode(form,'cpf','length')
        #self.assertListEqual(['cpf'], list(form.errors))
        

    def assertFormErrorCode(self, form, field, code ):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0].code
        self.assertEqual(code, exception)


    def make_validated_form(self, **kwargs):
        valid = dict(name='Veridiana Mantecon', cpf = '12345678901',
                    email='veridiana@mt.net', phone='19 3344-5566')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form


