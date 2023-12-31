from wtforms import EmailField, FloatField, Form, PasswordField, StringField, validators


class CategoryForm(Form):
    name = StringField('name', [validators.InputRequired(), validators.Length(min=3, max=50)])


class UserForm(Form):
    name = StringField('name', [validators.InputRequired(), validators.Length(min=3, max=50)])
    email = EmailField('email', [validators.InputRequired(), validators.Length(min=3, max=50)])
    password = PasswordField('password', [validators.InputRequired(), validators.Length(min=3, max=50)])


class FinanceForm(Form):
    description = StringField('description', [validators.InputRequired(), validators.Length(min=3, max=50)])
    value = FloatField('value', [validators.InputRequired()])
    finance_type = StringField('finance_type', [validators.InputRequired(), validators.Length(min=3, max=50)])
    category = StringField('category', [validators.InputRequired(), validators.Length(min=3, max=50)])


class AuthForm(Form):
    email = EmailField('email', [validators.InputRequired(), validators.Length(min=3, max=50)])
    password = PasswordField('password', [validators.InputRequired(), validators.Length(min=3, max=50)])
