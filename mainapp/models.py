import os
from django.db import models


from studysite.settings import BASE_DIR, AUTH_USER_MODEL

from docxtpl import DocxTemplate, InlineImage
from docx.shared import Mm



class Template1(models.Model):
    ANSWER_TABLE1 = (
        ('Да', 'Да'),
        ('Нет', 'Нет'),
        ('М/б', 'М/б'),
    )

    ANSWER_GENERAL_NOTES = (
        ('Да', 'Да'),
        ('Нет', 'Нет'),
    )

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
    theme1_info1_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme1_info1_note = models.CharField(max_length=50, null=True, blank=True)
    theme1_info2_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme1_info2_note = models.CharField(max_length=50, null=True, blank=True)
    theme1_info3_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme1_info3_note = models.CharField(max_length=50, null=True, blank=True)
    theme1_info4_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme1_info4_note = models.CharField(max_length=50, null=True, blank=True)

    theme2_info1_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme2_info1_note = models.CharField(max_length=50, null=True, blank=True)
    theme2_info2_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme2_info2_note = models.CharField(max_length=50, null=True, blank=True)
    theme2_info3_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme2_info3_note = models.CharField(max_length=50, null=True, blank=True)
    theme2_info4_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme2_info4_note = models.CharField(max_length=50, null=True, blank=True)

    theme3_info1_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme3_info1_note = models.CharField(max_length=50, null=True, blank=True)
    theme3_info2_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme3_info2_note = models.CharField(max_length=50, null=True, blank=True)
    theme3_info3_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme3_info3_note = models.CharField(max_length=50, null=True, blank=True)
    theme3_info4_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme3_info4_note = models.CharField(max_length=50, null=True, blank=True)

    theme4_info1_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme4_info1_note = models.CharField(max_length=50, null=True, blank=True)
    theme4_info2_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme4_info2_note = models.CharField(max_length=50, null=True, blank=True)
    theme4_info3_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme4_info3_note = models.CharField(max_length=50, null=True, blank=True)
    theme4_info4_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme4_info4_note = models.CharField(max_length=50, null=True, blank=True)

    theme5_info1_answer = models.CharField(max_length=10, null=True, blank=True, choices=ANSWER_TABLE1)
    theme5_info1_note = models.CharField(max_length=50, null=True, blank=True)

    #Table 2
    table2_name_inspector1 = models.CharField(max_length=50, null=True, blank=True)
    table2_date1 = models.DateField(null=True, blank=True)
    table2_signature1 = models.ImageField(upload_to='signatures/', null=True, blank=True)
    table2_name_inspector2 = models.CharField(max_length=50, null=True, blank=True)
    table2_date2 = models.DateField(null=True, blank=True)
    table2_signature2 = models.ImageField(upload_to='signatures/', null=True, blank=True)

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
    note1_answer1 = models.CharField(max_length=50, null=True, blank=True, choices=ANSWER_GENERAL_NOTES)
    note1_answer2 = models.CharField(max_length=50, null=True, blank=True, choices=ANSWER_GENERAL_NOTES)
    note2_type = models.CharField(max_length=50, null=True, blank=True)
    note2_text = models.CharField(max_length=50, null=True, blank=True)
    note2_answer1 = models.CharField(max_length=50, null=True, blank=True, choices=ANSWER_GENERAL_NOTES)
    note2_answer2 = models.CharField(max_length=50, null=True, blank=True, choices=ANSWER_GENERAL_NOTES)
    note3_type = models.CharField(max_length=50, null=True, blank=True)
    note3_text = models.CharField(max_length=50, null=True, blank=True)
    note3_answer1 = models.CharField(max_length=50, null=True, blank=True, choices=ANSWER_GENERAL_NOTES)
    note3_answer2 = models.CharField(max_length=50, null=True, blank=True, choices=ANSWER_GENERAL_NOTES)


    name_inspector2 = models.CharField(max_length=50, null=True, blank=True)
    date_inspector2 = models.DateField(null=True, blank=True)
    phone_inspector2 = models.CharField(max_length=50, null=True, blank=True)
    type_inspector2 = models.CharField(max_length=50, null=True, blank=True)
    subsystem_inspector2 = models.CharField(max_length=50, null=True, blank=True)
    count_inspector2 = models.CharField(max_length=50, null=True, blank=True)

    name_inspector3 = models.CharField(max_length=50, null=True, blank=True)
    date_inspector3 = models.DateField(null=True, blank=True)
    signature_inspector = models.ImageField(upload_to='signatures/', null=True, blank=True)

    inspector = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='templates1', verbose_name='Инспектор')
    template1_status = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        if self.id:
            tpl = DocxTemplate(os.path.join(BASE_DIR, 'mediafiles/template1.docx'))
            context = {
                'number_order1': self.number_order1, 'number_order2': self.number_order2,
                'date_order': self.date_order, 'name_client1': self.number_order2,
                'name_client2': self.name_client2, 'name_client3': self.name_client3,
                'date_client': self.date_client, 'email': self.email,
                'number_project1': self.number_project1, 'name_project': self.name_project,
                'date_install': self.date_install, 'address_project': self.address_project,
                'date_project': self.date_project, 'name_client4': self.name_client4,
                'status_project': self.status_project, 'text1': self.text1,
                'text2': self.text2, 'text3': self.text3,
                'date_text': self.date_text,
                'company': self.company, 'installer': self.installer,
                'theme1_info1_answer': self.theme1_info1_answer,
                'theme1_info1_note': self.theme1_info1_note,
                'theme1_info2_answer': self.theme1_info2_answer,
                'theme1_info2_note': self.theme1_info2_note,
                'theme1_info3_answer': self.theme1_info3_answer,
                'theme1_info3_note': self.theme1_info3_note,
                'theme1_info4_answer': self.theme1_info4_answer,
                'theme1_info4_note': self.theme1_info4_note,
                'theme2_info1_answer': self.theme2_info1_answer,
                'theme2_info1_note': self.theme2_info1_note,
                'theme2_info2_answer': self.theme2_info2_answer,
                'theme2_info2_note': self.theme2_info2_note,
                'theme2_info3_answer': self.theme2_info3_answer,
                'theme2_info3_note': self.theme2_info3_note,
                'theme2_info4_answer': self.theme2_info4_answer,
                'theme2_info4_note': self.theme2_info4_note,
                'theme3_info1_answer': self.theme3_info1_answer,
                'theme3_info1_note': self.theme3_info1_note,
                'theme3_info2_answer': self.theme3_info2_answer,
                'theme3_info2_note': self.theme3_info2_note,
                'theme3_info3_answer': self.theme3_info3_answer,
                'theme3_info3_note': self.theme3_info3_note,
                'theme3_info4_answer': self.theme3_info4_answer,
                'theme3_info4_note': self.theme3_info4_note,
                'theme4_info1_answer': self.theme4_info1_answer,
                'theme4_info1_note': self.theme4_info1_note,
                'theme4_info2_answer': self.theme4_info2_answer,
                'theme4_info2_note': self.theme4_info2_note,
                'theme4_info3_answer': self.theme4_info3_answer,
                'theme4_info3_note': self.theme4_info3_note,
                'theme4_info4_answer': self.theme4_info4_answer,
                'theme4_info4_note': self.theme4_info4_note,
                'table2_name_inspector1': self.table2_name_inspector1,
                'table2_date1': self.table2_date1,
                'table2_signature1': InlineImage(tpl=tpl, image_descriptor=self.table2_signature1,
                                                 width=Mm(10)),
                'table2_name_inspector2': self.table2_name_inspector2,
                'table2_date2': self.table2_date2,
                'table2_signature2': InlineImage(tpl=tpl, image_descriptor=self.table2_signature2,
                                                 width=Mm(10)),
                'number_order3': self.number_order3, 'number1': self.number1,
                'name_inspector1': self.name_inspector1,
                'date_inspector1': self.date_inspector1,
                'phone_inspector1': self.phone_inspector1,
                'type_inspector1': self.type_inspector1,
                'subsystem_inspector1': self.subsystem_inspector1,
                'count_inspector1': self.count_inspector1,
                'note1_type': self.note1_type, 'note1_text': self.note1_text,
                'note1_answer1': self.note1_answer1, 'note1_answer2': self.note1_answer2,
                'note2_type': self.note2_type, 'note2_text': self.note2_text,
                'note2_answer1': self.note2_answer1, 'note2_answer2': self.note2_answer2,
                'note3_type': self.note3_type, 'note3_text': self.note3_text,
                'note3_answer1': self.note3_answer1, 'note3_answer2': self.note3_answer2,
                'name_inspector2': self.name_inspector2,
                'date_inspector2': self.date_inspector2,
                'phone_inspector2': self.phone_inspector2,
                'type_inspector2': self.type_inspector2,
                'subsystem_inspector2': self.subsystem_inspector2,
                'count_inspector2': self.count_inspector2,
                'name_inspector3': self.name_inspector3,
                'date_inspector3': self.date_inspector3,
                'signature_inspector': InlineImage(tpl=tpl, image_descriptor=self.signature_inspector,
                                                   width=Mm(10)),
            }

            tpl.render(context)
            tpl.save('mediafiles/templates1/template1_' + str(self.id) + '.docx')
        super().save(*args, **kwargs)



class ContactsComments(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    comment = models.TextField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы из стр контакты'