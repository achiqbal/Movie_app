from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Movie
from .forms import CreateMovie
from django.template.loader import render_to_string


def home(request):
	user_query = str(request.GET.get('query',''))
	search_result = Movie.objects.filter(title__icontains=user_query)
	context = {
		'movies': search_result
	}
	return render(request, 'movie/home.html', context)

def upload(request):
	form = CreateMovie()
	if request.method == 'POST':
		form = CreateMovie(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = CreateMovie()
	return render(request, 'movie/movie_form.html', {'form': form})

# def upload(request):
# 	form = CreateMovie()
# 	context = {
# 		'form': form
# 	}
# 	html_form = render_to_string('movie_form.html', context, request=request)
# 	return JsonResponse({'html_form': html_form})

def detail(request, pk):
	context = {
		'movies': Movie.objects.get(pk=pk)
	}
	return render(request, 'movie/movie_detail.html', context)

def update(request, pk):
	movies = get_object_or_404(Movie, pk=pk)
	form = CreateMovie(request.POST or None, instance=movies)
	if form.is_valid():
		form.save()
		return redirect('home')
	return render(request, 'movie/movie_form.html', {'form': form})

def delete(request, pk):
	movies = get_object_or_404(Movie, pk=pk)
	movies.delete()
	return redirect('home')