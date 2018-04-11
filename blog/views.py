from django.shortcuts import render

from .models import Post
from django.utils import timezone

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login

from django import forms
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm

from .forms import PostForm
from .forms import KeywordForm

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import mpld3

from django.http import HttpResponse

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from pandas import DataFrame

import io

import os
from django.conf import settings

def index(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user) # Redirect to a success page. ...
		else: # Return an 'invalid login' error message.
			return render(request, 'blog/home')
			
	return render(request, 'blog/index.html') # request index.html in templates folder
	
def signup(request):
	if request.method == 'POST': # HTTP method 'POST': if user submits a form
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password) #authenticate by checking for matching users
			login(request, user) #login
			return redirect('post_list')
	else:
		form = SignUpForm()
		
	return render(request, 'registration/signup.html',{'form':form})
	
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'blog/post_list.html', {'posts': posts}) #request = the user request itself, param2 = template file, param3 = data needed by template
	
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	
	return render(request, 'blog/post_detail.html', {'post': post})
	
def post_detail_audience_reactions(request):
	post = get_object_or_404(Post, pk=5)
	post2 = get_object_or_404(Post, pk=14)
	post3 = get_object_or_404(Post, pk=18)
	
	graph1 = graphEnthusiasm()
	graph2 = graphEnthusiasmOverTime()
	
	return render(request, 'blog/post_detail_audience_reactions.html', {'post': post, 'post2': post2, 'post3': post3, 'graph1': graph1, 'graph2': graph2})

def post_detail_choosing_keywords(request):
	post = get_object_or_404(Post, pk=6)
	post2 = get_object_or_404(Post, pk=9)
	post3 = get_object_or_404(Post, pk=10)
	post4 = get_object_or_404(Post, pk=11)
		
	table = tableKeywordFindings()
	table2 = tableKeywordFindings2()
	
	graph1 = graphKeywordFindings()
	
	return render(request, 'blog/post_detail_choosing_keywords.html', {'post': post, 'post2': post2, 'post3': post3, 'post4': post4, 'table': table, 'table2': table2, 'graph1': graph1})

def post_detail_choosing_topics(request):
	post = get_object_or_404(Post, pk=7)
	post2 = get_object_or_404(Post, pk=8)
	post3 = get_object_or_404(Post, pk=12)
	post4 = get_object_or_404(Post, pk=13)
	post5 = get_object_or_404(Post, pk=15)
	post6 = get_object_or_404(Post, pk=16)
	post7 = get_object_or_404(Post, pk=17)
	
	table1 = tableTopicFindings(0)
	table2 = tableTopicFindings(1)
	
	graph = graphCountryCatFindings(1)
	
	if request.method == 'POST':
		form = KeywordForm(request.POST)
		if form.is_valid():
			keyword = form.cleaned_data['keyword']
			return redirect('post_detail_choosing_topics_search', keyword)
	else:
		form = KeywordForm()
	
	return render(request, 'blog/post_detail_choosing_topics.html', {'post': post, 'post2': post2, 'post3': post3, 'post4': post4, 'post5': post5, 'post6': post6, 'post7': post7, 'table1': table1, 'table2': table2, 'form': form, 'graph': graph})

def post_detail_choosing_topics_de(request):
	post = get_object_or_404(Post, pk=7)
	post2 = get_object_or_404(Post, pk=8)
	post3 = get_object_or_404(Post, pk=12)
	post4 = get_object_or_404(Post, pk=13)
	post5 = get_object_or_404(Post, pk=15)
	post6 = get_object_or_404(Post, pk=16)
	post7 = get_object_or_404(Post, pk=17)
	
	table1 = tableTopicFindings(0)
	table2 = tableTopicFindings(1)
	
	graph = graphCountryCatFindings(2)
	
	if request.method == 'POST':
		form = KeywordForm(request.POST)
		if form.is_valid():
			keyword = form.cleaned_data['keyword']
			return redirect('post_detail_choosing_topics_search', keyword)
	else:
		form = KeywordForm()
	
	return render(request, 'blog/post_detail_choosing_topics.html', {'post': post, 'post2': post2, 'post3': post3, 'post4': post4, 'post5': post5, 'post6': post6, 'post7': post7, 'table1': table1, 'table2': table2, 'form': form, 'graph': graph})
	
