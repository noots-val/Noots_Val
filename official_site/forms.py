#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Noots on 2018/02/03.


from django import forms
from django.core.mail import send_mail
from django.conf import settings

__author__ = 'Noots'
__version__ = '1.0'
__date__ = '2018/02/03'


class ContactForm(forms.Form):
    """
    フォーム用クラス
    名前、メールアドレス、本文のフォームを定義
    """

    name = forms.CharField(label='お名前', max_length=100)
    mail_address = forms.EmailField(label='メールアドレス', max_length=100)
    message = forms.CharField(label='お問い合わせ内容', max_length=10000, widget=forms.Textarea)

    def send_email(self):
        """
        「お問い合わせ」画面で使用するメールフォームから、名前とアドレスと本文を受け取り、NootsのGmailへと送信する
        """
        subject = 'メールが届きました'
        name = self.cleaned_data['name']
        mail_address = self.cleaned_data['mail_address']
        received_message = self.cleaned_data['message']
        send_message = 'お名前：' + name + '\nメールアドレス：' + mail_address + '\n内容：\n' + received_message

        from_email = settings.EMAIL_HOST_USER
        to = [settings.EMAIL_HOST_USER]

        send_mail(subject, send_message, from_email, to)
