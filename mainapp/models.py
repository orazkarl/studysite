from django.db import models

from user_auth.models import User

class Template1(models.Model):
    # Info clients
    number_order1 = models.CharField(max_length=50, null=True, blank=True)
    number_order2 = models.CharField(max_length=50, null=True, blank=True)
    date_order = models.DateField(null=True, blank=True)
    name_client1 = models.CharField(max_length=50, null=True, blank=True)
    name_client2 = models.CharField(max_length=50, null=True, blank=True)
    name_client3 = models.CharField(max_length=50, null=True, blank=True)
    date_client = models.DateField( null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    # Info projects
    number_project1 = models.CharField(max_length=50, null=True, blank=True)
    name_project = models.CharField(max_length=50, null=True, blank=True)
    date_install = models.DateField(null=True, blank=True)
    address_project = models.CharField(max_length=50, null=True, blank=True)
    date_project = models.DateField(null=True, blank=True)
    name_client4 = models.CharField(max_length=50, null=True, blank=True)
    status_project = models.CharField(max_length=50, null=True, blank=True)
    # Customer request
    text1 = models.CharField(max_length=50, null=True, blank=True)
    text2 = models.CharField(max_length=50, null=True, blank=True)
    text3 = models.CharField(max_length=50, null=True, blank=True)
    date_text = models.DateField(null=True, blank=True)
    company = models.CharField(max_length=50, null=True, blank=True)
    installer = models.CharField(max_length=50, null=True, blank=True)
    # Table 1
    theme1_info1_answer = models.CharField(max_length=10, null=True, blank=True)
    theme1_info1_note = models.CharField(max_length=50, null=True, blank=True)
    theme1_info2_answer = models.CharField(max_length=10, null=True, blank=True)
    theme1_info2_note = models.CharField(max_length=50, null=True, blank=True)
    theme1_info3_answer = models.CharField(max_length=10, null=True, blank=True)
    theme1_info3_note = models.CharField(max_length=50, null=True, blank=True)
    theme1_info4_answer = models.CharField(max_length=10, null=True, blank=True)
    theme1_info4_note = models.CharField(max_length=50, null=True, blank=True)

    theme2_info1_answer = models.CharField(max_length=10, null=True, blank=True)
    theme2_info1_note = models.CharField(max_length=50, null=True, blank=True)
    theme2_info2_answer = models.CharField(max_length=10, null=True, blank=True)
    theme2_info2_note = models.CharField(max_length=50, null=True, blank=True)
    theme2_info3_answer = models.CharField(max_length=10, null=True, blank=True)
    theme2_info3_note = models.CharField(max_length=50, null=True, blank=True)
    theme2_info4_answer = models.CharField(max_length=10, null=True, blank=True)
    theme2_info4_note = models.CharField(max_length=50, null=True, blank=True)

    theme3_info1_answer = models.CharField(max_length=10, null=True, blank=True)
    theme3_info1_note = models.CharField(max_length=50, null=True, blank=True)
    theme3_info2_answer = models.CharField(max_length=10, null=True, blank=True)
    theme3_info2_note = models.CharField(max_length=50, null=True, blank=True)
    theme3_info3_answer = models.CharField(max_length=10, null=True, blank=True)
    theme3_info3_note = models.CharField(max_length=50, null=True, blank=True)
    theme3_info4_answer = models.CharField(max_length=10, null=True, blank=True)
    theme3_info4_note = models.CharField(max_length=50, null=True, blank=True)

    theme4_info1_answer = models.CharField(max_length=10, null=True, blank=True)
    theme4_info1_note = models.CharField(max_length=50, null=True, blank=True)
    theme4_info2_answer = models.CharField(max_length=10, null=True, blank=True)
    theme4_info2_note = models.CharField(max_length=50, null=True, blank=True)
    theme4_info3_answer = models.CharField(max_length=10, null=True, blank=True)
    theme4_info3_note = models.CharField(max_length=50, null=True, blank=True)
    theme4_info4_answer = models.CharField(max_length=10, null=True, blank=True)
    theme4_info4_note = models.CharField(max_length=50, null=True, blank=True)

    theme5_info1_answer = models.CharField(max_length=10, null=True, blank=True)
    theme5_info1_note = models.CharField(max_length=50, null=True, blank=True)

    #Table 2
    table2_name_inspector1 = models.CharField(max_length=50, null=True, blank=True)
    table2_date1 = models.DateField(null=True, blank=True)
    table2_signature1 = models.CharField(max_length=50, null=True, blank=True)
    table2_name_inspector2 = models.CharField(max_length=50, null=True, blank=True)
    table2_date2 = models.DateField(null=True, blank=True)
    table2_signature2 = models.CharField(max_length=50, null=True, blank=True)

    number_order3 = models.CharField(max_length=50, null=True, blank=True)
    number1 = models.CharField(max_length=50, null=True, blank=True)

    name_inspector1 = models.CharField(max_length=50, null=True, blank=True)
    date_inspector1 = models.DateField(null=True, blank=True)
    phone_inspector1 = models.CharField(max_length=50, null=True, blank=True)
    type_inspector1 = models.CharField(max_length=50, null=True, blank=True)
    subsystem_inspector1 = models.CharField(max_length=50, null=True, blank=True)
    count_inspector1 = models.CharField(max_length=50, null=True, blank=True)

    # General notes
    note1_type = models.CharField(max_length=50, null=True, blank=True)
    note1_text = models.CharField(max_length=50, null=True, blank=True)
    note1_answer1 = models.CharField(max_length=50, null=True, blank=True)
    note1_answer2 = models.CharField(max_length=50, null=True, blank=True)
    note2_type = models.CharField(max_length=50, null=True, blank=True)
    note2_text = models.CharField(max_length=50, null=True, blank=True)
    note2_answer1 = models.CharField(max_length=50, null=True, blank=True)
    note2_answer2 = models.CharField(max_length=50, null=True, blank=True)
    note3_type = models.CharField(max_length=50, null=True, blank=True)
    note3_text = models.CharField(max_length=50, null=True, blank=True)
    note3_answer1 = models.CharField(max_length=50, null=True, blank=True)
    note3_answer2 = models.CharField(max_length=50, null=True, blank=True)


    name_inspector2 = models.CharField(max_length=50, null=True, blank=True)
    date_inspector2 = models.DateField(null=True, blank=True)
    phone_inspector2 = models.CharField(max_length=50, null=True, blank=True)
    type_inspector2 = models.CharField(max_length=50, null=True, blank=True)
    subsystem_inspector2 = models.CharField(max_length=50, null=True, blank=True)
    count_inspector2 = models.CharField(max_length=50, null=True, blank=True)

    name_inspector3 = models.CharField(max_length=50, null=True, blank=True)
    date_inspector3 = models.DateField(null=True, blank=True)
    signature_inspector = models.CharField(max_length=50, null=True, blank=True)

    inspector = models.ForeignKey(User, on_delete=models.CASCADE, related_name='templates1', verbose_name='Инспектор')