def post_detail_choosing_topics_fr(request):
	post = get_object_or_404(Post, pk=7)
	post2 = get_object_or_404(Post, pk=8)
	post3 = get_object_or_404(Post, pk=12)
	post4 = get_object_or_404(Post, pk=13)
	post5 = get_object_or_404(Post, pk=15)
	post6 = get_object_or_404(Post, pk=16)
	post7 = get_object_or_404(Post, pk=17)
	
	table1 = tableTopicFindings(0)
	table2 = tableTopicFindings(1)
	
	graph = graphCountryCatFindings(3)
	
	if request.method == 'POST':
		form = KeywordForm(request.POST)
		if form.is_valid():
			keyword = form.cleaned_data['keyword']
			return redirect('post_detail_choosing_topics_search', keyword)
	else:
		form = KeywordForm()
	
	return render(request, 'blog/post_detail_choosing_topics.html', {'post': post, 'post2': post2, 'post3': post3, 'post4': post4, 'post5': post5, 'post6': post6, 'post7': post7, 'table1': table1, 'table2': table2, 'form': form, 'graph': graph})
	
def post_detail_choosing_topics_gb(request):
	post = get_object_or_404(Post, pk=7)
	post2 = get_object_or_404(Post, pk=8)
	post3 = get_object_or_404(Post, pk=12)
	post4 = get_object_or_404(Post, pk=13)
	post5 = get_object_or_404(Post, pk=15)
	post6 = get_object_or_404(Post, pk=16)
	post7 = get_object_or_404(Post, pk=17)
	
	table1 = tableTopicFindings(0)
	table2 = tableTopicFindings(1)
	
	graph = graphCountryCatFindings(4)
	
	if request.method == 'POST':
		form = KeywordForm(request.POST)
		if form.is_valid():
			keyword = form.cleaned_data['keyword']
			return redirect('post_detail_choosing_topics_search', keyword)
	else:
		form = KeywordForm()
	
	return render(request, 'blog/post_detail_choosing_topics.html', {'post': post, 'post2': post2, 'post3': post3, 'post4': post4, 'post5': post5, 'post6': post6, 'post7': post7, 'table1': table1, 'table2': table2, 'form': form, 'graph': graph})
	
def post_detail_choosing_topics_us(request):
	post = get_object_or_404(Post, pk=7)
	post2 = get_object_or_404(Post, pk=8)
	post3 = get_object_or_404(Post, pk=12)
	post4 = get_object_or_404(Post, pk=13)
	post5 = get_object_or_404(Post, pk=15)
	post6 = get_object_or_404(Post, pk=16)
	post7 = get_object_or_404(Post, pk=17)
	
	table1 = tableTopicFindings(0)
	table2 = tableTopicFindings(1)
	
	graph = graphCountryCatFindings(5)
	
	if request.method == 'POST':
		form = KeywordForm(request.POST)
		if form.is_valid():
			keyword = form.cleaned_data['keyword']
			return redirect('post_detail_choosing_topics_search', keyword)
	else:
		form = KeywordForm()
	
	return render(request, 'blog/post_detail_choosing_topics.html', {'post': post, 'post2': post2, 'post3': post3, 'post4': post4, 'post5': post5, 'post6': post6, 'post7': post7, 'table1': table1, 'table2': table2, 'form': form, 'graph': graph})
	
