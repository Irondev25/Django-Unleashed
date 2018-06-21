from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import (View, DetailView, CreateView,
                                    DeleteView, UpdateView)
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Tag, Startup, Newslink
from .forms import TagForm, NewslinkForm, StartupForm


class TagList(View):
    template_name = 'organizer/tag_list.html'
    model = Tag

    def get(self, request):
        return redirect('organizer_tag:page', page_number=1)

class TagPageList(View):
    template_name = 'organizer/tag_list.html'
    paginate_by = 5
    model = Tag

    def get(self, request, page_number):
        tags = self.model.objects.all()
        paginator = Paginator(tags, self.paginate_by)

        try:
            page = paginator.page(page_number)
        except EmptyPage:
            page = paginator.page(
                paginator.num_pages
            )
        except PageNotAnInteger:
            page = paginator.page(
                1
            )

        if page.has_next():
            next_url = reverse(
                'organizer_tag:page',
                kwargs={
                    'page_number': page.next_page_number()  
                }
            )
        else:
            next_url = None
        
        if page.has_previous():
            prev_url = reverse(
                'organizer_tag:page',
                kwargs={
                    'page_number': page.previous_page_number()
                }
            )
        else:
            prev_url = None
        
        context = {
            'is_paginated': page.has_other_pages(),
            'next_page_url': next_url,
            'previous_page_url': prev_url,
            'paginator': paginator,
            'tag_list': page
        }
        return render(
            request,
            self.template_name,
            context
        )


class TagDetail(DetailView):
    model = Tag
    

class TagCreate(CreateView):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


class TagUpdate(UpdateView):
    template_name = 'organizer/tag_form_update.html'
    model = Tag
    form_class = TagForm


class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer:tag_list')


class StartupList(View):
    template_name = 'organizer/startup_list.html'
    model = Startup
    paginate_by = 5
    page_kwarg = 'page'

    def get(self, request):
        startups = self.model.objects.all()
        paginator = Paginator(startups, self.paginate_by)
        page_number = request.GET.get(self.page_kwarg)
        try:
            page = paginator.page(page_number)
        except PageNotAnInteger:
            page = paginator.page(1)
        except EmptyPage:
            page = paginator.page(paginator.num_pages)
        #if next page is available
        if page.has_next():
            next_url = "?{page}={n}".format(
                page=self.page_kwarg, n=page.next_page_number())
        else:
            next_url = None
        #if previous page is available
        if page.has_previous():
            prev_url = "?{page}={n}".format(
                page=self.page_kwarg, n=page.previous_page_number())
        else:
            prev_url = None
        context = {'startup_list': page,
                   'paginator': paginator,
                   'is_paginated': page.has_other_pages(),
                   'next_page_url':next_url,
                   'previous_page_url': prev_url}
        return render(request, self.template_name, context)


class StartupDetail(DetailView):
    model = Startup


class StartupCreate(CreateView):
    template_name = 'organizer/startup_form.html'
    form_class = StartupForm


class StartupUpdate(UpdateView):
    template_name = 'organizer/startup_form_update.html'
    form_class = StartupForm
    model = Startup


class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy('organizer_startup:list')


class NewslinkCreate(CreateView):
    template_name = 'organizer/newslink_form.html'
    form_class = NewslinkForm
            

class NewslinkUpdate(View):
    template_name = 'organizer/newslink_form_update.html'
    form_class = NewslinkForm
    model = Newslink

    def get(self, request, pk):
        newslink = get_object_or_404(Newslink, pk=pk)
        form = self.form_class(instance=newslink)
        context = {
            'newslink': newslink,
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request, pk):
        newslink = get_object_or_404(Newslink, pk=pk)
        form = self.form_class(request.POST, instance=newslink)
        context = {
            'form': form,
            'newslink': newslink
        }
        if form.is_valid():
            updated_link = form.save()
            return redirect(updated_link)
        else:
            return render(request, self.template_name, context)


class NewslinkDelete(DeleteView):
    model = Newslink

    def get_success_url(self):
        return self.object.startup.get_absolute_url()