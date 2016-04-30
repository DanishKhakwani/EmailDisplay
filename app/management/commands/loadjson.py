#!/usr/bin/python

from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand, CommandError
from app.models import Email, User

import json
import datetime
import os

class Command(BaseCommand):
    help = 'Loads email and user table from json files'

    def handle(self, *args, **options):

        with open('./ids.json') as ids_json:
            ids = json.load(ids_json)
            ids_json.close()

        with open('./emails.json') as emails_json:
            emails = json.load(emails_json)
            emails_json.close()

        usersList = []
        usersMap = {}

        for user in ids:
            usersMap = {
                    "user_id": user,
                    "name": ids[user]
            }

            usersList.append(usersMap)
        
        for user in usersList:
            try:
                u = User(**user)
                u.save()
                self.stdout.write(u.user_id + ' created')
            except IntegrityError:
                self.stdout.write(u.user_id + ' SKIPPED')

        for email in emails:
            try:
                jsts = email["timeSent"]

                try:
                    email["timeSent"] = datetime.datetime.fromtimestamp(jsts/1000.0)
                except ValueError:
                    self.stdout.write(e.subject + ' SKIPPED')
                    continue
                    
                e = Email(**email)
                e.save()
            except IntegrityError:
                self.stdout.write(e.subject + ' SKIPPED')