def post_detail_choosing_topics_search(request, pk_letter):
	post = get_object_or_404(Post, pk=7)
	post2 = get_object_or_404(Post, pk=8)
	
	if request.method == 'POST':
		form = KeywordForm(request.POST)
		if form.is_valid():
			keyword = form.cleaned_data['keyword']
			return redirect('post_detail_choosing_topics_search', keyword)
	else:
		form = KeywordForm()
	
	graph1 = graphTopicSearch(pk_letter)
	graph2 = graphTopicSearch2(pk_letter)
	
	return render(request, 'blog/post_detail_choosing_topics_search.html', {'post': post, 'post2': post2, 'graph1': graph1, 'graph2': graph2, 'keyword': pk_letter, 'form': form})

def graphEnthusiasm():
	fig = Figure()
	ax = fig.add_subplot(111)
	
	filename = os.path.join(settings.BASE_DIR, 'blog\\USvideos.csv')
	USVids = pd.read_csv(filename, error_bad_lines=False)
	
	USVids = USVids.drop_duplicates(subset='video_id', keep="last")
	USVids['enthusiasm'] = USVids['likes'] / (USVids['likes'] + USVids['dislikes'])
	
	x = USVids['enthusiasm']
	y = USVids['views']
	
	ax.set_title('Views and Enthusiasm Ratings for Individual Videos in Trending Videos Section')
	ax.set_xlabel('Enthusiasm rating')
	ax.set_ylabel('Views')

	ax.plot(x, y, color='red', marker='o', linestyle='None')
	
	canvas = FigureCanvas(fig)	
	g = mpld3.fig_to_html(fig)
	
	return g

def graphEnthusiasmOverTime():
	fig = Figure()
	ax = fig.add_subplot(111)
	
	filename = os.path.join(settings.BASE_DIR, 'blog\\USvideos.csv')
	USVids = pd.read_csv(filename, error_bad_lines=False)
	
	USVids['enthusiasm'] = USVids['likes'] / (USVids['likes'] + USVids['dislikes'])
	USVids['y'], USVids['d'], USVids['m'] = zip(*USVids['trending_date'].map(lambda x: x.split('.')))
	USVids['ymd'] = USVids['y'] + USVids['m'] + USVids['d']
	USVids['ymd'] = USVids['ymd'].astype(int)

	for x in range (171114, 171131):
		USVids['ymd'] = USVids['ymd'].replace(x,(x - 171114),regex=True)
	for x in range (171201, 171232):
		USVids['ymd'] = USVids['ymd'].replace(x,(x - 171184),regex=True)
	for x in range (180101, 180132):
		USVids['ymd'] = USVids['ymd'].replace(x,(x - 180053),regex=True)
	for x in range (180201, 180229):
		USVids['ymd'] = USVids['ymd'].replace(x,(x - 180122),regex=True)
	for x in range (180301, 180306):
		USVids['ymd'] = USVids['ymd'].replace(x,(x - 180194),regex=True)

	USVidsGrouped = USVids.groupby(['ymd'])['enthusiasm'].mean()
	USVidsGrouped = pd.DataFrame(USVidsGrouped)
	USVidsGrouped.columns = ['avg_enthusiasm']
	USVids = USVids.join(USVidsGrouped, on=['ymd'], how='inner')
	USVids = USVids.filter(items=['ymd', 'avg_enthusiasm'])
	USVids = USVids.drop_duplicates()

	x = USVids['ymd']
	y = USVids['avg_enthusiasm']
	
	ax.set_title('Average Daily Enthusiasm Rating of Entire Trending Videos Section Over Time')
	ax.set_xlabel('Day (i.e. 0 = Day 1)')
	ax.set_ylabel('Average enthusiasm rating')

	ax.plot(x, y, color='red', marker='o', linestyle='None')
	
	canvas = FigureCanvas(fig)	
	g = mpld3.fig_to_html(fig)
	
	return g

