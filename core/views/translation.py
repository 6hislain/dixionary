from ..models import Word
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages

@require_http_methods(['GET'])
def translation_index(request):
	words = Word.objects.all()
	return render(request, 'word/index.html', {'words': words})

@require_http_methods(['GET', 'POST'])
def translation_create(request):
	if request.method == 'GET':
		return render(request, 'word/create.html')

	elif request.method == 'POST':
		language = request.POST['language']

		if Word.objects.filter(language=language).exists():
			messages.info(request, 'Language exists already')
			return redirect('language.create')

		new_language = Word(language=language)
		new_language.save()
		return redirect('language.index')

@require_http_methods(['GET', 'PUT'])
def translation_edit(request, id):
	pass

@require_http_methods(['DELETE'])
def translation_delete(request, id):
	pass