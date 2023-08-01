# Copyright 2023 Chilufya Mukuka <mukukachilu@gmail.com>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rest_framework.routers import DefaultRouter
from .views import SupportEmailView, SupportEmailResponseView, send_support_email, send_support_email_response
from django.urls import path, include



urlpatterns = [
    path('support-email/get/', SupportEmailView.as_view()),
    path('support-email-response/get/', SupportEmailResponseView.as_view()),
    path('send-support-email/', send_support_email),
    path('send-support-email-response/', send_support_email_response)
]