def graphKeywordFindings():	
	fig = Figure()
	ax = fig.add_subplot(111)
	
	filename = os.path.join(settings.BASE_DIR, 'blog\\USvideos.csv')
	USVids = pd.read_csv(filename, error_bad_lines=False)
	
	SplitTitle = USVids.title.str.split('\s+',expand=True).stack()
	USVidsSplitTitle = USVids.join(pd.Series(index=SplitTitle.index.droplevel(1), data=SplitTitle.values, name='SplitTitle'))

	USVidsSplitTitle['SplitTitle'] = USVidsSplitTitle['SplitTitle'].replace("\W","",regex=True)
	USVidsSplitTitle['SplitTitle'] = USVidsSplitTitle['SplitTitle'].str.lower()
	USVidsSplitTitle = USVidsSplitTitle[USVidsSplitTitle['SplitTitle'] != '']
	USVidsSplitTitle = USVidsSplitTitle.drop_duplicates()

	WordsByInstanceCount = USVidsSplitTitle.groupby('SplitTitle').agg({'SplitTitle':'count', 'views':'sum', 'trending_date':'nunique'})
	WordsByInstanceCount = WordsByInstanceCount.rename(columns={'SplitTitle':'word_frequency', 'views':'word_total_views', 'trending_date':'days_trended'})
	WordsByInstanceCount['views_over_frequency'] = WordsByInstanceCount['word_total_views']/WordsByInstanceCount['word_frequency']
	WordsByInstanceCount = WordsByInstanceCount.sort_values('views_over_frequency', ascending=False)
	
	x = WordsByInstanceCount['days_trended']
	y = WordsByInstanceCount['views_over_frequency']
	
	ax.set_title('Statistics for Individual Keywords Used in Titles of Trending Videos')
	ax.set_xlabel('Total days in trending section')
	ax.set_ylabel('Total views ÷ total instances of use')

	ax.plot(x, y, marker='o', color='g', linestyle='None')
	
	canvas = FigureCanvas(fig)	
	g = mpld3.fig_to_html(fig)
	
	return g

def graphTopicSearch(keyword):
	keyword = keyword.lower()
	
	fig = Figure()
	ax = fig.add_subplot(111)
	
	filename = os.path.join(settings.BASE_DIR, 'blog\\USvideos.csv')
	USVids = pd.read_csv(filename, error_bad_lines=False)
	
	SplitTags = USVids.tags.str.split('|',expand=True).stack()
	USVidsSplitTags = USVids.join(pd.Series(index=SplitTags.index.droplevel(1), data=SplitTags.values, name='SplitTags'))
	USVidsSplitTags = USVidsSplitTags[USVidsSplitTags['SplitTags'] != '']
	USVidsSplitTags['SplitTags'] = USVidsSplitTags['SplitTags'].replace('"','',regex=True)
	USVidsSplitTags['SplitTags'] = USVidsSplitTags['SplitTags'].str.lower()

	USVidsSplitTags = USVidsSplitTags[USVidsSplitTags['SplitTags'] == keyword]
	
	USVidsSplitTags2 = USVidsSplitTags.groupby(['trending_date'])['views'].sum()
	USVidsSplitTags2 = pd.DataFrame(USVidsSplitTags2)
	USVidsSplitTags2.columns = ['total_views']
	USVidsSplitTags = USVidsSplitTags.join(USVidsSplitTags2, on=['trending_date'], how='inner')
	USVidsSplitTags = USVidsSplitTags.filter(items=['trending_date', 'total_views'])
	USVidsSplitTags = USVidsSplitTags.drop_duplicates(subset='trending_date')
	
	USVidsSplitTags['y'], USVidsSplitTags['d'], USVidsSplitTags['m'] = zip(*USVidsSplitTags['trending_date'].map(lambda x: x.split('.')))
	USVidsSplitTags['ymd'] = USVidsSplitTags['y'] + USVidsSplitTags['m'] + USVidsSplitTags['d']
	USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].astype(int)
	
	for x in range (171114, 171131):
		USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].replace(x,(x - 171114),regex=True)
	for x in range (171201, 171232):
		USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].replace(x,(x - 171184),regex=True)
	for x in range (180101, 180132):
		USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].replace(x,(x - 180053),regex=True)
	for x in range (180201, 180229):
		USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].replace(x,(x - 180122),regex=True)
	for x in range (180301, 180306):
		USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].replace(x,(x - 180194),regex=True)

	x = USVidsSplitTags['ymd']
	y = USVidsSplitTags['total_views']

	ax.set_title('Total Daily Views for Videos Featuring Keyword Over Specified Time Period')
	ax.set_xlabel('Day (i.e. 0 = Day 1)')
	ax.set_ylabel('Views')

	ax.plot(x, y, marker='h', linestyle='solid')
	
	canvas = FigureCanvas(fig)	
	g = mpld3.fig_to_html(fig)
	
	return g

