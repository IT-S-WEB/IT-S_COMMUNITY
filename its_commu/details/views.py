from django.http import JsonResponse
import os

# Create your views here.
# HTML 파일을 읽어 반환하는 함수
def load_html_file(file_name):
  file_path = os.path.join('templates', file_name)
  with open(file_path, 'r', encoding='utf-8') as file:
    return file.read()

def info_its(request):
  html_content = load_html_file('info_its.html')
  return JsonResponse({'html': html_content})

def info_year(request):
  html_content = load_html_file('info_year.html')
  return JsonResponse({'html': html_content})