def graphTopicSearch2(keyword):
	keyword = keyword.lower()
	
	fig = Figure()
	ax = fig.add_subplot(111)
	
	filename = os.path.join(settings.BASE_DIR, 'blog\\USvideos.csv')
	USVids = pd.read_csv(filename, error_bad_lines=False)
	
	SplitTags = USVids.tags.str.split('|',expand=True).stack()
	USVidsSplitTags = USVids.join(pd.Series(index=SplitTags.index.droplevel(1), data=SplitTags.values, name='SplitTags'))
	USVidsSplitTags = USVidsSplitTags[USVidsSplitTags['SplitTags'] != '']
	USVidsSplitTags['SplitTags'] = USVidsSplitTags['SplitTags'].replace('"','',regex=True)
	USVidsSplitTags['SplitTags'] = USVidsSplitTags['SplitTags'].str.lower()
		
	USVidsSplitTags['y'], USVidsSplitTags['d'], USVidsSplitTags['m'] = zip(*USVidsSplitTags['trending_date'].map(lambda x: x.split('.')))
	USVidsSplitTags['ymd'] = USVidsSplitTags['y'] + USVidsSplitTags['m'] + USVidsSplitTags['d']
	USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].astype(int)
	
	for x in range (171114, 171131):
		USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].replace(x,(x - 171114),regex=True)
	for x in range (171201, 171232):
		USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].replace(x,(x - 171184),regex=True)
	for x in range (180101, 180132):
		USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].replace(x,(x - 180053),regex=True)
	for x in range (180201, 180229):
		USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].replace(x,(x - 180122),regex=True)
	for x in range (180301, 180306):
		USVidsSplitTags['ymd'] = USVidsSplitTags['ymd'].replace(x,(x - 180194),regex=True)

	USVidsSplitTags = USVidsSplitTags[USVidsSplitTags['SplitTags'] == keyword]
	
	USVidsSplitTags = USVidsSplitTags.groupby(['ymd'])['views'].sum()

	ax.set_title('Total Daily Views for Videos Featuring Keyword Over Specified Time Period')
	ax.set_ylabel('Views')
	
	USVidsSplitTags.plot(ax=ax, kind='bar')
	
	canvas = FigureCanvas(fig)	
	g = mpld3.fig_to_html(fig)
	
	return g
	
def graphCountryCatFindings(country):
	fig = Figure()
	ax = fig.add_subplot(111)
	
	if country == 1:
		filename = os.path.join(settings.BASE_DIR, 'blog\\AnalyzeCA.csv')
	elif country == 2:
		filename = os.path.join(settings.BASE_DIR, 'blog\\AnalyzeDE.csv')
	elif country == 3:
		filename = os.path.join(settings.BASE_DIR, 'blog\\AnalyzeFR.csv')
	elif country == 4:
		filename = os.path.join(settings.BASE_DIR, 'blog\\AnalyzeGB.csv')
	else:
		filename = os.path.join(settings.BASE_DIR, 'blog\\AnalyzeUS.csv')
	
	videos = pd.read_csv(filename, error_bad_lines=False)
	
	if country == 1:
		ax.set_title('Total Trended YouTube Videos per Genre Over Specified Time Period: Canada')
	elif country == 2:
		ax.set_title('Total Trended YouTube Videos per Genre Over Specified Time Period: Germany')
	elif country == 3:
		ax.set_title('Total Trended YouTube Videos per Genre Over Specified Time Period: France')
	elif country == 4:
		ax.set_title('Total Trended YouTube Videos per Genre Over Specified Time Period: United Kingdom')
	else:
		ax.set_title('Total Trended YouTube Videos per Genre Over Specified Time Period: United States')
	
	ax.set_ylabel('Number of videos')
	
	videos = videos.groupby(['category_id'])['video_id'].count()
	videos.plot(ax=ax, kind='bar')
	
	g = mpld3.fig_to_html(fig)
	
	return g
	
def tableKeywordFindings():	
	filename = os.path.join(settings.BASE_DIR, 'blog\\USvideos.csv')
	USVids = pd.read_csv(filename, error_bad_lines=False)
	
	SplitTitle = USVids.title.str.split('\s+',expand=True).stack()
	USVidsSplitTitle = USVids.join(pd.Series(index=SplitTitle.index.droplevel(1), data=SplitTitle.values, name='SplitTitle'))

	USVidsSplitTitle['SplitTitle'] = USVidsSplitTitle['SplitTitle'].replace("\W","",regex=True)
	USVidsSplitTitle['SplitTitle'] = USVidsSplitTitle['SplitTitle'].str.lower()
	USVidsSplitTitle = USVidsSplitTitle[USVidsSplitTitle['SplitTitle'] != '']
	USVidsSplitTitle = USVidsSplitTitle.drop_duplicates()

	WordsByInstanceCount = USVidsSplitTitle.groupby('SplitTitle').agg({'SplitTitle':'count', 'views':'sum', 'trending_date':'nunique'})
	WordsByInstanceCount = WordsByInstanceCount.rename(columns={'SplitTitle':'word_frequency', 'views':'word_total_views', 'trending_date':'days_trended'})
	WordsByInstanceCount['views_over_frequency'] = WordsByInstanceCount['word_total_views']/WordsByInstanceCount['word_frequency']
	WordsByInstanceCount = WordsByInstanceCount.sort_values('views_over_frequency', ascending=False)
	WordsByInstanceCount = WordsByInstanceCount.ix[0:10]
	
	g = WordsByInstanceCount.to_html()
	
	return g

def tableKeywordFindings2():	
	filename = os.path.join(settings.BASE_DIR, 'blog\\USvideos.csv')
	USVids = pd.read_csv(filename, error_bad_lines=False)
	
	SplitTitle = USVids.title.str.split('\s+',expand=True).stack()
	USVidsSplitTitle = USVids.join(pd.Series(index=SplitTitle.index.droplevel(1), data=SplitTitle.values, name='SplitTitle'))

	USVidsSplitTitle['SplitTitle'] = USVidsSplitTitle['SplitTitle'].replace("\W","",regex=True)
	USVidsSplitTitle['SplitTitle'] = USVidsSplitTitle['SplitTitle'].str.lower()
	USVidsSplitTitle = USVidsSplitTitle[USVidsSplitTitle['SplitTitle'] != '']
	USVidsSplitTitle = USVidsSplitTitle.drop_duplicates()

	USVidsSplitTitle['y'], USVidsSplitTitle['d'], USVidsSplitTitle['m'] = zip(*USVidsSplitTitle['trending_date'].map(lambda x: x.split('.')))
	USVidsSplitTitle['ymd'] = USVidsSplitTitle['y'] + USVidsSplitTitle['m'] + USVidsSplitTitle['d']
	USVidsSplitTitle['ymd'] = USVidsSplitTitle['ymd'].astype(int)
	USVidsSplitTitle['ymd2'] = USVidsSplitTitle['ymd']
	USVidsSplitTitle = USVidsSplitTitle[~USVidsSplitTitle['SplitTitle'].isin(["the","of","to","and","a","in","is","it","you","that","he","was","for","on","are","with","as","i","his","they","be","at","one","have","this","from","or","had","by","word","but","what","some","we","can","out","other","were","all","there","when","up","use","your","how","said","an","each","she"])]

	WordsByInstanceCount = USVidsSplitTitle.groupby('SplitTitle').agg({'SplitTitle':'count', 'views':'sum', 'trending_date':'nunique', 'ymd':'min', 'ymd2':'max'})
	WordsByInstanceCount = WordsByInstanceCount.rename(columns={'SplitTitle':'word_frequency', 'views':'word_total_views', 'trending_date':'days_trended', 'ymd':'first_day', 'ymd2':'last_day'})
	WordsByInstanceCount['views_over_frequency'] = WordsByInstanceCount['word_total_views']/WordsByInstanceCount['word_frequency']
	WordsByInstanceCount = WordsByInstanceCount.sort_values('days_trended', ascending=False)	
	WordsByInstanceCount = WordsByInstanceCount.ix[0:50]
	
	g = WordsByInstanceCount.to_html()
	
	return g

def tableTopicFindings(type):
	filename = os.path.join(settings.BASE_DIR, 'blog\\USvideos.csv')
	USVids = pd.read_csv(filename, error_bad_lines=False)
	
	SplitTag = USVids.tags.str.split('|',expand=True).stack()
	USVidsSplitTitle = USVids.join(pd.Series(index=SplitTag.index.droplevel(1), data=SplitTag.values, name='SplitTag'))

	USVidsSplitTitle['SplitTag'] = USVidsSplitTitle['SplitTag'].str.lower()
	USVidsSplitTitle['SplitTag'] = USVidsSplitTitle['SplitTag'].replace('"','',regex=True)
	USVidsSplitTitle = USVidsSplitTitle[USVidsSplitTitle['SplitTag'] != '']
	USVidsSplitTitle = USVidsSplitTitle[USVidsSplitTitle['SplitTag'] != '[none]']
	USVidsSplitTitle = USVidsSplitTitle.drop_duplicates()

	USVidsSplitTitle['y'], USVidsSplitTitle['d'], USVidsSplitTitle['m'] = zip(*USVidsSplitTitle['trending_date'].map(lambda x: x.split('.')))
	USVidsSplitTitle['ymd'] = USVidsSplitTitle['y'] + USVidsSplitTitle['m'] + USVidsSplitTitle['d']
	USVidsSplitTitle['ymd'] = USVidsSplitTitle['ymd'].astype(int)
	USVidsSplitTitle['ymd2'] = USVidsSplitTitle['ymd']

	WordsByInstanceCount = USVidsSplitTitle.groupby('SplitTag').agg({'SplitTag':'count', 'views':'sum', 'trending_date':'nunique', 'ymd':'min', 'ymd2':'max'})
	WordsByInstanceCount = WordsByInstanceCount.rename(columns={'SplitTag':'word_frequency', 'views':'word_total_views', 'trending_date':'days_trended', 'ymd':'first_day', 'ymd2':'last_day'})
	WordsByInstanceCount['views_over_frequency'] = WordsByInstanceCount['word_total_views']/WordsByInstanceCount['word_frequency']
	WordsByInstanceCount = WordsByInstanceCount.sort_values(['days_trended', 'views_over_frequency'], ascending=False)
	
	if type == 1:
		WordsByInstanceCount['disparity'] = WordsByInstanceCount['views_over_frequency']/WordsByInstanceCount['days_trended']
		WordsByInstanceCount = WordsByInstanceCount.sort_values('disparity', ascending=False)
		WordsByInstanceCount = WordsByInstanceCount.filter(items=['word_frequency', 'word_total_views', 'days_trended', 'views_over_frequency', 'disparity'])
		WordsByInstanceCount = WordsByInstanceCount.ix[0:10]
	else:
		WordsByInstanceCount = WordsByInstanceCount.ix[0:50]
	
	g = WordsByInstanceCount.to_html()
	
	return g

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.description = "Lorem ipsum"
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})
	
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk) # pass Post model, pass unique pk value from urls.py
	if request.method == "POST": # user saves edits
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else: # user opens the post to edit
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})